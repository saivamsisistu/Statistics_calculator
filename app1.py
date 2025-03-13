from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)

class TODO(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Fix applied

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

with app.app_context():
    db.create_all()  # Ensure database is initialized

@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=TODO(title=title,description=desc)
        db.session.add(todo)
        db.session.commit()
    list = TODO.query.all()
    return render_template('index.html',allTODO=list)

@app.route("/function")
def function():
    list=TODO.query.all()
    print(list)
    return "This is a function page"

if __name__ == "__main__":
    app.run(debug=True)
