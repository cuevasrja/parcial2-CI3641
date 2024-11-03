from typing import List

def is_operator(c: str) -> bool:
    """
    ### Description
    Check if a character is an operator.
    
    ### Arguments
    - c: character to be checked.

    ### Returns
    True if the character is an operator, False otherwise.
    """
    return c in {'+', '-', '*', '/'}

def needs_parentheses(op1: str, op2: str, pos: int) -> bool:
    """
    ### Description
    Check if an operator needs parentheses to be shown in an expression.

    ### Arguments
    - op1: first operator.
    - op2: second operator.
    - pos: position of the second operator in the expression.

    ### Returns
    True if the second operator needs parentheses, False otherwise.
    """
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return operator_precedence[op1] < operator_precedence[op2] if pos == 0 else operator_precedence[op1] <= operator_precedence[op2]

def pre_show(expression: List[str]) -> str|None:
    """
    ### Description
    Show an expression in infix notation.

    ### Arguments
    - expression: list of tokens in prefix notation.

    ### Returns
    - str: The expression in infix notation if it is valid.
    - None: If the expression is invalid.
    """
    stack = []

    # Traverse the expression in reverse order
    for token in reversed(expression):
        # If the token is an operator
        if is_operator(token):
            # If there are less than 2 elements in the stack, the expression is invalid
            if len(stack) < 2:
                return None
            # Pop the first and second operands and their respective operators
            first_operand, first_operator = stack.pop()
            second_operand, second_operator = stack.pop()

            # If the first operand needs parentheses, add them
            if first_operator and needs_parentheses(first_operator, token, 0):
                first_operand = f"({first_operand})"
            # If the second operand needs parentheses, add them
            if second_operator and needs_parentheses(second_operator, token, 1):
                second_operand = f"({second_operand})"

            # Add the new expression to the stack
            stack.append((f"{first_operand} {token} {second_operand}", token))
        # If the token is an operand
        else:
            # Add the operand to the stack
            stack.append((token, ""))

    # If the stack has more than one element, the expression is invalid because it has more than one root
    if len(stack) != 1:
        return None

    # Return the expression in infix notation
    return stack[-1][0]

def post_show(expression: List[str]) -> str|None:
    """
    ### Description
    Show an expression in infix notation.

    ### Arguments
    - expression: list of tokens in postfix notation.

    ### Returns
    - str: The expression in infix notation if it is valid.
    - None: If the expression is invalid.
    """
    stack = []

    # For each token in the expression
    for token in expression:
        # If the token is an operator
        if is_operator(token):
            # If there are less than 2 elements in the stack, the expression is invalid
            if len(stack) < 2:
                return None
            # Pop the first and second operands and their respective operators
            second_operand, second_operator = stack.pop()
            first_operand, first_operator = stack.pop()

            # If the first operand needs parentheses, add them
            if first_operator and needs_parentheses(first_operator, token, 0):
                first_operand = f"({first_operand})"
            if second_operator and needs_parentheses(second_operator, token, 1):
                second_operand = f"({second_operand})"

            # Add the new expression to the stack
            stack.append((f"{first_operand} {token} {second_operand}", token))
        else:
            stack.append((token, ""))

    # If the stack has more than one element, the expression is invalid because it has more than one root
    if len(stack) != 1:
        return None

    # Return the expression in infix notation
    return stack[-1][0]
        

def show(order: str, expression: str) -> None|str:
    """
    ### Description
    Show an expression in infix notation.

    ### Arguments
    - order: order of the expression (pre or post).
    - expression: expression to be shown.

    ### Returns
    - str: The expression in infix notation if it is valid.
    - None: If the expression is invalid.
    """
    # Split the expression into tokens
    elements = expression.split(" ")
    # If the order is pre, show the expression in infix notation
    if order.lower() == "pre":
        res = pre_show(elements)
    # If the order is post, show the expression in infix notation
    elif order.lower() == "post":
        res = post_show(elements)
    # If the order is not pre or post, return None
    else:
        return None
    return res
