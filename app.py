from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Read connection string from environment variables in Azure App Service
MYSQL_HOST = os.getenv("MYSQL_HOST")      # VM private IP (e.g., 10.0.0.4)
MYSQL_USER = os.getenv("MYSQL_USER")      # appuser
MYSQL_PASS = os.getenv("MYSQL_PASS")      # password
MYSQL_DB   = os.getenv("MYSQL_DB")        # myapp

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASS,
            database=MYSQL_DB
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        return {"courses": rows}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
