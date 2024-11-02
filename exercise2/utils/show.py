from typing import List

def precedence(op: str) -> int:
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def pre_show(expression: List[str]) -> str:
    pass

def post_show(expression: List[str]) -> str:
    pass
        

def show(order: str, expression: str):
    elements = expression.split(" ")
    if order.lower() == "pre":
        res = pre_show(elements)
        print(res)
    elif order.lower() == "post":
        res = post_show(elements)
        print(res)
    else:
        print("Invalid order")
    print()
