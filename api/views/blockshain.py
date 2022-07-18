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
    return jsonify({"length": len(chain_data),
                       "chain": chain_data})

@api_views.route('/new_add', methods=['POST'])
def add_block():
    block_data = request.get_json

    block = Block(**block_data)
    new_block = blockchain.add_block(block=block)
    return make_response(jsonify(new_block), 200)


