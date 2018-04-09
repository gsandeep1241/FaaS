import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../FaaS/DeveloperInterface/')))

import dev_main

dev_main.process_developer_input()