from typing import List

def is_operator(c: str) -> bool:
    return c in {'+', '-', '*', '/'}

def needs_parentheses(op1: str, op2: str, pos: int) -> bool:
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return operator_precedence[op1] < operator_precedence[op2] if pos == 0 else operator_precedence[op1] <= operator_precedence[op2]

def pre_show(expression: List[str]) -> str|None:
    stack = []

    for token in reversed(expression):
        if is_operator(token):
            if len(stack) < 2:
                return None
            first_operand, first_operator = stack.pop()
            second_operand, second_operator = stack.pop()

            if first_operator and needs_parentheses(first_operator, token, 0):
                first_operand = f"({first_operand})"
            if second_operator and needs_parentheses(second_operator, token, 1):
                second_operand = f"({second_operand})"

            stack.append((f"{first_operand} {token} {second_operand}", token))
        else:
            stack.append((token, ""))

    if len(stack) != 1:
        return None

    return stack[-1][0]

def post_show(expression: List[str]) -> str|None:
    stack = []

    for token in expression:
        if is_operator(token):
            if len(stack) < 2:
                return None
            second_operand, second_operator = stack.pop()
            first_operand, first_operator = stack.pop()

            if first_operator and needs_parentheses(first_operator, token, 0):
                first_operand = f"({first_operand})"
            if second_operator and needs_parentheses(second_operator, token, 1):
                second_operand = f"({second_operand})"

            stack.append((f"{first_operand} {token} {second_operand}", token))
        else:
            stack.append((token, ""))

    if len(stack) != 1:
        return None

    return stack[-1][0]
        

def show(order: str, expression: str) -> None|str:
    elements = expression.split(" ")
    if order.lower() == "pre":
        res = pre_show(elements)
    elif order.lower() == "post":
        res = post_show(elements)
    else:
        return None
    return res
