class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type
        self.left = None
        self.right = None
        self.value = value

def create_rule(rule_string):
    tokens = rule_string.replace('(', '').replace(')', '').split()
    root = None
    current_node = None
    
    for token in tokens:
        if token in ['AND', 'OR']:
            operator_node = Node('operator', token)
            if root is None:
                root = operator_node
                current_node = root
            else:
                operator_node.left = current_node
                current_node = operator_node
        else:
            operand_node = Node('operand', token)
            if current_node is not None:
                current_node.right = operand_node
            else:
                current_node = operand_node
    
    return root  

def evaluate_rule(node, data):
    if node is None:
        return False  
    
    if node.type == 'operand':
        field, operator, value = node.value.split()
        value = int(value) if value.isdigit() else value.strip("'")
        return eval(f"{data[field]} {operator} {value}")

    elif node.type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)

def rule_ast_to_dict(node):
    if not node:
        return None
    return {
        "type": node.type,
        "value": node.value,
        "left": rule_ast_to_dict(node.left),
        "right": rule_ast_to_dict(node.right)
    }

def dict_to_rule_ast(node_dict):
    if not node_dict:
        return None
    node = Node(node_dict['type'], node_dict['value'])
    node.left = dict_to_rule_ast(node_dict['left'])
    node.right = dict_to_rule_ast(node_dict['right'])
    return node
