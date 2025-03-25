import sys
from collections import deque
import re

def isOperator(operator):
    return operator in {'+', '-', '*', '/', '%', '^', '~'}

def validOperands(left, right, operator):
    if isOperator(left) == True or left == None:
            raise RuntimeError("Not enough operands.")
    if isOperator(right) == True or right == None:
            raise RuntimeError("Not enough operands.")
    if right == 0 and (operator == "%" or operator == '/'):
            raise RuntimeError("Division by zero.")

def tokenize(math_expression):
    split_into_substrings = math_expression.split()
    tokenized_deque = deque(split_into_substrings)
    for element in range(len(tokenized_deque)):
        if isOperator(tokenized_deque[element]) == True:
            continue
        if re.match(r'^[+-]?(\d+(\.\d+)?|\.\d+)$', tokenized_deque[element]):
            tokenized_deque[element] = float(tokenized_deque[element])
        else:
            raise RuntimeError(f'Invalid token: "{tokenized_deque[element]}"')
    return tokenized_deque

def evaluatePrefix(token_deque):
    
    if not token_deque:
        raise RuntimeError("No input.")

    if isOperator(token_deque[0]) != True:
            some_num = token_deque.popleft()
            return some_num


    operator = token_deque.popleft()
    
    if operator == '~':
        if not token_deque:
            raise RuntimeError("Not enough operands.")
        left_operand = -1.0
        right_operand = evaluatePrefix(token_deque)
        return left_operand * right_operand


    if not token_deque:
        raise RuntimeError("Not enough operands.")

    left_operand = evaluatePrefix(token_deque)

    if not token_deque:
        raise RuntimeError("Not enough operands.")

    right_operand = evaluatePrefix(token_deque)

    if operator == "+":
        validOperands(left_operand, right_operand, operator)
        return left_operand + right_operand

    if operator == "-":
        validOperands(left_operand, right_operand, operator)
        return left_operand - right_operand

    if operator == "*":
        validOperands(left_operand, right_operand, operator)
        return left_operand * right_operand

    if operator == "/":
        validOperands(left_operand, right_operand, operator)
        return left_operand / right_operand

    if operator == "%":
        validOperands(left_operand, right_operand, operator)
        return left_operand % right_operand

    if operator == "^":
        validOperands(left_operand, right_operand, operator)
        return left_operand ** right_operand


def prefix(token_deque):
    if token_deque:
        totalvalue = evaluatePrefix(token_deque)
        if token_deque:   
            raise RuntimeError("Too much input.") 
        return totalvalue
    else:
        raise RuntimeError('No input.')

def postfix(token_deque):
    
    if not token_deque:
        raise RuntimeError("No input.")
    result = None
    teck_deck = deque()
    for token in token_deque:
        if isinstance(token, float):
            teck_deck.append(token)
        elif isOperator(token):
            if token == '~':
                if len(teck_deck) < 1:
                    raise RuntimeError("Not enough operands.")
                operand = teck_deck.pop()
                result = -operand
                teck_deck.append(result)
                continue
            if len(teck_deck) < 2:
                raise RuntimeError("Not enough operands.")
            right_operand = teck_deck.pop()
            left_operand = teck_deck.pop()


            if token == "+":
                validOperands(left_operand, right_operand, token)
                result = left_operand + right_operand

            if token == "-":
                validOperands(left_operand, right_operand, token)
                result = left_operand - right_operand

            if token == "*":
                validOperands(left_operand, right_operand, token)
                result = left_operand * right_operand

            if token == "/":
                validOperands(left_operand, right_operand, token)
                result = left_operand / right_operand

            if token == "%":
                validOperands(left_operand, right_operand, token)
                result = left_operand % right_operand

            if token == "^":
                validOperands(left_operand, right_operand, token)
                result = left_operand ** right_operand
            
            teck_deck.append(result)
    if len(teck_deck) == 1:
        return teck_deck.pop()
    else:
        raise RuntimeError("Too many operands.")
