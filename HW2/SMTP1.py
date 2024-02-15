# Boyang Mu: I pledge that I have not given or received any unauthorized help on this assignment, and that this work is my own.
import sys
import re


def is_mail_from_cmd(user_input):
    global idx
    if user_input[idx] == 'M':
        idx += 1
        if user_input[idx] == 'A':
            idx += 1 
            if user_input[idx] == 'I':
                idx += 1
                if user_input[idx] == 'L':
                    idx += 1
                    if is_whitespace(user_input):
                        if user_input[idx] == 'F':
                            idx += 1
                            if user_input[idx] == 'R':
                                idx += 1
                                if user_input[idx] == 'O':
                                    idx += 1
                                    if user_input[idx] == 'M':
                                        idx += 1
                                        if user_input[idx] == ':':
                                            idx += 1    
                                            if is_nullspace(user_input):
                                                if is_reverse_path(user_input):
                                                    if is_nullspace(user_input):
                                                        if is_crlf(user_input):
                                                            return True
    idx = 0
    return False


def is_rcpt_to_cmd(user_input):
    global idx
    if user_input[idx] == 'R':
        idx += 1
        if user_input[idx] == 'C':
            idx += 1 
            if user_input[idx] == 'P':
                idx += 1
                if user_input[idx] == 'T':
                    idx += 1
                    if is_whitespace(user_input):
                        if user_input[idx] == 'T':
                            idx += 1
                            if user_input[idx] == 'O':
                                idx += 1
                                if user_input[idx] == ':':
                                    idx += 1    
                                    if is_nullspace(user_input):
                                        if is_forward_path(user_input):
                                            if is_nullspace(user_input):
                                                if is_crlf(user_input):
                                                    return True
    idx = 0
    return False


def is_data_cmd(user_input):
    global idx
    if user_input[idx] == 'D':
        idx += 1
        if user_input[idx] == 'A':
            idx += 1 
            if user_input[idx] == 'T':
                idx += 1
                if user_input[idx] == 'A':
                    idx += 1
                    if is_nullspace(user_input):
                        if is_crlf(user_input):
                            return True
    idx = 0
    return False



def is_whitespace(user_input):
    global idx
    if is_space(user_input):
        if is_whitespace(user_input):
            return True
        return True    
    else: 
        return False


def is_space(user_input):
    global idx
    if user_input[idx] == ' ' or user_input[idx] == '\t':
        idx += 1
        return True
    else:
        return False


def is_nullspace(user_input):
    global idx
    if is_whitespace(user_input):
        return True
    else:
        return True


def is_reverse_path(user_input):
    global idx
    if is_path(user_input):
        return True
    else:
        return False


def is_forward_path(user_input):
    global idx
    if is_path(user_input):
        return True
    else:
        return False


def is_path(user_input):
    global idx
    global syntax_error
    if user_input[idx] == "<":
        idx += 1
        if is_mailbox(user_input):
            if user_input[idx] == ">":
                idx += 1
                return True
            else:
                syntax_error = 1
    else:
        syntax_error = 1 
    return False


def is_mailbox(user_input):
    global idx
    global syntax_error
    if is_local_part(user_input):
        if user_input[idx] == "@":
            idx += 1
            if is_domain(user_input):
                return True
        else:
            syntax_error = 1
    return False


def is_local_part(user_input):
    global idx
    global syntax_error
    if is_string(user_input):
        return True
    syntax_error = 1
    return False

def is_string(user_input):
    global idx
    if is_char(user_input):
        if is_string(user_input):
            return True
        return True    
    else: 
        return False

def is_char(user_input):
    global idx
    special = ["<", ">", "(", ")", "[", "]", "\\", ".", ",", ";", ":", "@", "\""]
    if (user_input[idx].isascii()) and (user_input[idx] not in special) and (user_input[idx] != " "):
        idx += 1
        return True
    return False


def is_domain(user_input):
    global idx
    if is_element(user_input):
        if user_input[idx] == ".":
            idx += 1
            if is_domain(user_input):
                return True
            else:
                return False
        return True
    return False


