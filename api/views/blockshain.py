from http.server import BaseHTTPRequestHandler
from api.views import api_views
from flask import jsonify, Flask, request, make_response
from chain import Blockchain, Block

app = Flask(__name__)

blockchain = Blockchain()


@api_views.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return make_response(jsonify({"length": len(chain_data),
                       "chain": chain_data}), 200)

@api_views.route('/mine', methods=['GET'])
def mine():
    # perform mine operation
    id = blockchain.mine()
    return make_response(jsonify({
        "index": id
    }), 201)


