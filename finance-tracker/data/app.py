from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('finance_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

#receives all transactions + add new transactions
@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    conn = get_db_connection()
    if request.method == 'GET':
        transactions = conn.execute('SELECT * FROM transactions').fetchall()
        return jsonify([dict(ix) for ix in transactions]), 200

    if request.method == 'POST':
        new_trans = request.json
        conn.execute('INSERT INTO transactions (category_id, amount, description, transaction_date) VALUES (?, ?, ?, ?)',
                     (new_trans['category_id'], new_trans['amount'], new_trans['description'], new_trans['transaction_date']))
        conn.commit()
        return {"message": "Transaction created successfully"}, 201

#receives specific transaction + update transaction + delete transaction by id
@app.route('/transactions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def transaction(id):
    conn = get_db_connection()
    transaction = conn.execute('SELECT * FROM transactions WHERE id = ?', (id,)).fetchone()

    if not transaction:
        return {"error": "Transaction not found"}, 404

    if request.method == 'GET':
        return jsonify(dict(transaction)), 200

    elif request.method == 'PUT':
        updates = request.json
        conn.execute('UPDATE transactions SET category_id = ?, amount = ?, description = ?, transaction_date = ? WHERE id = ?',
                     (updates['category_id'], updates['amount'], updates['description'], updates['transaction_date'], id))
        conn.commit()
        return {"message": "Transaction updated successfully"}, 200

    elif request.method == 'DELETE':
        conn.execute('DELETE FROM transactions WHERE id = ?', (id,))
        conn.commit()
        return {"message": "Transaction deleted successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)