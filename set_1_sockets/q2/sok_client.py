import socket
import json

HOST = socket.gethostname().split('.')[0]
PORT = 7000
BUFF_SIZE = 1024

def validate_first_brackets(expression):
    stack = []

    for char in expression:
        if char in ['[', '{']:
            return False  
        elif char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False  
            stack.pop()

    return len(stack) == 0

def validate_balanced_brackets(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False  
            stack.pop()

    return len(stack) == 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
    """
    request struct = {
        method: GET
        msg: math expression string 
    }

    response struct --> {
        status: NUMBER
        data: response (math expression) data OR error msg
    }
    """
    try:
        skt.connect((HOST, PORT))
        req = {}
        req["method"] = "GET"
        
        print(f"Client connected on {HOST}:{PORT}")
        msg = input("Enter expression: ")

        if not validate_first_brackets(msg):
            raise Exception(f"Please use only first brackets in the expression")
        
        if not validate_balanced_brackets(msg):
            raise Exception(f"Brackets are not balanced in the expression")
        try:
            res = eval(msg)
            print(res)
        except Exception as e:
            raise Exception("Invalid math Expression")
        
        req["msg"] = msg
        skt.sendall(json.dumps(req).encode())    

        print("Client request: ", req)

        data = skt.recv(BUFF_SIZE)
        res = json.loads(data.decode())
        
        print("response from server: ", res)
        
        print(f"Server --> status: {res['status']}, data: {res['data']}")
        
        skt.close()
    except Exception as e:
        print(e)
        err_res = {
            "status" : 500,
            "data": str(e)
        }
        print(err_res)
        skt.close()



