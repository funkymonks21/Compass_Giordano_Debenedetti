def calcular_valor_maximo(operadores,operandos):
    def calcular_lista(operador, operando):
        match operador:
            case '+':
                return operando[0] + operando[1]
            case '-':
                return operando[0] - operando[1]
            case '/':
                return operando[0] / operando[1]
            case '*':
                return operando[0] * operando[1]
            case '%':
                return operando[0] % operando[1]
    resultado = list(map(lambda x: calcular_lista(x[0], x[1]), zip(operadores, operandos)))
    return max(resultado)

operadores = ['+', '*', '*', '/', '-']
operandos = [(2,4), (2,4), (2,8), (20,1), (19,-3)]

if __name__ == '__main__':
    print(f'O maior resultado das operações é: {calcular_valor_maximo(operadores,operandos)}')