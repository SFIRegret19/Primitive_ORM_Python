import sqlite3
# import texts
# from config import priceSu, priceB, priceP, priceSh
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age TEXT NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

# initiate_db()
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Пицца', f'{texts.Pizza_text}', f'{priceP}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Суши', f'{texts.Sushi_text}', f'{priceSu}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Бургер', f'{texts.Burger_text}', f'{priceB}'))
# cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Шаурма', f'{texts.Shaurma_text}', f'{priceSh}'))

def add_user(username, email, age):
    initiate_db()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    connection.commit()

def is_included(username):
    initiate_db()
    return cursor.execute("SELECT username FROM Users WHERE username = ?", (username, )).fetchone() is not None


def get_all_products():
    initiate_db()
    cursor.execute(" CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")
    cursor.execute("SELECT title, description, price FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    return all_products

if __name__ == "__main__":
    connection.commit()
    connection.close()