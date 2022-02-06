import numpy as np
import xlrd

def excelinput(path):#read excel data and transform to matrix function
    data = xlrd.open_workbook(path)
    table = data.sheets()[0] # get the first sheet in excel
    nrows = table.nrows  # number of rows
    ncols = table.ncols  # number of columns
    datamatrix = np.zeros((nrows, ncols))
    for x in range(ncols):
        cols = table.col_values(x)
        cols1 = np.matrix(cols)  # convert lists to matrices for matrix operations
        datamatrix[:, x] = cols1 # Store data
    return datamatrix  #m1 = excel2m("t1.xlsx");m2 = excel2m("t2.xlsx")#read data