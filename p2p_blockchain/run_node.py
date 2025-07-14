from flask import Flask, jsonify, request, render_template, redirect, url_for
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/')
def index():
    chain = blockchain.chain
    return render_template('index.html', chain=chain)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.form

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(
        values['sender'],
        values['recipient'],
        float(values['amount'])
    )

    return redirect(url_for('index'))

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])

    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    block = blockchain.new_block(proof)

    return redirect(url_for('index'))

@app.route('/chain', methods=['GET'])
def full_chain():
    chain = blockchain.chain
    return render_template('chain.html', chain=chain)


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    nodes = request.form.get('nodes').split(',')
    for node in nodes:
        blockchain.register_node(node)

    return redirect(url_for('index'))

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    return redirect(url_for('index'))

if __name__ == '__main__':
    import sys
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port, debug=True)

