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
        ("https://tenor.com/view/ryan-gosling-ryan-gosling-drive-flip-gif-5480671772097000575",),
        ("https://tenor.com/view/gosling-blade-runner-gosling-angry-gosling-pokerface-pokerface-gif-3757061166121710535",),
        ("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWQ3bWZwbWJpZ3VrcmNrM3g0eTRvaWNtZjJrcmswZ3lhMTA3dGwxYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aoTKz5O4dE27S/giphy.gif",),
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
