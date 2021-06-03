from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# well, shake_128 and 256 have dynamic length. I've set it to 256 arbitrarly, feel free to change

@app.route('/api/digest', methods=['POST'])
def postdigest():
    content=request.form.get('content').encode('utf-8')
    answer = {}
    for algo in hashlib.algorithms_guaranteed:
        if algo.startswith('shake_'):
            answer[algo] = getattr(hashlib, algo)(content).hexdigest(256)
        else:
            answer[algo] = getattr(hashlib, algo)(content).hexdigest()
    return jsonify(answer)

@app.route('/api/digest/<algo>/<content>')
def getdigest(algo, content):
    answer = {}
    if algo.startswith('shake_'):
        answer[algo] = getattr(hashlib, algo)(content.encode('utf-8')).hexdigest(256)
    else:
        answer[algo] = getattr(hashlib, algo)(content.encode('utf-8')).hexdigest()
    return jsonify(answer)