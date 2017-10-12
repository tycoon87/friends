#from flask import Flask, render_template
#
#from mysqlconnection import MySQLConnector
#app = Flask(__name__)
#
#mysql = MySQLConnector(app, 'friendsdb')
#
#print mysql.query_db("SELECT * FROM friends")
#
#@app.route('/')
#def index():
#    friends = mysql.query_db("SELECT * FROM friends")
#    print friends
#    return render_template('friends.html')
#
#@app.route('/friends/<friend_id>')
#def show(friend_id):
#    query = "SELECT * FROM friends WHERE id = :specific_id"
#    data = {'specific_id': friend_id}
#    friends = mysql.query_db(query, data)
#    return render_template('index.html', one_friend=friends[0])
#
#@app.route('/friends', methods=['POST'])
#def create():
#    print request.form['first_name']
#    print request.form['last_name']
#    print request.form['occupation']
#    return redirect('/')
#
#app.run(debug=True)

#************************************************

from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('friends.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    print query
    mysql.query_db(query)
    return redirect('/')

app.run(debug=True)