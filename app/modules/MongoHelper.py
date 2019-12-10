
'''
Helper file for all Mongo queries
'''

# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import urllib
import json
import datetime
import string, random, hashlib

# Custom packages
import pymongo
from ..modules import Credential as Credential


#connect to local MongoDB
def init_Mongo():
    uname = Credential.getMongoID()
    password = Credential.getMongoPass()
    connectionString = "mongodb+srv://{}:{}@clubswipecluster-raujd.gcp.mongodb.net/test".format(uname, password)
    print("Trying to connect to: "+connectionString)
    mongo = pymongo.MongoClient(connectionString)
    db = mongo["clubswipe"]
    usercol = db["userdata"]
    clubcol = db["clubdata"]
    return (db, usercol, clubcol)

#remove user from database (only for unit testing purposes)
def DB_remove_user(col, email):
    cursor = col.find({'email': email})
    for x in cursor:
        print("removing email")
        col.delete_one({"email": email})
        break

#login user to database
def DB_login_user(db, col, email, password, statusCode):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    result = 0
    cursor = col.find({'email': email})

    id_save = 00000

    statusCode = "2" #email doesnt exist
    for x in cursor:
        # print("iterating through cursor")
        if x:
            id_save = x['id']
            y = x['password']
            emailList = [x['email']]
            if password == y:
                statusCode = "0" # success
                result = 1
                userVect= x['vector']
            else:
                statusCode = "1"# wrong pass
        break

    resultJson = jsonify({"valid" : result, "status":statusCode, 'id':id_save, "vector":userVect})

    return resultJson

#register user to database
def DB_register_user(db, usercol, id, email, password, vector , statusCode):
    result = 0
    statusCode = "0"
    #Connect to DB and insert, and then change the values of result and status code accordingly

    # Status code == 1 implies that an id with that email already exists
    print(email)
    cursor = col.find({'email': email})
    for x in cursor:
        print("iterating through cursor")
        if x:
            print("register user failed or exists")
            statusCode = "1"
            resultJson = jsonify({"valid" : result, "status" : statusCode})
            return resultJson

    result = 1
    #emailList = [email]
    col.insert_one({'email': email, 'password': password, 'id': id, 'vector': vector})
    print("user inserted into database")
    #test sendgrind
    #Communications.send_email(key, emailList, 'Successful Registration', 'Thank you for signing up to HousingAlertNYC!')

    resultJson = jsonify({"valid" : result, "status" : statusCode})
    return resultJson

def DB_insert_club(db, col, club_dict):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    col.insert_one(club_dict)
    return True

def DB_fetch_clubs(db, col, parameter={}):
    cursor = col.find(parameter)
    result = []
    for document in cursor:
        result.append(document)
    return result
