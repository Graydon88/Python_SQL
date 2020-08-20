#import pymysql
import MySQLdb
import json
import sqlite3
import sys
import os




endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
port = "xxxx"
username = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
database_name = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'



db = MySQLdb.connect(host=endpoint, user=username, passwd=password, db=database_name)






var_json = {
            "function":"update",
            "ans_ID":27,
            "ans_Content":"answer.py 1 upd",
            "ans_Date_Created": "2020-06-01",
            "ans_Date_Modified":"2020-08-01",
            "ans_Order": 2,
            "quest_ID" : 9
            
            
            
        }


class Answer:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.index = params.get('ans_ID', '')
        self.content = params.get('ans_Content', '')
        self.datecreated = params.get('ans_Date_Created', '')
        self.datemodified = params.get('ans_Date_Modified', '')
        self.quest_id = params.get('quest_ID', 0)
        self.ans_order = params.get('ans_Order', 0)


    def insert_Answer(params):
        content = action.content
        datecreated = action.datecreated
        ans_order = action.ans_order
        quest_id = action.quest_id
        
        
        cursor = db.cursor()
        cursor.execute("Insert into Answer (ans_Content, ans_Date_Created, ans_Order) Values (%s, %s, %s)", (content, datecreated, ans_order))
        last_id = db.insert_id()
        db.commit()
        
        cursor = db.cursor()
        cursor.execute("Insert into Question_Answer_assoc (Question_assoc, Answer_assoc) Values (%s, %s)", (quest_id, last_id))
        db.commit()
        return last_id
        
        

    def delete_Answer(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Delete from Answer where ans_ID = %s", [index])
        db.commit()
        
        cursor.execute("Delete from Question_Answer_assoc where Answer_assoc = %s", [index])
        db.commit()
        
    def update_Answer(params):
        content = action.content
        datemodified = action.datemodified
        ans_order = action.ans_order
        index = action.index
                
        cursor = db.cursor()
        cursor.execute("UPDATE Answer SET ans_Content = %s, ans_Date_Modified = %s, ans_Order = %s Where ans_ID = %s", (content, datemodified, ans_order, index))
        db.commit()
        
        
    def select_Answer(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Select * from Answer where ans_ID = %s", [index])
        db.commit()
        record = cursor.fetchall()

        print(record)
        



action = Answer(var_json)

if action.function == 'insert':
    id = action.insert_Answer()
    insertid = json.dumps(str(id))
    print(insertid)

elif action.function == 'select':
    output = action.select_Answer()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)
    
elif action.function == 'delete':
    action.delete_Answer()
    
elif action.function == 'update':
    action.update_Answer()
