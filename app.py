from flask import Flask, render_template, request, redirect, session
import sqlite3, datetime

app = Flask(__name__)
app.secret_key = "apple-ultra-secret"

# ---------- DATABASE ----------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

with get_db() as db:
    db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    db.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        email TEXT,
        phone TEXT,
        status TEXT,
        created_at TEXT
    )
    """)
    db.commit()

# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")

        user = get_db().execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u, p)
        ).fetchone()

        if user:
            session["user"] = u
            return redirect("/dashboard")

    return render_template("login.html")

# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        db = get_db()
        db.execute("INSERT INTO users (username,password) VALUES (?,?)", (u, p))
        db.commit()
        return redirect("/")

    return render_template("register.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    total = db.execute("SELECT COUNT(*) FROM posts").fetchone()[0]
    published = db.execute(
        "SELECT COUNT(*) FROM posts WHERE status='Published'"
    ).fetchone()[0]
    draft = total - published

    return render_template(
        "dashboard.html",
        total=total,
        published=published,
        draft=draft
    )

# ---------- POSTS ----------
@app.route("/posts", methods=["GET", "POST"])
def posts():
    if "user" not in session:
        return redirect("/")

    db = get_db()

    if request.method == "POST":
        db.execute("""
        INSERT INTO posts (title,content,email,phone,status,created_at)
        VALUES (?,?,?,?,?,?)
        """, (
            request.form["title"],
            request.form["content"],
            request.form["email"],
            request.form["phone"],
            request.form["status"],
            datetime.datetime.now().strftime("%d %b %Y %H:%M")
        ))
        db.commit()

    posts = db.execute("SELECT * FROM posts ORDER BY id DESC").fetchall()
    return render_template("posts.html", posts=posts)

# ---------- EDIT ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect("/")

    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id=?", (id,)).fetchone()

    if request.method == "POST":
        db.execute("""
        UPDATE posts
        SET title=?, content=?, email=?, phone=?, status=?
        WHERE id=?
        """, (
            request.form["title"],
            request.form["content"],
            request.form["email"],
            request.form["phone"],
            request.form["status"],
            id
        ))
        db.commit()
        return redirect("/posts")

    return render_template("edit.html", post=post)

# ---------- DELETE ----------
@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect("/")

    db = get_db()
    db.execute("DELETE FROM posts WHERE id=?", (id,))
    db.commit()
    return redirect("/posts")

# ---------- ANALYTICS ----------
@app.route("/analytics")
def analytics():
    if "user" not in session:
        return redirect("/")

    db = get_db()
    published = db.execute(
        "SELECT COUNT(*) FROM posts WHERE status='Published'"
    ).fetchone()[0]
    draft = db.execute(
        "SELECT COUNT(*) FROM posts WHERE status='Draft'"
    ).fetchone()[0]

    return render_template("analytics.html", published=published, draft=draft)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)