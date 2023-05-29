from os import system as sys

variables = {}
start = True 

while start == True:
    command = input("> ")

    if command.startswith("set"):
        parts = command.split()
        if len(parts) == 4 and parts[2] == "=":
            var_name = parts[1]
            var_value = parts[3]
            variables[var_name] = var_value
        else:
            print("unknown syntax: set <variable_name> = <value>")

    elif command.startswith("say"):
        
        if command == "say variable":
            print(variables)

        elif command.startswith("say var"):
            parts = command.split()
            if len(parts) == 3:
                var_name = parts[2]
                if var_name in variables:
                    print(variables[var_name])
                else:
                    print(f"variable '{var_name}' does not exist")
            else:
                print("unknown syntax: say var <variable_name>")
        else:
            command = command[4:]
            print(f"{command}")
    elif command == "quit":
        start = False
    elif command == "clear":
        sys("cls")


    elif command != "":
        print("unknown command:",command)
        string_length = int(len(command))
        error_char = "^" * string_length
        print("                ", error_char)


