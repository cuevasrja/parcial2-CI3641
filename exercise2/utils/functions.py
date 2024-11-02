def need_brackets_post(operator1, operator2):
    if (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/'):
        return False
    if (operator1 == '*' or operator1 == '/') and (operator2 == '+' or operator2 == '-'):
        return True
    return False