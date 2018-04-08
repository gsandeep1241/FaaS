import sys
sys.path.insert(0, '../FaaS/DeveloperInterface/')
import dev_main

while True:
    cmd = raw_input('Enter your command:')

    if cmd == "quit":
        print ("Goodbye!")
        break

    ret = dev_main.process_developer_input(cmd)

    print(ret)