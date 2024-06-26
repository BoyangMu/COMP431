import sys, socket, re


def next_input_line():
    current_line = input()
    return current_line


def input_from():
    #prompt for "From:" field and return input line
    sys.stdout.write("From:\n")
    return next_input_line().strip()

def input_to():
    #prompt for "To:" field and return input line
    sys.stdout.write("To:\n")
    return next_input_line().strip()

def input_subject():
    #prompt for "Subject:" field and return input
    sys.stdout.write("Subject:\n")
    return next_input_line().strip()



def input_message():
    sys.stdout.write("Message:\n")
    message = ""
    while True:
        line = input()
        message += line + "\n"
        if line == ".":
            break
    return message


def input_email(socket):
    email = {"from": "", "to": "", "subject": "", "message": ""}
    email['from'] = input_from()
    if email['from'] == "QUIT":
        socket.send("QUIT\n".encode())
        receive_data_from_server(socket)
        socket.close()
        quit()
    email['to'] = input_to()
    if email['to'] == "QUIT":
        socket.send("QUIT\n".encode())
        receive_data_from_server(socket)
        socket.close()
        quit()
    email['subject'] = input_subject()
    if email['subject'] == "QUIT":
        socket.send("QUIT\n".encode())
        receive_data_from_server(socket)
        socket.close()
        quit()
    email['message'] = input_message()
    if email['message'] == "QUIT":
        socket.send("QUIT\n".encode())
        receive_data_from_server(socket)
        socket.close()
        quit()
    return email

def send_data_to_server(data, socket):
    if(isinstance(data, list) == True):
        socket.send(data[0].encode())
        socket.send('.\n'.encode())
    else:
        socket.send(data.encode())


def receive_data_from_server(socket):
    try:
        message = socket.recv(4096).decode()
        sys.stdout.write(message)
        return message
    except socket.error as err:
        socket.close()
        quit()


def get_server_response_code(socket):
    response = receive_data_from_server(socket)
    response_code = ""
    match = re.fullmatch("(250|354|500|501|503)[ \t]+.*\n", response)
    if match:
        response_code = match.group(1) 
    return response_code


def send_data_to_server_and_expect_response_code(data, expected_response_code, socket):
    socket.send(data.encode())
    response_code = get_server_response_code(socket)
    if response_code != expected_response_code:
        quit_smtp(socket)
        sys.exit(0)

def quit_smtp(socket):
    send_data_to_server("QUIT\n", socket)
    receive_data_from_server(socket)
    socket.close()
    quit()

def send_email(mail, socket):
    send_data_to_server_and_expect_response_code(f"MAIL FROM: <{mail['from']}>\n", "250", socket)
    send_data_to_server_and_expect_response_code(f"RCPT TO: <{mail['to']}>\n", "250", socket)
    send_data_to_server_and_expect_response_code("DATA\n", "354", socket)

    message =  f"From: <{mail['from']}>\n"
    message += f"To: <{mail['to']}>\n"
    message += f"Subject: {mail['subject']}\n"
    message += f"\n"
    message += f"{mail['message']}"

    send_data_to_server_and_expect_response_code(message, "250", socket)

host = sys.argv[1]
port = int(sys.argv[2])
connected = False

def conductGreetings(host, socket):
    try:
        # greeting
        message = socket.recv(4096).decode()
        greeting = re.match('220\s+[ -~]*', message)
        sys.stdout.write(message)

        if greeting:
            socket.send(f"HELO {host}\n".encode())
            # greeting going the other way
            message = socket.recv(4096).decode()
            okay = re.match('250\s+[ -~]*', message)
            sys.stdout.write(message)
            if okay:
                return True
        return False
    except socket.error as err:
        quit()

connected = False

while (True):
    try:
        if not connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            conductGreetings(host, s)
            serverSocket = s
            connected = True
        email = input_email(serverSocket) 
        send_email(email, serverSocket)
    except EOFError:
        quit_smtp(serverSocket)