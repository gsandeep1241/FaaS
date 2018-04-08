import sys
sys.path.insert(0, '../FaaS/CustomerInterface/')
import cust_main

while True:
    cmd = raw_input('Enter your command:')

    if cmd == "quit":
        print ("Goodbye!")
        break

    ret = cust_main.process_customer_input(cmd)

    print(ret)