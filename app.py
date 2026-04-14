from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # Requete corrigée
    query = "SELECT * FROM users WHERE id = ?"
    try:
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        return str(results)
    except Exception as e:
        return "Erreur serveur"
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)