import sys


start = 0
end = 0
with open(sys.argv[1],"r") as f:
    for line in f:
        if line[0:5] == "From:" and start == 1:
            print(".")
            user_input = input()
            if user_input[0:4] != "250 ":
                print(user_input)
                print("QUIT")
                exit()
            else:
                print(user_input)
            print("MAIL FROM:" + line[5:-1])
            user_input = input()
            if user_input[0:4] != "250 ":
                print(user_input, file=sys.stderr)
                print("QUIT")
                exit()
            else:
                print(user_input, file=sys.stderr) 
        elif line[0:5] == "From:":
            print("MAIL FROM:" + line[5:-1])
            user_input = input()
            if user_input[0:4] != "250 ":
                print(user_input, file=sys.stderr)
                print("QUIT")
                exit()
            else:
                print(user_input, file=sys.stderr)
        elif line[0:3] == "To:":
            print("RCPT TO:" + line[3:-1])
            user_input = input()
            if user_input[0:4] != "250 ":
                print(user_input, file=sys.stderr)
                print("QUIT")
                exit()
            else:
                print(user_input, file=sys.stderr)
        elif start == 0:
            print("DATA")
            start = 1
            user_input = input()
            if user_input[0:4] != "354 ":
                print(user_input, file=sys.stderr)
                print("QUIT")
                exit()
            else:
                print(user_input, file=sys.stderr)
            print(line[:-1])
        else:
            print(line[:-1])
        

print(".")
user_input = input()
print(user_input, file=sys.stderr)
print("QUIT")
exit()


        

    