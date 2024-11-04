from typing import List
from utils.operations import operations

def pre_eval(expression: List[str]) -> int|None:
    """
    ### Description
    Evaluate a prefix expression.

    ### Parameters
    - expression: List[str] -> The prefix expression to evaluate.

    ### Return
    - int: The result of the expression.
    - None: If the expression is invalid.
    """
    stack = []

    # For each token in the expression in reverse order
    for token in reversed(expression):
        # If the token is not an operator, add it to the stack
        if token not in operations.keys():
            stack.append(int(token))
        # If the token is an operator
        else:
            # If there are less than 2 elements in the stack, the expression is invalid
            if len(stack) < 2:
                return None
            # Pop the left and right operands
            left_operand = stack.pop()
            right_operand = stack.pop()
            # Calculate the result of the operation and add it to the stack
            result: int = operations[token](left_operand, right_operand)
            stack.append(result)
    return stack.pop()

def post_eval(expression: List[str]) -> int|None:
    """
    ### Description
    Evaluate a postfix expression.

    ### Parameters
    - expression: List[str] -> The postfix expression to evaluate.

    ### Return
    - int: The result of the expression.
    - None: If the expression is invalid.
    """
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = operations[token](a, b)
            stack.append(result)
    return stack[0] if len(stack) == 1 else None
    

def eval(order: str, expression: str) -> None|str:
    """
    """
    elements = expression.split(" ")
    if order.lower() == "pre":
        res = pre_eval(elements)
    elif order.lower() == "post":
        res = post_eval(elements)
    else:
        return None
    return res