from typing import Callable, Dict

def sum(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    return a // b

operations: Dict[str, Callable[[int, int], int]] = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}