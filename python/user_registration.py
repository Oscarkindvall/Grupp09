from flask import Flask, render_template, request, redirect
import hashlib, binascii, os
from db_operations import insert, fetchall

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def register():
    """
    Receives User resitration information from a form and creates Person & Profile in the database.
    """
    level = request.form["level"]

    förnamn = request.form["fNamn"]
    efternamn = request.form["eNamn"]
    email = request.form["email"]
    gender = request.form["gender"]

    userName = request.form["userName"]
    password = request.form["pwd"]
    password = hash_password(password)

    level = request.form["level"]
    ort = request.form["ort"]



    # if user name doesn't already exists
    usernameList = fetchall("select username from registration", "")
    usernameList = ("".join(str(usernameList)))

    if userName not in usernameList:

        def insertPerson():
            sql = "insert into person(name, email, gender) values(%s,%s,%s)"
            namn = förnamn + " " + efternamn
            val = (namn, email, gender,)
            insert(sql,val)

        def insertRegistration():
            sql = "insert into registration(username, password) values(%s,%s)"
            val = (userName, password,)
            insert(sql,val)

        def insert_Profile():
            sql = "insert into profile(img, level, ort) values(%s, %s, %s)"
            image = '/static/blank_profile.png'
            val = (image, level, ort,)
            insert(sql,val)

        insert_Person()
        insert_Profile()
        insert_Registration()
        return True
    else:
        return False
