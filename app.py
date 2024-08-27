# app.py
from flask import Flask, request, jsonify, render_template_string
import random
import string
from pydantic import BaseModel

app = Flask(__name__)

# HTML form template
form_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Token Generator</title>
  </head>
  <body>
    <div class="container">
      <h1>Generate Token</h1>
      <form action="/generate-token" method="post">
        <div class="form-group">
          <label for="length">Token Length:</label>
          <input type="number" id="length" name="length" required>
        </div>
        <button type="submit">Generate</button>
      </form>
      {% if token %}
      <h2>Generated Token: {{ token }}</h2>
      {% endif %}
    </div>
  </body>
</html>
'''


"""
Route decorator for the root URL.

Returns:
    str: The rendered template string.
"""
@app.route('/')
def index():
    return render_template_string(form_template)

@app.route('/generate-token', methods=['POST'])
def generate_token():
    length = int(request.form['length'])
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return render_template_string(form_template, token=token)

@app.route('/api/generate-token', methods=['GET'])
def api_generate_token():
    length = int(request.args.get('length', 8))  # Default length is 8
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return jsonify({'token': token})

    class TokenRequest(BaseModel):
        text: str

    @app.route('/api/generate-tokens', methods=['POST'])
    def api_generate_tokens():
        request_data = request.get_json()
        token_request = TokenRequest(**request_data)
        tokens = generate_tokens_from_text(token_request.text)
        return jsonify({'tokens': tokens})

    def generate_tokens_from_text(text):
        tokens = text.split()  # Split the text into individual words
        tokens = [token.upper() for token in tokens]  # Convert each word to uppercase
        return tokens

if __name__ == '__main__':
    app.run(debug=True)