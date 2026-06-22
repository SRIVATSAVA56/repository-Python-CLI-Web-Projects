import sqlite3
from flask import Flask, request, redirect, url_for, session, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'highly_optimized_secret_key'  # Required for secure session handling
DB_FILE = 'database.db'

# ==========================================
# 1. DATABASE INITIALIZATION (O(1) Space)
# ==========================================
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        # Create Users and Tasks tables if they don't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT, done INTEGER DEFAULT 0)''')
        conn.commit()

init_db()

# ==========================================
# 2. EMBEDDED HTML/CSS (Responsive UI)
# ==========================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7f6; display: flex; justify-content: center; padding: 20px; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
        h2 { text-align: center; color: #333; }
        input[type="text"], input[type="password"] { width: 95%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #218838; }
        .task { display: flex; justify-content: space-between; align-items: center; padding: 10px; border-bottom: 1px solid #eee; }
        .task.done { text-decoration: line-through; color: #888; }
        .btn-small { width: auto; padding: 5px 10px; font-size: 12px; margin-left: 5px; }
        .btn-danger { background: #dc3545; } .btn-danger:hover { background: #c82333; }
        .error { color: red; text-align: center; font-size: 14px; }
        .toggle-link { text-decoration: none; color: inherit; flex-grow: 1; }
    </style>
</head>
<body>
    <div class="container">
        {% if error %}<p class="error">{{ error }}</p>{% endif %}
        
        {% if not session.get('user_id') %}
            <h2>Login / Register</h2>
            <form method="POST" action="/auth">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" name="action" value="login">Login</button>
                <button type="submit" name="action" value="register" style="background: #007bff; margin-top: 10px;">Register</button>
            </form>
        {% else %}
            <h2>My Tasks</h2>
            <form method="POST" action="/add" style="display: flex; gap: 10px; margin-bottom: 20px;">
                <input type="text" name="title" placeholder="New Task..." required style="margin: 0;">
                <button type="submit" style="width: 80px;">Add</button>
            </form>
            
            <div id="tasks">
                {% for task in tasks %}
                <div class="task {% if task[3] %}done{% endif %}">
                    <a href="/toggle/{{ task[0] }}" class="toggle-link">{{ task[2] }}</a>
                    <form method="POST" action="/delete/{{ task[0] }}" style="margin: 0;">
                        <button type="submit" class="btn-small btn-danger">X</button>
                    </form>
                </div>
                {% else %}
                <p style="text-align: center; color: #888;">No tasks yet. Add one above!</p>
                {% endfor %}
            </div>
            <br>
            <form method="POST" action="/logout"><button class="btn-small" style="background: #6c757d;">Logout</button></form>
        {% endif %}
    </div>
</body>
</html>
"""

# ==========================================
# 3. ROUTING & CORE LOGIC
# ==========================================
@app.route('/')
def index():
    error = request.args.get('error')
    tasks = []
    # If user is logged in, fetch their specific tasks in O(log N) time
    if 'user_id' in session:
        with sqlite3.connect(DB_FILE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM tasks WHERE user_id = ? ORDER BY id DESC', (session['user_id'],))
            tasks = c.fetchall()
            
    return render_template_string(HTML_TEMPLATE, tasks=tasks, error=error)

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']
    action = request.form['action']
    
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        if action == 'register':
            try:
                c.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                          (username, generate_password_hash(password)))
                conn.commit()
                # Auto-login after registration
                c.execute('SELECT id FROM users WHERE username = ?', (username,))
                session['user_id'] = c.fetchone()[0]
                return redirect(url_for('index'))
            except sqlite3.IntegrityError:
                return redirect(url_for('index', error="Username already exists!"))
                
        elif action == 'login':
            c.execute('SELECT id, password FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            if user and check_password_hash(user[1], password):
                session['user_id'] = user[0]
                return redirect(url_for('index'))
            return redirect(url_for('index', error="Invalid username or password."))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_task():
    if 'user_id' in session:
        title = request.form['title']
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('INSERT INTO tasks (user_id, title) VALUES (?, ?)', (session['user_id'], title))
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 'user_id' in session:
        with sqlite3.connect(DB_FILE) as conn:
            # Flips the boolean state using mathematical absolute value (1 -> 0, 0 -> 1)
            conn.execute('UPDATE tasks SET done = ABS(done - 1) WHERE id = ? AND user_id = ?', (task_id, session['user_id']))
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' in session:
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, session['user_id']))
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Runs the application on a local development server
    app.run(debug=True)