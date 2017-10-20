#!python
#coding=utf-8
#将给定的列表按要求，在屏幕上打印出来

#定义函数
def printTable(tableData):
    colWiths=[0]*len(tableData)
    for i in range(len(tableData)):
        templist=[]
        for j in range(len(tableData[i])):
          templist=templist+[len(tableData[i][j])]
        colWiths[i]=max(templist)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print tableData[j][i].rjust(max(colWiths)),
        print


#定义列表，并调用函数进行打印
tableData=[["apples","oranges","cherries","banana"],
["Alice","Boo","Carol","David"],
["dogs","cats","moose","gooose"]
]
printTable(tableData)