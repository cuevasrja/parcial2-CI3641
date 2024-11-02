from typing import Dict

def F_recursive(alpha: int, beta: int, n: int, dic: Dict[str, int] = {}) -> int:
    if 0 <= n < alpha * beta:
        dic[f"{alpha},{beta},{n}"] = n
        return n
    res = 0
    for i in range(1, alpha + 1):
        new_n = n - beta * i
        if f"{alpha},{beta},{new_n}" in dic:
            res += dic[f"{alpha},{beta},{new_n}"]
        else:
            temp = F_recursive(alpha, beta, new_n, dic)
            dic[f"{alpha},{beta},{new_n}"] = temp
            res += temp
    return res

def F_iterative(alpha: int, beta: int, n: int) -> int:
    dic: Dict[str, int] = {}
    for i in range(alpha * beta):
        dic[f"{alpha},{beta},{i}"] = i
    for i in range(alpha * beta, n + 1):
        res = 0
        for j in range(1, alpha + 1):
            new_n = i - beta * j
            res += dic[f"{alpha},{beta},{new_n}"]
        dic[f"{alpha},{beta},{i}"] = res
    return dic[f"{alpha},{beta},{n}"]

def F_tail(alpha: int, beta: int, n: int) -> int:
    def helper(alpha: int, beta: int, n: int, acc: int, dic: Dict[str, int] = {}) -> int:
        if 0 <= n < alpha * beta:
            return acc + n
        res = 0
        for i in range(1, alpha + 1):
            new_n = n - beta * i
            if f"{alpha},{beta},{new_n}" in dic:
                res += dic[f"{alpha},{beta},{new_n}"]
            else:
                temp = helper(alpha, beta, new_n, 0, dic)
                dic[f"{alpha},{beta},{new_n}"] = temp
                res += temp
        return res
    return helper(alpha, beta, n, 0)