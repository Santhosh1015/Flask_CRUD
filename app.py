from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://san_Santhosh:San_amx3hmmm@cluster0.maj8a.mongodb.net/flask_DB?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/addStudent', methods=['POST'])
def addStudent():
    try:
        rollno = request.form['rollno'] 
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        if not rollno or not name or not email or not mobile:
            return "All fields are required", 400
        
        mongo.db.students.insert_one({
            'rollno': rollno,
            'name': name,
            'email': email,
            'mobile': mobile
        })

        return redirect(url_for('home'))

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/editStudent', methods=['POST'])
def editStudent():
    original_rollno = request.form['original_rollno']
    rollno = request.form['rollno']
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']

    mongo.db.students.update_one(
        {'rollno': original_rollno},
        {'$set': {
            'rollno': rollno,
            'name': name,
            'email': email,
            'mobile': mobile
        }}
    )

    return redirect(url_for('home'))
@app.route('/deleteStudent/<rollno>')
def deleteStudent(rollno):
    mongo.db.students.delete_one({'rollno':rollno})
    return redirect(url_for('home'))
@app.route('/')
def home():
    students = mongo.db.students.find()
    return render_template("index.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)
