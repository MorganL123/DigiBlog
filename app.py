from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')

def index():
    
    return render_template('index.html')
    

@app.route('/success', methods = ["POST"])
def submit():
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']
    add_user_info(name, title, content)
    users = get_all_users()
    return render_template('index.html', users = users)

def add_user_info(name, title, content):
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO users(name, title, content) VALUES (?, ?, ?)", (name, title, content))
    conn.commit()
    conn.close()



def get_all_users():
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM users")
    users = []

    for row in result:
        user = {
            'rowid': row[0],
            'name': row[1],
            'title': row[2],
            'content': row[3],
        }
        print(user)
        users.append(user)
    conn.close()
    return users


if __name__== '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 3000)