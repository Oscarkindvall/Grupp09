from bottle import route, run, template, static_file, request, redirect
from os import listdir

import psycopg2

con = psycopg2.connect( 
    dbname="padel", 
    user="aj9613",
    password="g0rvfpok",
    host="pgserver.mah.se")

cur = con.cursor()

@route('/')
def index():
    cur.execute('select namn from person')
    namn = cur.fetchall()
    return template('index.html', namn=namn)



@route('/logIn')
def logIn():

    return template("log_in.html", username ="")

@route('/logInUser', method="POST")
def login():
    cred = []
    cur.execute("select username from profile")
    cred = cur.fetchall()
    username = getattr(request.forms, "userName")
    password = getattr(request.forms, "pwd")
    for name in cred:
        if username == name[0]:
            cur.execute("select password from profile where username='%s'" % (username))
            cred = cur.fetchall()
            for pwd in cred:
                if password == pwd[0]:
                    return template("welcome.html", user = username)
                else:
                    print("fel lösenord")
                    return template("log_in")
        else:
            pass
# @route('/loggedIn')
# def loggedIn(username):
#     return template("welcome.html", user = username)



# @route('/logInUser', method="POST")
# def logInUser():
#     print("hej")
#     # data regarding the profile table


#     userName = getattr(request.forms,"userName")
#     password = getattr(request.forms,"password")
#     print(userName, password)

   

#     def selectMember():
#         # userSelect = []
#         # userSelect.append(userName)
#         # userSelect.append(password)
        
#         sql = "select * from profile where username = %s AND profile.password = %s"
#         val = userName,password
#         cur.execute(sql, val)
        

    # selectMember()
    
    




run(host='localhost', port=8080, debug=True)
con.close()

