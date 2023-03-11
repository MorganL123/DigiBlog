from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')

def index():
    users = get_all_users()
    return render_template('index.html', users = users)

@app.route('/edit/<rowid>')
def edit(rowid):
    users = get_user(rowid)
    return render_template('edit.html', user = users)

@app.route('/edit-user/<rowid>', methods=['POST'])
def edit_user(rowid):
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']
    update_user(name, title, content, rowid)

    return redirect(url_for('index'))
    
@app.route('/delete-user/<rowid>')
def delete(rowid):
    delete_user(rowid)
    return redirect(url_for('index'))

@app.route('/success', methods = ["POST"])
def submit():
    name = request.form['name']
    title = request.form['title']
    content = request.form['content']
    add_user(name, title, content)
    users = get_all_users()
    return render_template('index.html', users = users)

def add_user(name, title, content):
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO users(name, title, content) VALUES (?, ?, ?)", (name, title, content))
    conn.commit()
    conn.close()

def update_user(name, title, content, rowid):
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    curs.execute("UPDATE users SET name  = ?, title = ?, content =  ? WHERE rowid = ?", (name, title, content, rowid))
    conn.commit()
    conn.close()

def delete_user(rowid):
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM users WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def get_user(rowid):
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM users WHERE rowid = ?", (rowid,))

    for row in result:
        user = {
            'rowid': row[0],
            'name': row[1],
            'title': row[2],
            'content': row[3],
        }
        print(user)
    conn.close()
    return user

def get_all_users():
    conn = sqlite3.connect('./static/data/digiblog.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM users")
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
    app.run(debug=True, host ='0.0.0.0', port = 2000)