'''

reference data using the XBBG module

blp returns a pandas dataframe
we can easily get items from the dataframe

contact:
gitHub: @dlefcoe
twitter: @dlefcoe
email: darren@redhedge.uk

'''

import os

import time
import datetime
import collections

import blpapi
from xbbg import blp

import openpyxl
import pandas as pd

# import numpy as np

bloombergLimit = 500_000


def main():

    # measure time for some basic examples
    t1 = time.time()
    
    # basic example (not used now)
    #examples()
    
    bondData = get_bonds()    
    t2 = time.time()

    # save data to file
    isStored = store_data(bondData)

    t3 = time.time()


    print('the time take is:', round(t2-t1, 3) , 'seconds')


def examples():
    """
    examples of how to get basic data from bbg
    """

    # get some data for a single name
    x = blp.bdp('BDEV LN Equity', 'px_last')
    print(x)
    print('the type of x', type(x))
    print('the value of x:', x.iloc[0]['px_last'])


    # get multiple data for a single name
    y = blp.bdp('BDEV LN Equity', flds=['px_bid', 'px_ask'])
    print(y)


    # get multiple data for multiple names
    z = blp.bdp(tickers=['BDEV LN Equity', 'BARC LN Equity'], flds=['px_bid', 'px_ask'])
    print(z)
    print('here is the bdev ask >>>', z.loc['BDEV LN Equity','px_ask'])


def store_data(someData):
    ''' function to store data to file 
    
    if data is stored:
        return: True otherwise False
    '''

    dataWritten = False

    # location to store file
    pathToStore = os.path.dirname(__file__)
    # use a subfolder callled data folder
    pathToStore = os.path.join(pathToStore, 'dataFolder')
    print(f'the file resides here: {pathToStore}')

    # file name
    fileDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    

    fileToStoreXLSX = 'hybrids_results ' + fileDateTime + '.xlsx'
    fileToStoreHTML = 'hybrids_results ' + fileDateTime + '.html'
    print(f'the name of the excel file: {fileToStoreXLSX}')
    print(f'the name of the HTML file: {fileToStoreHTML}')

    # full path name
    fullPathToStoreXLSX = os.path.join(pathToStore, fileToStoreXLSX)
    fullPathToStoreHTML = os.path.join(pathToStore, fileToStoreHTML)    
    
    # save the file (to excel and html)
    df = pd.DataFrame(someData)
    df.to_excel(fullPathToStoreXLSX)
    df.to_html(fullPathToStoreHTML)
    dataWritten = True


    return dataWritten

    



def get_bonds():
    """
    function to get bond data from bloomberg using tickers in an excel sheet.

    return:
        data - a pandas data set
    """

    print('getting bond data...')
    # securtiyList = ['US29265WAA62 Corp', 'XS1713463559 Corp', 'XS2000719992 Corp', 'XS0954675129 Corp', 'XS0954675129 Corp']
    fieldList = ['ticker', 'coupon', 'nxt_call_dt', 'final_maturity', 
                'mty_typ', 'px_mid', 'z_sprd_mid', 'yas_ispread', 'yas_bond_yld', 
                'yas_risk','crncy', 'payment_rank', 'industry_sector','rtg_moody','rtg_sp']

    # the script fis here
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # get items from sheet (in the same folder)
    fileToGet = 'hybridSecurityList.xlsx'
    # join file and correct folder
    fileToGet = os.path.join(dir_path, fileToGet)
    secListXlsx = pd.ExcelFile(fileToGet)
    
    # the names of the available sheets
    print('getting security list from:', secListXlsx.sheet_names)
    df = pd.DataFrame(secListXlsx.parse('tickers'))
    print('summary of the data')
    print(df.info)
    
    # put all isin's in a list
    isin = df.iloc[:,1].tolist()
    securtiyList = [x + " Corp" for x in isin]

    # make the lists unique (and keep the order)
    securtiyList = list(collections.OrderedDict.fromkeys(securtiyList))

    # get the data from bloomberg
    print('getting data from bbg')

    # replaced with getListDataFromBbg function
    '''
    if len(securtiyList) > 49:
        # there are lots of securities
        print(f'lots of data requested: {len(securtiyList)} items requested')
        reducedListSize = input(f'reduce list size to value or press "x" to use {len(securtiyList)}  >>>')
        if reducedListSize == 'x':
            # keep the same size
            reducedListSize = len(securtiyList)
        else:
            # reeduce the list size
            reducedListSize = int(reducedListSize)
        
        # set the reduced list to size selected
        reducedList = securtiyList[0:reducedListSize]
        # run code on the smaller list
        bondData = bloombergAPI_bigData(reducedList,fieldList, 10)
    else:
        bondData = blp.bdp(tickers=securtiyList, flds=fieldList)
    '''

    bondData = getListDataFromBbg(securtiyList, fieldList)

    #print('number of columns:', data.head())
    print('data is fetched:')
    print(bondData.info)

    return bondData


