# 📚 Flask CRUD Web Application with MongoDB

This is a simple **CRUD (Create, Read, Update, Delete)** web application built using **Flask** (Python Framework) and **MongoDB** as the database.  
It allows users to add, view, edit, and delete **student records** via a beautiful Bootstrap UI with modals for Add/Edit.

---

## 🚀 Features
- Add new student data
- Edit existing student information using modal popup
- Delete student records with confirmation
- Display all student records in a table
- Bootstrap 5 styling for a modern look
- MongoDB database integration

---

## 🛠️ Technology Stack
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript (jQuery)
- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Others**: Flask-PyMongo

---

## 📂 Project Structure

```
Flask_CRUD/
|
|├— app.py                  # Main Flask application
|├— templates/
|    └— index.html          # Main HTML page
|├— static/
|    |
|    ├— css/
|    |   └— bootstrap.min.css
|    |
|    ├— js/
|    |   ├— bootstrap.bundle.min.js
|    |   └— jquery-3.7.1.min.js
|├— requirements.txt        # Python dependencies
|└— README.md                # (this file)
```

---

## 📦 Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Flask_CRUD.git
   cd Flask_CRUD
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   # OR
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure MongoDB is running locally**
   - Default connection string assumed: `mongodb://localhost:27017/`
   - Database: `school`
   - Collection: `students`

5. **Run the Flask app**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 👉 Important Endpoints

| Route | Method | Description |
|:------|:-------|:------------|
| `/` | GET | Display all students |
| `/addStudent` | POST | Add a new student |
| `/editStudent` | POST | Edit an existing student |
| `/deleteStudent/<rollno>` | GET | Delete a student by Roll No |

---

## 💃 Sample `requirements.txt`
```txt
Flask
Flask-PyMongo
```

---

## ✨ Future Improvements
- Add validation (front-end + back-end)
- Add search/filter functionality
- Deploy on cloud (Heroku, Render, etc.)
- Use AJAX for smooth form submit without refresh

---

## 👨‍💼 Author

- **Santhosh**  
- GitHub: [github.com/Santhosh1015](https://github.com/Santhosh1015)

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it!

---

# 🎯 Quick Start

```bash
git clone https://github.com/your-username/Flask_CRUD.git
cd Flask_CRUD
pip install -r requirements.txt
python app.py
```
# 🎯 Output Screen
![HomePage]()

And your project will be live at `http://127.0.0.1:5000/` 🚀

