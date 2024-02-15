import sys


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
                                        else:
                                            print("ERROR -- mail-from-cmd")
                                            return False               
                                    else:
                                        print("ERROR -- mail-from-cmd")
                                        return False 
                                else:
                                    print("ERROR -- mail-from-cmd") 
                                    return False
                            else:
                                print("ERROR -- mail-from-cmd")  
                                return False
                        else:
                            print("ERROR -- mail-from-cmd") 
                            return False
                    else:
                        print("ERROR -- whitespace")
                        return False
                else:
                    print("ERROR -- mail-from-cmd")
                    return False
            else:
                print("ERROR -- mail-from-cmd")
                return False
        else:
            print("ERROR -- mail-from-cmd")
            return False 
    else:
        print("ERROR -- mail-from-cmd") 
        return False
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


def is_path(user_input):
    global idx
    if user_input[idx] == "<":
        idx += 1
        if is_mailbox(user_input):
            if user_input[idx] == ">":
                idx += 1
                return True
            else:
                print("ERROR -- path")  
    else:
        print("ERROR -- path")  
    return False


def is_mailbox(user_input):
    global idx
    if is_local_part(user_input):
        if user_input[idx] == "@":
            idx += 1
            if is_domain(user_input):
                return True
        else:
            print("ERROR -- mailbox")
    return False


def is_local_part(user_input):
    global idx
    if is_string(user_input):
        return True
    print("ERROR -- string")  
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
    if is_name(user_input):
        return True
    if is_letter(user_input):
        return True
    else:
        idx -= 1
    print("ERROR -- element")  
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
    if user_input[idx] == "\n":
        idx += 1
        return True
    print("ERROR -- CRLF")  
    return False


for line in sys.stdin:
    user_input = line
    print(user_input[0:-1])
    idx = 0
    if is_mail_from_cmd(user_input) == True:
        print("Sender ok")
exit()


