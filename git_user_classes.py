import pymysql
import MySQLdb
import json
import sqlite3
import sys
import os




endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
port = "xxxx"
username = 'xxxxxxxxxxxxxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxx'
database_name = 'xxxxxxxxxxxxxx'



db = MySQLdb.connect(host=endpoint, user=username, passwd=password, db=database_name)



    


var_json = {
            "function":"select",
            "usr_Last_Name":"last name",
            "usr_First_Name":"first name",
            "usr_Middle_Name":"middle name",
            "usr_Suffix_Name":"Mrs.",
            "usr_Title_Name":"pres",
            "usr_State":"ca",
            "usr_Industry":"Sales",
            "usr_Role":"CEO",
            "usr_Company":"MyCompany",
            "usr_Date_Created":"2020-08-18",
            "usr_Date_Modified":"2020-08-18",
            "usr_Company_Size":"1",
            "usr_ID":"8",
            "usr_Auth_Zero":"1224"
        }



class User:
    def __init__(self, params):
        self.function = params.get('function', '')
        self.lname = params.get('usr_Last_Name', '')
        self.fname = params.get('usr_First_Name', '')
        self.mname = params.get('usr_Middle_Name', '')
        self.sfx = params.get('usr_Suffix_Name', '')
        self.title = params.get('usr_Title_Name', '')
        self.state = params.get('usr_State', '')
        self.industry = params.get('usr_Industry', '')
        self.role = params.get('usr_Role', '')
        self.company = params.get('usr_Company', '')
        self.datecreated = params.get('usr_Date_Created', '')
        self.datemodified = params.get('usr_Date_Modified', '')
        self.size = params.get('usr_Company_Size', 0)
        self.index = params.get('usr_ID', 0)
        self.auth = params.get('usr_Auth_Zero', '')
        
    def insert_User(params):
        lname = action.lname
        fname = action.fname
        mname = action.mname
        sfx = action.sfx
        title = action.title
        state = action.state
        industry = action.industry
        role = action.role
        company = action.company
        datecreated = action.datecreated
        size = action.size
        auth = action.auth
        
        cursor = db.cursor()
        cursor.execute("Insert into User (usr_Last_Name, usr_First_Name, usr_Middle_Name, usr_Suffix_Name, usr_Title_Name, usr_State, usr_Industry, usr_Role, usr_Company, usr_Date_Created, usr_Company_Size, usr_Auth_Zero) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (lname, fname, mname, sfx, title, state, industry, role, company, datecreated, size, auth))
        last_id = db.insert_id()
        db.commit()
        return last_id
        
        

    def delete_User(params):
        index = action.index
        
        cursor = db.cursor()
        cursor.execute("Delete from User where usr_ID = %s", [index])
        db.commit()
        
    def update_User(params):
        lname = action.lname
        fname = action.fname
        mname = action.mname
        sfx = action.sfx
        title = action.title
        state = action.state
        industry = action.industry
        role = action.role
        company = action.company
        datecreated = action.datecreated
        size = action.size
        index = action.index
                
        cursor = db.cursor()
        cursor.execute("UPDATE User SET usr_Last_Name = %s, usr_First_Name = %s, usr_Middle_Name = %s, usr_Suffix_Name = %s, usr_Title_Name = %s, usr_State = %s, usr_Industry = %s, usr_Role = %s, usr_Company = %s, usr_Date_Modified = %s, usr_Company_Size = %s WHERE usr_ID = %s", (lname, fname, mname, sfx, title, state, industry, role, company, datecreated, size, index))
        db.commit()
        
        
    def select_User(params):
        auth = action.auth
        
        cursor = db.cursor()
        cursor.execute("Select * from User where usr_Auth_Zero = %s", [auth])
        db.commit()
        record = cursor.fetchall()
        return record
        



action = User(var_json)

if action.function == 'insert':
    id = action.insert_User()
    insertid = json.dumps(str(id))
    print(insertid)

elif action.function == 'select':
    output = action.select_User()
    data = json.dumps(output)
    print(data)
    
elif action.function == 'delete':
    action.delete_User()
    
elif action.function == 'update':
    action.update_User()
