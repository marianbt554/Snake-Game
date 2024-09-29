from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store high scores (in-memory for now)
high_scores = []

@app.route('/')
def home():
    return render_template('snake.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    username = data.get('username', 'Anonymous')
    score = data.get('score', 0)

    high_scores.append({'username': username, 'score': score})
    high_scores.sort(key=lambda x: x['score'], reverse=True)

    return jsonify(high_scores[:5])  # Return top 5 scores

if __name__ == "__main__":
    app.run(debug=True)
