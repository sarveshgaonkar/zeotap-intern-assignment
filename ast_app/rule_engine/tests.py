# tests.py
from rule_engine import create_rule, evaluate_rule, combine_rules

def test_single_rule():
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    user_data = {"age": 35, "department": "Sales"}
    assert evaluate_rule(ast, user_data) == True

def test_combined_rule():
    rule1 = "age > 30"
    rule2 = "department = 'Marketing'"
    ast = combine_rules([rule1, rule2], operator='AND')
    user_data = {"age": 35, "department": "Marketing"}
    assert evaluate_rule(ast, user_data) == True

if __name__ == "__main__":
    test_single_rule()
    test_combined_rule()
    print("All tests passed.")
