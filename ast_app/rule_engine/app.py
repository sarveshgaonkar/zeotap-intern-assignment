# app.py

from rule_engine import create_rule, evaluate_rule, combine_rules

def main():
    # Define some sample rules
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "age < 25 AND department = 'Marketing'"

    # Create AST for each rule
    ast_rule1 = create_rule(rule1)
    ast_rule2 = create_rule(rule2)

    # Combine the rules with an AND operator
    combined_ast = combine_rules([rule1, rule2], operator='AND')

    # Define some sample user data
    user_data = {"age": 22, "department": "Marketing"}

    # Evaluate the combined rule against the user data
    result = evaluate_rule(combined_ast, user_data)

    # Output the result
    print("Is the user eligible?", result)

if __name__ == "__main__":
    main()
