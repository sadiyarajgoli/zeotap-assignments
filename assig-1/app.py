from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from rules import create_rule, evaluate_rule, rule_ast_to_dict, dict_to_rule_ast

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['rule_engine_db']

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_data = request.get_json()
    rule_string = rule_data['rule_string']
    rule_ast = create_rule(rule_string)
    
    db.rules.insert_one({
        "rule_string": rule_string,
        "ast": rule_ast_to_dict(rule_ast)
    })
    
    return jsonify({"message": "Rule created successfully!"}), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    evaluation_data = request.get_json()
    rule_id = evaluation_data['rule_id']
    user_data = evaluation_data['data']
    
    rule = db.rules.find_one({"_id": ObjectId(rule_id)})
    if not rule:
        return jsonify({"error": "Rule not found"}), 404
    
    rule_ast = dict_to_rule_ast(rule['ast'])
    result = evaluate_rule(rule_ast, user_data)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
