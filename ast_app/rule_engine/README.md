README for Application 1: Rule Engine with AST

Project Overview
This project implements a Rule Engine that uses an Abstract Syntax Tree (AST) to represent, combine, and evaluate rules based on user data. The application allows for dynamic creation, combination, and evaluation of rules through a backend-only implementation.

Features
AST Creation: Parses rule strings into an AST structure.
Rule Combination: Combines multiple rules into a single AST.
Rule Evaluation: Evaluates rules against provided user data.
Test Cases: Unit tests to validate the rule engine's correctness

Project Structure
app.py: The main application file where rules are created, combined, and evaluated.
rule_engine.py: Contains the core logic for AST creation, rule combination, and rule evaluation.
tests.py: Test cases to verify the functionality of the rule engine.

Prerequisites
Python 3.8+
pip (Python package manager)

Installation and Setup
Clone the Repository:
git clone https://github.com/yourusername/rule-engine-ast.git

cd rule-engine-ast
Create a Virtual Environment (optional but recommended):
python -m venv venv
On Windows: venv\Scripts\activate

Install Dependencies (if any):
pip install -r requirements.txt
(Note: Add a requirements.txt file if you use any external libraries. If none, this step can be skipped.)

How to Run the Application
Running the Rule Engine:
python app.py
The application will evaluate rules defined in app.py based on the sample user data and return whether the user is eligible or not.

Running Test Cases: To run the test cases and verify that the rule engine works as expected:
python tests.py

Usage Example
Example Rule:

Rule: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"

Example User Data:

user_data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}

Expected Output:

Is the user eligible? True
