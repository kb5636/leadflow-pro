from flask import Flask, render_template, request, redirect
import sqlite3, os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def dashboard():
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('SELECT * FROM leads')
    leads = c.fetchall()
    conn.close()
    return render_template('dashboard.html', leads=leads)

@app.route('/add-lead', methods=['POST'])
def add_lead():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('INSERT INTO leads (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    @app.route('/delete-lead/<int:lead_id>', methods=['POST'])
@app.route('/delete-lead/<int:lead_id>', methods=['POST'])
def delete_lead(lead_id):
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('DELETE FROM leads WHERE id = ?', (lead_id,))
    conn.commit()
    conn.close()
    return redirect('/')

