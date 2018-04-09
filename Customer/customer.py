import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../FaaS/CustomerInterface/')))

import cust_main

cust_main.process_customer_input()