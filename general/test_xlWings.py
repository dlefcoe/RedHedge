



# %% imports

import xlwings as xw
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



# %% main module
def the_main_code():
    """ the main module """
    some_code()



def some_code():
    # wb = xw.Book()  # this will create a new workbook
    fname = 'testExcel.xlsx'
    wb = xw.Book(fname)  # connect to an existing file in the current working directory


    #xw.apps[10559].books[fname]

    #Instantiate a sheet object
    sht = wb.sheets['Sheet1']

    # Reading/writing values to/from ranges is as easy as
    sht.range('A1').value = 'Foo 1'
    x = sht.range('A1').value

    print(x)

    expand_range(sht)
    some_pandas(sht)


def expand_range(sht):
    """
    takes a sheet and does range expanding
    """
    sht.range('a5').value =  [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
    x = sht.range('a5').value
    print('x has the value:', x)

    y = sht.range('a5').expand().value
    print('y has the range:', y)


def some_pandas(sht):
    """ some pandas stuff """
    df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
    sht.range('d1').value = df
    x = sht.range('d1').options(pd.DataFrame, expand='table').value
    print('the pandas dataframe:')
    print(x)

def some_matplotlib(sht):
    """ some matplotlib magic """
    fig = plt.figure()
    plt.plot([1,2,3,4,5])
    
    pass

if __name__ == "__main__":
    the_main_code()


# %%
