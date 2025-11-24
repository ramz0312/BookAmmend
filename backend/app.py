# backend/app.py - BookAmmend API Entry Point (Flask)
from flask import Flask, jsonify, request
# from backend import database # To be implemented later
app = Flask(__name__)
# Route to serve the main HTML page
@app.route('/')
def index():
    # In a real app, this would render a template like 'index.html'
    return "BookAmmend Backend Running. Frontend templates will be served here."
# API Endpoint for recommendations
@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # genre = request.args.get('genre', 'fiction') # Get query parameter
    # books = database.fetch_books_by_genre(genre) # Placeholder for DB query
    # Placeholder Data
    recommended_books = [
        {"id": 1, "title": "The Price of Salt", "author": "Patricia Highsmith", "genre": "Thriller"},
        {"id": 2, "title": "The Road", "author": "Cormac McCarthy", "genre": "Post-Apocalyptic"}
    ]
    
    return jsonify({"success": True, "books": recommended_books})

if __name__ == '__main__':
    app.run(debug=True)
