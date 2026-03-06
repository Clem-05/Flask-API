from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulation d'une table en base de données
users_list = [
    {"id": 1, "name": "Clemence", "role": "Etudiante"},
    {"id": 2, "name": "Prof", "role": "Enseignant"}
]

# 1. Route simple (GET) - Page d'accueil
@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur l'API EFREI"})

# 3. Route GET - Accéder à une donnée (un utilisateur par son ID)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users_list if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Non trouve"}), 404

# 5. Route POST - Créer une donnée
@app.route('/users', methods=['POST'])
def create_user():
    new_data = request.get_json()
    new_user = {
        "id": len(users_list) + 1,
        "name": new_data.get("name"),
        "role": new_data.get("role")
    }
    users_list.append(new_user)
    return jsonify(new_user), 201

# 6. Route PUT - Modifier une donnée
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users_list if u["id"] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user), 200
    return jsonify({"error": "Non trouve"}), 404

# 7. Route DELETE - Supprimer une donnée
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users_list
    users_list = [u for u in users_list if u["id"] != user_id]
    return jsonify({"message": "Utilisateur supprime"}), 200

if __name__ == '__main__':
    app.run(debug=True)
