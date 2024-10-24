# rule_engine.py

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left  # left child for binary operators like AND, OR
        self.right = right  # right child for binary operators
        self.value = value  # value for operand nodes (e.g., a condition like 'age > 30')

    def __repr__(self):
        return f"Node(type={self.node_type}, left={self.left}, right={self.right}, value={self.value})"


import re

def create_rule(rule_string):
    # Tokenize the rule string by splitting on AND/OR
    tokens = re.split(r'\s+(AND|OR)\s+', rule_string)
    root = None

    for token in tokens:
        token = token.strip()
        if token in ["AND", "OR"]:
            # Create an operator node (set root.left = previous root, root.right to be filled later)
            root = Node(node_type='operator', left=root, value=token)
        else:
            # Create operand node for the condition (e.g., 'age > 30')
            operand_node = Node(node_type='operand', value=token)
            if root is None:
                root = operand_node  # First operand becomes the root if no operators yet
            else:
                root.right = operand_node  # Right child of the operator node
    
    return root


def evaluate_rule(node, data):
    if node.node_type == 'operand':
        # Extract the operand condition (e.g., "age > 30" or "department = 'Sales'")
        condition = node.value
        for key, value in data.items():
            # Add quotes around strings for proper comparison
            if isinstance(value, str):
                condition = condition.replace(key, f"'{value}'")
            else:
                condition = condition.replace(key, str(value))

        # Ensure the comparison operator is correct (replace = with == for conditions)
        condition = condition.replace("=", "==")

        return bool(eval(condition))  # Ensure return value is always boolean

    elif node.node_type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)


def combine_rules(rules, operator='AND'):
    combined_root = None
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_root is None:
            combined_root = rule_ast  # First rule sets the initial AST
        else:
            # Combine with an operator (AND/OR) node
            combined_root = Node(node_type='operator', left=combined_root, right=rule_ast, value=operator)
    return combined_root
