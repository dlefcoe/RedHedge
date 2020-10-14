import sys
import os
# sub folder with modules
sys.path.append('R:\\Quant Tools\\code\\bbg\\corpHybrids\\modules')

import hybridsMethods as hm

# import hy
print('this works')


# we can use the relative import which is cleaner
import dl_py_modules.hybridsMethods as hoo



print('the hoo file resides here:', hoo.__file__)

# print(sys.path)

x = hm.oneYearBonds(1)
print(hm.__file__)
print(os.__file__)