def is_element(user_input):
    global idx
    global syntax_error
    if is_name(user_input):
        return True
    if is_letter(user_input):
        return True
    else:
        idx -= 1
    syntax_error = 1  
    return False


def is_name(user_input):
    global idx
    if is_letter(user_input):
        if is_let_dit_str(user_input):
            return True
        idx -= 1
    return False


def is_letter(user_input):
    global idx
    if user_input[idx].isalpha():
        idx += 1
        return True
    return False

def is_let_dit_str(user_input):
    global idx
    if is_let_dig(user_input):
        if is_let_dit_str(user_input):
            return True
        return True
    return False


def is_let_dig(user_input):
    global idx
    if is_letter(user_input):
        return True
    if is_digit(user_input):
        return True
    return False


def is_digit(user_input):
    global idx
    if user_input[idx].isdigit():
        idx += 1
        return True
    return False

def is_crlf(user_input):
    global idx
    global syntax_error
    if user_input[idx] == "\n":
        idx += 1
        return True
    syntax_error = 1
    return False



previous = 0
data = ""
dup_data = ""
file_path = []
if_data = False
for line in sys.stdin:
    user_input = line
    print(user_input[0:-1])
    idx = 0
    syntax_error = 0
    if previous == 0:
        if is_mail_from_cmd(user_input):
            print("250 OK")
            previous = 1
            mail_from = re.search('<(.+?)>', user_input)
            if mail_from:
                address = mail_from.group(1)
            data += "From: <" + address + ">\n"
        else:
            if is_rcpt_to_cmd(user_input) or is_data_cmd(user_input):
                print("503 Bad sequence of commands")
                previous = 0
                data = ""
                file_path = []
            else:
                if syntax_error == 0:
                    print("500 Syntax error: command unrecognized")
                else:
                    print("501 Syntax error in parameters or arguments")
                previous = 0
                data = ""
                file_path = []
    elif previous == 1:
        if is_rcpt_to_cmd(user_input):
            print("250 OK")
            previous = 2
            rcpt_tp = re.search('<(.+?)>', user_input)
            if rcpt_tp:
                address = rcpt_tp.group(1)
            data += "To: <" + address + ">\n"
            path = "HW2/forward/" + address
            file_path.append(path)
        else:
            if is_mail_from_cmd(user_input) or is_data_cmd(user_input):
                print("503 Bad sequence of commands")
                previous = 0
                data = ""
                file_path = []
            else:
                if syntax_error == 0:
                    print("500 Syntax error: command unrecognized")
                else:
                    print("501 Syntax error in parameters or arguments")
                previous = 0
                data = ""
                file_path = []
    elif previous == 2:
        if is_rcpt_to_cmd(user_input):
            print("250 OK")
            previous = 2
            rcpt_tp = re.search('<(.+?)>', user_input)
            if rcpt_tp:
                address = rcpt_tp.group(1)
            path = "HW2/forward/" + address
            data += "To: <" + address + ">\n"
            file_path.append(path)
        elif is_data_cmd(user_input):
            print("354 Start mail input; end with <CRLF>.<CRLF>")
            previous = 3
        else:
            if is_mail_from_cmd(user_input):
                print("503 Bad sequence of commands")
                previous = 0
                data = ""
                file_path = []
            else:
                if syntax_error == 0:
                    print("500 Syntax error: command unrecognized")
                else:
                    print("501 Syntax error in parameters or arguments")
                previous = 0
                data = ""
                file_path = []
    elif previous == 3:
        data += user_input
        if_data = True
        dup_data = data
        if data[-3:] == "\n.\n":
            for path in file_path:
                f = open(path, "a")
                f.write(data[:-2])
                f.close()
            data = ""
            file_path = []
            if_data = False
            print("250 OK")
            previous = 0
    syntax_error = 0

if if_data and dup_data[-3:] != "\n.\n":
    print("501 Syntax error in parameters or arguments")

exit()


