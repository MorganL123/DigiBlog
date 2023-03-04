from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')

def index():
    users = get_all_users()
    
    return render_template('index.html', engineers = engineers)

@app.route('/success', methods = ["POST"])
def submit():
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']

    add_post(name, title, content)

    return render_template('post.html')    

def add_user(name, age, height, group):
    conn = sqlite3.connect('./static/data/DigiBlog.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO users(name, title, content) VALUES (?, ?, ?)", (name, title, content))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('./static/data/DigiBlog.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM users")
    users = []
    for row in result:
        user = {
            'name': row[0],
            'age': row[1],
            'height': row[2],
            'group': row[3]
        }
        print(user)
        users.append(user)
    conn.close()
    return users


if __name__== '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 8000)