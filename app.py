from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB = "tasks.db"


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)


@app.get("/")
def home():
    return jsonify({"message": "Python Task Manager API"})


@app.get("/tasks")
def get_tasks():
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()

    return jsonify([dict(row) for row in rows])

@app.post("/tasks")
def add_task():
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    with sqlite3.connect(DB) as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            (title, 0)
        )
        task_id = cursor.lastrowid

    return jsonify({
        "id": task_id,
        "title": title,
        "completed": 0
    }), 201
        


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

    if cursor.rowcount == 0:
        return jsonify({"error": "task not found"}), 404

    return jsonify({"message": "task deleted"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)