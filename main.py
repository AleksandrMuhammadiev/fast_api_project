import sqlite3


def get_user(pk):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (pk, ))
    user = cursor.fetchone()
    lst = ['id', 'name', 'username', 'email', 'phone', 'address']
    dict_user = {lst[i]: user[i] for i in range(len(lst))}
    return dict_user


def all_user():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM users 
    ''', )
    users = cursor.fetchall()
    lst = ['id', 'name', 'username', 'email', 'phone', 'address']
    dict_user = [{lst[i]: user[i] for i in range(len(lst))} for user in users]
    return dict_user


def save_user(user):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO users(name, username, email, phone, address) 
        VALUES (?, ?, ?, ?, ?)
    ''', user)
    db.commit()
    db.close()
