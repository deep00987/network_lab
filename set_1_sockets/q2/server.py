# Write a TCP Math server program that accepts any valid integer arithmetic expression, evaluates it and
# returns the value of the expression. Also write a TCP client program that accepts an integer arithmetic
# expression from the user and sends it to the server to get the result of evaluation. Choose your own formats
# for the request/reply messages.

from datetime import datetime
import socket

HOST = "127.0.0.1"
PORT = 32768
BUFF_SIZE = 1024

def calculate(s):
    operators = []
    operands = []
    prec = {
        '+' : 1,
        '-' : 1,
        '*' : 2, 
        '/' : 2,
    }
    m = len(s)
    i = 0
    while i < m:
        if s[i].isdigit() == True:
            value = 0
            while i < m and s[i].isdigit():
                value = (value * 10) + (ord(s[i]) - ord('0'))
                i += 1
                operands.append(value)
                i = i - 1
        elif s[i] in prec:

            while len(operators) > 0 and prec[operators[-1]] >= prec[s[i]]:
                op2 = operands.pop()
                op1 = operands.pop()
                operator = operators.pop()
                res = operate(op1, op2, operator)
                operands.append(res)
                
            operators.append(s[i])
        else:
            i += 1
            continue
        i += 1
    while len(operators) > 0:
        op2 = operands.pop()
        op1 = operands.pop()
        operator = operators.pop()
        res = operate(op1, op2, operator)
        operands.append(res)
        
    return operands[0]
    

def operate(v1, v2, op):
    if op == '+': return v1 + v2
    elif op == '-': return v1 - v2
    elif op == '*': return v1 * v2
    elif op == '/' and v2 != 0:
        return v1 // v2
    else: return -999  


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Server listining on {HOST}:{PORT}")
    
    conn = None
    try:
        conn, addr = server.accept()
            
        data = conn.recv(BUFF_SIZE)
        print ("Client --> ", data.decode())
        
        res = eval(data.decode())
        msg = f"result: {res}"
        print("server --> ", msg)

        conn.send(msg.encode())
        data = conn.recv(BUFF_SIZE)
        print(f"Client --> ", data.decode())
        
        conn.close()

        print("connection closed.")

    except KeyboardInterrupt:
        print("key pressed ctrl + c")
        server.close()

    server.close()

if __name__ == "__main__":
    main()