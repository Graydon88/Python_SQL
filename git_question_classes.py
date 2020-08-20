#import pymysql
import MySQLdb
import json
import sqlite3
import sys
import os




endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
port = "xxxx"
username = 'xxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxx'
database_name = 'xxxxxxxxxxxxxxxxxxxxxx'



db = MySQLdb.connect(host=endpoint, user=username, passwd=password, db=database_name)






var_json = {
            "function":"select",
            "quest_ID":9,
            "quest_Content":"question.py 1 upd",
            "quest_Type":"2020-08-28",
            "quest_Date_Created": "2020-06-01",
            "quest_Date_Modified":"2020-08-01",
            "quest_Mult" : 1,
            "quest_Order": 3,
            "surv_ID" : 4
            
            
            
        }


class Question:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.index = params.get('quest_ID', '')
        self.content = params.get('quest_Content', '')
        self.datecreated = params.get('quest_Date_Created', '')
        self.type = params.get('quest_Type', 0)
        self.datemodified = params.get('quest_Date_Modified', '')
        self.survey_id = params.get('surv_ID', 0)
        self.quest_order = params.get('quest_Order', 0)
        self.quest_mult = params.get('quest_Mult', 0)


    def insert_Question(params):
        content = action.content
        type = action.type
        datecreated = action.datecreated
        quest_mult = action.quest_mult
        quest_order = action.quest_order
        survey_id = action.survey_id
        
        
        cursor = db.cursor()
        cursor.execute("Insert into Question (quest_Content, quest_Type, quest_Date_Created, quest_Mult, quest_Order) Values (%s, %s, %s, %s, %s)", (content, type, datecreated, quest_mult, quest_order))
        last_id = db.insert_id()
        db.commit()
        
        cursor = db.cursor()
        cursor.execute("Insert into Survey_Question_assoc (Survey_assoc, Question_assoc) Values (%s, %s)", (survey_id, last_id))
        db.commit()
        return last_id
        
        

    def delete_Question(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Delete from Question where quest_ID = %s", [index])
        db.commit()
        
        cursor.execute("Delete from Survey_Question_assoc where Question_assoc = %s", [index])
        db.commit()
        
    def update_Question(params):
        content = action.content
        type = action.type
        datemodified = action.datemodified
        quest_mult = action.quest_mult
        quest_order = action.quest_order
        index = action.index
                
        cursor = db.cursor()
        cursor.execute("UPDATE Question SET quest_Content = %s, quest_Type = %s, quest_Date_Modified = %s, quest_Mult = %s, quest_Order = %s Where quest_ID = %s", (content, type, datemodified, quest_mult, quest_order, index))
        db.commit()
        
        
    def select_Question(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Select * from Question where quest_ID = %s", [index])
        db.commit()
        record = cursor.fetchall()

        print(record)
        



action = Question(var_json)

if action.function == 'insert':
    id = action.insert_Question()
    insertid = json.dumps(str(id))
    print(insertid)

elif action.function == 'select':
    output = action.select_Question()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)
    
elif action.function == 'delete':
    action.delete_Question()
    
elif action.function == 'update':
    action.update_Question()
