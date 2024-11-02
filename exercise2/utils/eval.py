from typing import List
from utils.operations import operations

def pre_eval(expression: List[str]) -> int:
    """
    ### Description
    Evaluate a prefix expression.

    ### Parameters
    - expression: List[str] -> The prefix expression to evaluate.

    ### Return
    - int: The result of the expression.
    """
    nums: List[int] = [int(x) for x in expression if x.isdigit()]
    operators: List[str] = [x for x in expression if not x.isdigit()]
    result: int = nums[0]
    for i in range(1, len(nums)):
        result = operations[operators[i-1]](result, nums[i])
    return result

def post_eval(expression: List[str]) -> int:
    """
    ### Description
    Evaluate a postfix expression.

    ### Parameters
    - expression: List[str] -> The postfix expression to evaluate.

    ### Return
    - int: The result of the expression.
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
    return stack[0]
    

def eval(order: str, expression: str) -> None:
    elements = expression.split(" ")
    if order.lower() == "pre":
        res = pre_eval(elements)
        print(res)
    elif order.lower() == "post":
        res = post_eval(elements)
        print(res)
    else:
        print("Invalid order")
    print()