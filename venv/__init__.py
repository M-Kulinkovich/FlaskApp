from flask import Flask
import db

app = Flask(__name__)

@app.route("/")
def test():
    db.db.users.insert_one({"name": "user"})
    return "Connected!"

if __name__ == '__main__':
    app.run(debug=True)

