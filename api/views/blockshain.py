from api.views import api_views
from flask import jsonify, Flask, request, make_response
from chain import Blockchain, block

app = Flask(__name__)

blockchain = Blockchain()


@api_views.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({"length": len(chain_data),
                       "chain": chain_data})

@api_views.route('/new_add', method=['POST'])
def add_block():
    data = request.get_json
    new_block = blockchain.add_block()
    return make_response(jsonify(new_block), 200)


