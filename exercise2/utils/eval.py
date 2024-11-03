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
    nums: List[int] = [int(x) for x in expression if x.isdigit()]
    operators: List[str] = [x for x in expression if not x.isdigit()]
    if len(nums) == 0 or (len(operators) == 0 and len(nums) > 1):
        return None
    result: int = nums[0]
    for i in range(1, len(nums)):
        result = operations[operators[i-1]](result, nums[i])
    return result

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