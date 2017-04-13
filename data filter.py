#!/usr/bionpython
# coding:utf-8
import os

import datetime

from datetime import timedelta
from xlsxwriter.workbook import Workbook


import csv


def readxml():
    tmpdict = dict()
    dirname = """D:\pyworkspace\dataet1"""
    filename = "belle_answer4.csv"
    f = open(filename, 'rb')
    reader = csv.reader(f)
    cn = 0
    for row in reader:
        if cn == 0:
            cn+=1
            continue
        tmpkey = str(row[1])+str(row[2])
        left = str(row[6])
        right = str(row[7])
        tmpsum = left + right
        #print tmpkey+" "+str(left)+" " +str(right)+" "+str(tmpsum)

        tmpinnerdict = dict()
        keylist,keysum = tmpdict.get(tmpkey,[list(),tmpinnerdict])
        keylist.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        innersum = keysum.get(tmpsum,0)
        innersum += 1
        keysum[tmpsum]=innersum
        tmpdict[tmpkey]=[keylist,keysum]

        cn+=1
        print keysum
    f.close()

    # threslist = [8,9]
    # for thres in threslist:
    #     filename = "newset" + "_" + str(thres) + ".xlsx"
    #     workbook = Workbook(filename)
    #     sheet = workbook.add_worksheet()
    #     sheet.write(0, 0, "answerid")
    #     sheet.write(0, 1, "userid")
    #     sheet.write(0, 2, "itemid")
    #     sheet.write(0, 3, "questionid")
    #     sheet.write(0, 4, "useranswer")
    #     sheet.write(0, 5, "finishtime")
    #     r = 1
    #     for key,valuelist in tmpdict.iteritems():
    #         innerdict = valuelist[1]
    #         if innerdict.get(2,0) >= thres or innerdict.get(10,0) >=thres:
    #             print key
    #             continue
    #         for keylist in valuelist[0]:
    #             sheet.write(r, 0, keylist[0])
    #             sheet.write(r, 1, keylist[1])
    #             sheet.write(r, 2, keylist[2])
    #             sheet.write(r, 3, keylist[3])
    #             sheet.write(r, 4, keylist[4])
    #             sheet.write(r, 5, keylist[5])
    #             r+=1
    #     print "finished: " + filename
    #     workbook.close()

if __name__ == "__main__":
    readxml()
    # createDailyFloder()
    # getTask1()
    #
    # schedule.every().day.at("00:30").do(getTask1)
    # schedule.every().day.at("00:02").do(createDailyFloder)
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)