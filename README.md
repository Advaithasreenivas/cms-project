## 📚 Content Management System REST API (Flask CRUD Project)

This project is a **Content Management System (CMS)** built using **Python Flask**.  
It demonstrates **CRUD operations (Create, Read, Update, Delete)** for managing content such as posts/articles and provides **analytics endpoints**.  
All APIs are tested using **Postman**.

---

## 🚀 Features

- Admin login and session-based authentication
- Create new content/posts (POST)
- View all posts (GET)
- View post by ID (GET)
- Update post details (PUT)
- Delete post by ID (DELETE)
- Analytics for published and draft content
- JSON-based request and response handling
- API testing using Postman

---

## 🛠️ Technologies Used

- Python 3
- Flask (Web Framework)
- SQLite (Database)
- Postman (API Testing)
- Chart.js (Analytics visualization)

---

## 📁 Project Structure

---

## ⚙️ Installation & Setup

### 1️⃣ Install Flask

### 2️⃣ Run the Application

The server will start at:http://127.0.0.1:5000/

---

## 🔗 API Endpoints

| Method | Endpoint              | Description                     |
|------|-----------------------|---------------------------------|
| POST | `/`                   | Admin login                     |
| GET  | `/dashboard`          | Admin dashboard                 |
| POST | `/posts`              | Add new post                    |
| GET  | `/posts`              | Get all posts                   |
| GET  | `/posts/<id>`         | Get post by ID                  |
| PUT  | `/posts/<id>`         | Update post                     |
| DELETE | `/delete/<id>`      | Delete post                     |
| GET  | `/analytics`          | View analytics data             |
| GET  | `/logout`             | Logout admin                    |

---

## 📥 Sample JSON Request

### Add Post (POST `/posts`)

```json
{
  "title": "AI in Healthcare",
  "content": "AI helps doctors detect diseases early",
  "status": "Published",
  "email": "admin@example.com",
  "phone": "7893412468"
}
🧪 Testing with Postman

Open Postman

Select HTTP method (POST / GET / PUT / DELETE)

Enter API URL, for example:
http://127.0.0.1:5000/posts
For POST or PUT:

Go to Body → raw → JSON

Paste JSON data

Click Send

Verify response status and data

⚠️ Notes

Authentication is session-based

Unauthorized access redirects to login

Analytics data is calculated from stored posts

Database file can be replaced with MySQL or MongoDB for production use

👨‍💻 Author

Advaitha sreenivas

📜 License

This project is created for educational purposes and is free to use for learning and academic demonstrations.
