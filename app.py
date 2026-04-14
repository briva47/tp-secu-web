from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    # Vulnérabilité
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return str(results)
    except Exception as e:
        return "Erreur serveur"
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)