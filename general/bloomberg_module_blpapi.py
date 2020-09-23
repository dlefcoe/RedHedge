'''

we establish that in order to get bloomberg working with the current version of python we can use the below import method for the BLP api.
the link to the setup is here:

https://medium.com/@johann_78792/getting-started-with-bloombergs-python-desktop-api-5fd083b4193a


'''


import time
import os


with os.add_dll_directory('C:/blp/DAPI'):
    import blpapi

t = time.time()
print (t)


