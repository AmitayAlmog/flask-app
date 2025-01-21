from flask import Flask, render_template
import os
import random
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST", "localhost")  
db_user = os.getenv("DB_USER", "root")       
db_password = os.getenv("DB_PASSWORD", "")
db_name = os.getenv("DB_NAME", "gifdatabase")

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="db",
    user="user",
    password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS gifdatabase")
mydb.commit()

mydb = mysql.connector.connect(
  host="db",
  user="user",
  password="password",
  database="gifdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS visitor_count (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count INT NOT NULL DEFAULT 0
)
""")

mycursor.execute("SELECT COUNT(*) FROM visitor_count")
if mycursor.fetchone()[0] == 0:
    mycursor.execute("INSERT INTO visitor_count (count) VALUES (0)")
    mydb.commit()



mycursor.execute("SELECT COUNT(*) FROM images")
if mycursor.fetchone()[0] == 0:
    initial_gifs = [
        ("https://i.pinimg.com/originals/29/2a/50/292a50994d357e1884373ee8bf362562.gif",),
        ("https://i.pinimg.com/originals/2f/e4/67/2fe467f5a4350854f383c2185f1da571.gif",),
        ("https://media.tenor.com/iY7tFslwb0YAAAAe/ryan-gosling-confused-gif.png",),
    ]
    mycursor.executemany("INSERT INTO images (url) VALUES (%s)", initial_gifs)
    mydb.commit()


@app.route("/")
def index():
    mycursor.execute("UPDATE visitor_count SET count = count + 1 WHERE id = 1")
    mydb.commit()

    mycursor.execute("SELECT count FROM visitor_count WHERE id = 1")
    visitor_count = mycursor.fetchone()[0]

    mycursor.execute("SELECT url FROM images")
    gifs = [row[0] for row in mycursor.fetchall()]

    url = random.choice(gifs) if gifs else None
    return render_template("index.html", url=url, visitor_count=visitor_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
