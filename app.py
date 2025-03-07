from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAchemy

app=Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAchemy(app)

class Todo (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created= db.Column(db.)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