def getListDataFromBbg(securtiyList, fieldList):
    ''' 
    gets data from bloomberg using a while loop until completion

        inputs:
            securtiyList - list of tickers to obtain
            fieldList - the fields requested for each ticker

        output:
            resultsOfDataReq - resulting pandas array of the data that was requested

    '''
    # get the data (bdp returns a dataframe)
    resultsOfDataReq = blp.bdp(tickers=securtiyList, flds=fieldList)

    
    #pre-loop initialization
    keepLooping = True
    loopingCounter = 0
    while keepLooping:
        
        # check which items are missing
        listError = list(set(securtiyList)-set(resultsOfDataReq.index.values))
        
        if len(listError) == 0:
            # data collection process finished
            keepLooping = False
            break
        else:
            print(len(listError), 'of', len(securtiyList), 'remaining', ': loop', loopingCounter)
            loopingCounter += 1
            if loopingCounter > 10:
                # more than 10 tries at data collection
                keepLooping = False
                break

        # get and append more data
        try:
            nextChunk = blp.bdp(tickers=listError, flds=fieldList)
            resultsOfDataReq = resultsOfDataReq.append(nextChunk)
        except:
            print('no data to add')

        # remove duplicates
        resultsOfDataReq = resultsOfDataReq.drop_duplicates()

    return resultsOfDataReq
    


def bloombergAPI_bigData(securtiyList, fieldList, rowChunk):
    ''' 
    if the number of tickers and fields are too large, then this function is used to break up the lists to allow for data connection

        inputs:
            securtiyList - list of tickers to obtain
            fieldList - the fields requested for each ticker
            rowChunk - how many rows to aquire in one batch

        output:
            resultsOfDataReq - resulting pandas array of the data that was requested
    '''


    # split the security list into batches of n rows
    n = rowChunk
    iterationsRequired = int(len(securtiyList) / n)
    remainingBit = len(securtiyList) - iterationsRequired * n
    
    print(f'we will iterate {iterationsRequired} times and {remainingBit} will be left')
    

    resultsOfDataReq = pd.DataFrame()
    # bulk of data
    for i in range(iterationsRequired):
        print('processing: ', i*n, 'to', (i+1)*n, 'from the list.')
        nextChunk = blp.bdp(tickers=securtiyList[i*n:(i+1)*n], flds=fieldList)
        resultsOfDataReq = resultsOfDataReq.append(nextChunk)
        percentDone = round((len(resultsOfDataReq.index) / len(securtiyList))*100, 1)
        print('items completed:', len(resultsOfDataReq.index), 'out of', len(securtiyList),  "=> precent aquired:", percentDone)
        # if i > 2:
        #     print('breaking the loop for testing purpose')
        #     break

    # end stub
    if remainingBit == 0:
        # there is no stub
        pass
    else:
        # process the stub
        print('processing last chuunk: ', iterationsRequired*n, 'to', len(securtiyList))
        nextChunk = blp.bdp(tickers=securtiyList[iterationsRequired*n:len(securtiyList)], flds=fieldList)
        percentDone = round((len(resultsOfDataReq.index) / len(securtiyList))*100, 1)
        print('items completed:', len(resultsOfDataReq.index), 'out of', len(securtiyList), "=> precent aquired:", percentDone)

    # compare rows of dataframe to securitiy list to find the missing items
    #print('index column of the pandas list')]
    #print(list(resultsOfDataReq.index.values))
    print('missing items from the securities list')
    listError = list(set(securtiyList)-set(resultsOfDataReq.index.values))
    print(listError)
    

    return resultsOfDataReq




if __name__ == "__main__":
    main()
    pass

