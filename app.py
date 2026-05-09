from datetime import datetime
import sqlite3
from pathlib import Path

from flask import Flask, flash, g, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "tasks.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-me"


def get_db():
    """Open a SQLite connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error=None):
    """Close the SQLite connection at the end of the request."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create the tasks table if it does not already exist."""
    with sqlite3.connect(DATABASE) as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        db.commit()


def list_tasks():
    """Return all tasks, newest first."""
    db = get_db()
    return db.execute(
        "SELECT id, title, description, created_at FROM tasks ORDER BY id DESC"
    ).fetchall()


def create_task(title, description):
    """Insert a new task into the database."""
    db = get_db()
    db.execute(
        "INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)",
        (title, description, datetime.now().strftime("%Y-%m-%d %H:%M")),
    )
    db.commit()


@app.route("/", methods=["GET", "POST"])
def home():
    """Homepage: show existing tasks and handle basic task creation."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()

        if not title:
            flash("Task title is required.", "error")
        else:
            create_task(title, description)
            flash("Task created successfully.", "success")
            return redirect(url_for("home"))

    tasks = list_tasks()
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
