from typing import Dict

def F_recursive(alpha: int, beta: int, n: int, dic: Dict[str, int] = {}) -> int:
    """
    ### Description
    This function calculates the value of a function F recursively.

    ### Arguments
    - alpha: positive integer.
    - beta: positive integer.
    - n: integer.
    - dic: dictionary to store the results of previous calculations. (default: {})

    ### Returns
    The value of the function F.
    """
    # Base case
    if 0 <= n < alpha * beta:
        dic[f"{alpha},{beta},{n}"] = n
        return n
    res = 0
    # Recursive case. For each i in [1, alpha], calculate the value of F(alpha, beta, n - beta * i)
    for i in range(1, alpha + 1):
        new_n = n - beta * i
        # If the value of F(alpha, beta, n - beta * i) is already calculated, use it
        if f"{alpha},{beta},{new_n}" in dic:
            res += dic[f"{alpha},{beta},{new_n}"]
        # Otherwise, calculate the value of F(alpha, beta, n - beta * i) recursively
        else:
            temp = F_recursive(alpha, beta, new_n, dic)
            dic[f"{alpha},{beta},{new_n}"] = temp
            res += temp
    return res

def F_tail(alpha: int, beta: int, n: int) -> int:
    """
    ### Description
    This function calculates the value of a function F using tail recursion.

    ### Arguments
    - alpha: positive integer.
    - beta: positive integer.
    - n: integer.

    ### Returns
    The value of the function F.
    """
    def helper(alpha: int, beta: int, n: int, acc: int = 0, dic: Dict[str, int] = {}) -> int:
        """
        ### Description
        This function calculates the value of a function F using tail recursion.

        ### Arguments
        - alpha: positive integer.
        - beta: positive integer.
        - n: integer.
        - acc: accumulator. (default: 0)
        - dic: dictionary to store the results of previous calculations. (default: {})
        """
        # Base case
        if 0 <= n < alpha * beta:
            return acc + n
        res = 0
        # Recursive case. For each i in [1, alpha], calculate the value of F(alpha, beta, n - beta * i)
        for i in range(1, alpha + 1):
            new_n = n - beta * i
            # If the value of F(alpha, beta, n - beta * i) is already calculated, use it
            if f"{alpha},{beta},{new_n}" in dic:
                res += dic[f"{alpha},{beta},{new_n}"]
            # Otherwise, calculate the value of F(alpha, beta, n - beta * i) recursively
            else:
                temp = helper(alpha, beta, new_n, 0, dic)
                dic[f"{alpha},{beta},{new_n}"] = temp
                res += temp
        return res
    # Call the helper function
    return helper(alpha, beta, n)

def F_iterative(alpha: int, beta: int, n: int) -> int:
    """
    ### Description
    This function calculates the value of a function F using iteration.

    ### Arguments
    - alpha: positive integer.
    - beta: positive integer.
    - n: integer.

    ### Returns
    The value of the function F.
    """
    dic: Dict[str, int] = {}
    # Calculate the value of F for each i in [0, alpha * beta]
    for i in range(alpha * beta):
        dic[f"{alpha},{beta},{i}"] = i
    # Calculate the value of F for n
    for i in range(alpha * beta, n + 1):
        res = 0
        # For each i in [1, alpha], calculate the value of F(alpha, beta, n - beta * i)
        for j in range(1, alpha + 1):
            new_n = i - beta * j
            res += dic[f"{alpha},{beta},{new_n}"]
        dic[f"{alpha},{beta},{i}"] = res
    return dic[f"{alpha},{beta},{n}"]