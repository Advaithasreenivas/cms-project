## 📚 Content Management System REST API (Flask CRUD Project)

This project is a simple **Content Management System (CMS) REST API** built using **Python Flask**.  
It demonstrates basic **CRUD operations (Create, Read, Update, Delete)** using HTTP methods and JSON data.  
All backend APIs are tested using **Postman**.

---

## 🚀 Features

* Admin login (POST)
* Add new posts (POST)
* Get all posts (GET)
* Get post by ID (GET)
* Update post details (PUT)
* Delete post by ID (DELETE)
* Analytics for published and draft posts
* JSON-based request and response handling

---

## 🛠️ Technologies Used

* Python 3  
* Flask (Web Framework)  
* SQLite (Database)  
* Postman (API Testing)  

---

## 📁 Project Structure
```
cms-project/
│
├── app.py # Main Flask application
├── database.db # SQLite database
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── static/ # CSS & JS files
└── templates/ # HTML templates
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/cms-project.git

cd cms-project

### 2️⃣ Install Dependencies

pip install flask

### 3️⃣ Run the Application
python app.py
Server will run at:http://127.0.0.1:5000/

---

## 🔗 API Endpoints

| Method | Endpoint          | Description            |
|------|-------------------|------------------------|
| POST | `/`               | Admin login            |
| POST | `/posts`          | Add new post           |
| GET  | `/posts`          | Get all posts          |
| GET  | `/posts/<id>`     | Get post by ID         |
| PUT  | `/posts/<id>`     | Update post            |
| DELETE | `/delete/<id>`  | Delete post            |
| GET  | `/analytics`      | View analytics         |
| GET  | `/logout`         | Logout admin           |

---

## 📥 Sample Request (POST `/posts`)

title = AI in Healthcare
content = AI helps doctors detect diseases early
status = Published
email = admin@example.com

phone = 7893412468

---

## 🧪 Testing with Postman

1. Open **Postman**
2. Select request method (POST / GET / PUT / DELETE)
3. Enter URL, for example:http://127.0.0.1:5000/posts 
4. Go to **Body → x-www-form-urlencoded**
5. Enter required fields
6. Click **Send**

---

## ⚠️ Notes

* Data is stored in **SQLite database**
* Analytics are calculated based on post status
* Designed for academic and learning purposes

---

## 👨‍💻 Author

**Advaitha Sreenivas**

---

## 📜 License

This project is for educational purposes and free to use.  





