import pymysql
import MySQLdb
import json
import sqlite3
import sys
import os




endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
port = "xxxxxxxx"
username = 'xxxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
database_name = 'xxxxxxxxxxxxxxxxxxx'




db = MySQLdb.connect(host=endpoint, user=username, passwd=password, db=database_name)



    


var_json = {
            "function":"update",
            "surv_Name":"updated survey",
            "surv_Type":"Type 1 upd",
            "surv_Date_Modified":"2020-08-28",
            "surv_Visibility": 1,
            "surv_Date_Created":"2020-07-01",
            "surv_ID" : 4,
            "usr_ID": 20
            
        }



class Survey:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.name = params.get('surv_Name', '')
        self.type = params.get('surv_Type', '')
        self.datecreated = params.get('surv_Date_Created', '')
        self.visibility = params.get('surv_Visibility', 0)
        self.datemodified = params.get('surv_Date_Modified', '')
        self.user_id = params.get('usr_ID', 0)
        self.survey_id = params.get('surv_ID', 0)
        
        
    def insert_Survey(params):
        name = action.name
        type = action.type
        datecreated = action.datecreated
        visibility = action.visibility
        datemodified = action.datemodified
        user_id = action.user_id
        
        
        cursor = db.cursor()
        cursor.execute("Insert into Survey (surv_Name, surv_Type, surv_Date_Modified, surv_Visibility, surv_Date_Created) Values (%s, %s, %s, %s, %s)", (name, type, datemodified, visibility, datecreated))
        last_id = db.insert_id()
        db.commit()
        
        cursor = db.cursor()
        cursor.execute("Insert into UserId_Survey_assoc (UserId_assoc, Survey_assoc) Values (%s, %s)", (user_id, last_id))
        db.commit()
        return last_id
        
        

    def delete_Survey(params):
        index = action.survey_id
        
        cursor = db.cursor()
        cursor.execute("Delete from Survey where surv_ID = %s", [index])
        db.commit()
        
        cursor.execute("Delete from UserId_Survey_assoc where Survey_assoc = %s", [index])
        db.commit()
        
    def update_Survey(params):
        name = action.name
        type = action.type
        visibility = action.visibility
        datemodified = action.datemodified
        survey_id = action.survey_id
                
        cursor = db.cursor()
        cursor.execute("UPDATE Survey SET surv_Name = %s, surv_Type = %s, surv_Date_Modified = %s, surv_Visibility = %s Where surv_ID = %s", (name, type, datemodified, visibility, survey_id))
        db.commit()
        
        
    def select_Survey(params):
        index = action.survey_id
        
        cursor = db.cursor()
        cursor.execute("Select * from Survey where surv_ID = %s", [index])
        db.commit()
        record = cursor.fetchall()

        print(record)
        



action = Survey(var_json)

if action.function == 'insert':
    id = action.insert_Survey()
    insertid = json.dumps(str(id))
    print(insertid)

elif action.function == 'select':
    output = action.select_Survey()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)
    
elif action.function == 'delete':
    action.delete_Survey()
    
elif action.function == 'update':
    action.update_Survey()
