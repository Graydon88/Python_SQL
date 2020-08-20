#import pymysql
import MySQLdb
import json
import sqlite3
import sys
import os




endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
port = "xxxx"
username = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxxx'
database_name = 'xxxxxxxxxxxxxxxxxxxxxxxxx'



db = MySQLdb.connect(host=endpoint, user=username, passwd=password, db=database_name)






var_json = {
            "function":"select",
            "resp_ID":8,
            "resp_Content":"Response.py 1 upd",
            "resp_Date_Modified":"2020-08-01",
            "ans_ID" : 27
            
            
            
        }


class Response:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.index = params.get('resp_ID', '')
        self.content = params.get('resp_Content', '')
        self.datemodified = params.get('resp_Date_Modified', '')
        self.ans_id = params.get('ans_ID', 0)


    def insert_Response(params):
        content = action.content
        datemodified = action.datemodified
        ans_id = action.ans_id
        
        
        cursor = db.cursor()
        cursor.execute("Insert into Response (resp_Content, resp_Date_Modified) Values (%s, %s)", (content, datemodified))
        last_id = db.insert_id()
        db.commit()
        
        cursor = db.cursor()
        cursor.execute("Insert into Answer_Response_assoc (Answer_assoc, Response_assoc) Values (%s, %s)", (ans_id, last_id))
        db.commit()
        return last_id
        
        

    def delete_Response(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Delete from Response where resp_ID = %s", [index])
        db.commit()
        
        cursor.execute("Delete from Answer_Response_assoc where Response_assoc = %s", [index])
        db.commit()
        
    def update_Response(params):
        content = action.content
        datemodified = action.datemodified
        index = action.index
                
        cursor = db.cursor()
        cursor.execute("UPDATE Response SET resp_Content = %s, resp_Date_Modified = %s Where resp_ID = %s", (content, datemodified, index))
        db.commit()
        
        
    def select_Response(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Select * from Response where resp_ID = %s", [index])
        db.commit()
        record = cursor.fetchall()

        print(record)
        



action = Response(var_json)

if action.function == 'insert':
    id = action.insert_Response()
    insertid = json.dumps(str(id))
    print(insertid)

elif action.function == 'select':
    output = action.select_Response()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)
    
elif action.function == 'delete':
    action.delete_Response()
    
elif action.function == 'update':
    action.update_Response()
