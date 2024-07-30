from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import io

app = Flask(__name__)
CORS(app)


@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        exec(code)
        sys.stdout = old_stdout
        return jsonify({"output": redirected_output.getvalue()})
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({"output": str(e)})


if __name__ == '__main__':
    app.run(port=8000)