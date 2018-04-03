connected = False
while True:
    cmd = raw_input("Enter your command:")
    cmd_parts = cmd.split(' ')

    if(cmd_parts[0] == "quit"):
        break;

    if(cmd_parts[0] != "connect" and !connected):
        print("Please first connect to the lambda service.")
        continue

    if(cmd_parts[0] == "connect"):
        connected = True
        continue

    if(cmd_parts[0] == "setup"):
        #setup account with the lambda service
        continue

    if(cmd_parts[0] == "login"):
        #login to the service
        continue

    if(cmd_parts[0] == "deploy"):
        #deploy files to the lamdba service
        continue