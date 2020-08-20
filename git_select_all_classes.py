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
            "function":"select_R",
            "usr_ID":1

        }


class Select:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.index = params.get('usr_ID', '')



    def select_Survey(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Select * from User U left join UserId_Survey_assoc usa on usa.UserId_assoc = U.usr_ID left join Survey s on s.surv_ID = usa.Survey_assoc left join Survey_Question_assoc sqa on sqa.Survey_assoc = s.surv_ID left join Question q on q.quest_ID = sqa.Question_assoc left join Question_Answer_assoc qaa on qaa.Question_assoc = q.quest_ID left join Answer a on a.ans_ID = qaa.Answer_assoc Where U.usr_ID = %s", [index])
            
        db.commit()
        record = cursor.fetchall()

        print(record)
        
    def select_Response(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Select r.resp_Content from User U left join UserId_Survey_assoc usa on usa.UserId_assoc = U.usr_ID left join Survey s on s.surv_ID = usa.Survey_assoc left join Survey_Question_assoc sqa on sqa.Survey_assoc = s.surv_ID left join Question q on q.quest_ID = sqa.Question_assoc left join Question_Answer_assoc qaa on qaa.Question_assoc = q.quest_ID left join Answer a on a.ans_ID = qaa.Answer_assoc left join Answer_Response_assoc ara on ara.Answer_assoc = a.ans_ID left join Response r on r.resp_ID = ara.Response_assoc Where U.usr_ID = %s", [index])
            
        db.commit()
        record = cursor.fetchall()

        print(record)


action = Select(var_json)

if action.function == 'select_S':
    output = action.select_Survey()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)
elif action.function == 'select_R':
    output = action.select_Response()
    
        ############ I need to figure out why this is printing null and not a json object ###################
    data = json.dumps(output)
    
    #print(data)