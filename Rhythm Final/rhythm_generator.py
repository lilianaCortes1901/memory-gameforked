from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Endpoint to generate a rhythm
@app.route('/generate_rhythm', methods=['GET'])


def generate_rhythm():
    """
    Generates an endless rhythm sequence.
    
    Returns:
        JSON response with progressively faster beats.
    """

    length = int(request.args.get('length', 4))  # Default rhythm length of 4 beats, but if supplied a length, the default is overridden. 
    rhythm = [random.uniform(0.5, 1.5) for _ in range(length)]  # Random time intervals
    return jsonify({'rhythm': rhythm})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)