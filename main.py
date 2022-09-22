from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__, template_folder='template')
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'
 
mysql = MySQL(app)
@app.route('/')
def main():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "login"
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO accounts(username, email, password) VALUES(%s, %s, %s)''', (name, email, password))
        mysql.connection.commit()
        cursor.close()
        return render_template('home.html')
if __name__ == '__main__':
   app.run(debug = False)
