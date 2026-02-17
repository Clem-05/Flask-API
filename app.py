from flask import Flask, jsonify

app = Flask(__name__)

# Route 1 : Page d'accueil
@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue sur mon API!",
        "status": "success"
    })

# Route 2 : Informations sur l'utilisateur
@app.route('/user')
def get_user():
    return jsonify({
        "id": 1,
        "name": "Clemence",
        "role": "Etudiante EFREI",
        "skills": ["Python", "OOP", "Flask"]
    })

if __name__ == '__main__':
    app.run(debug=True)
