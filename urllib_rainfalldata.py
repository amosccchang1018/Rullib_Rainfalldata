# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:06:07 2018

@author: Chi
"""
import urllib.request
import datetime
from dateutil.relativedelta import relativedelta
import fnmatch  #用來找有沒有後綴是某個類型檔案的

filenames_mix = [];
filenames = [];
web_site = "ftp://ftp-cdc.dwd.de/pub/CDC/grids_germany/daily/evapo_p/"
web_data = urllib.request.urlopen(web_site).read().decode("utf-8")
filenames_mix = web_data.split('\n')
for i in filenames_mix: 
    filenames.append( i.strip().split(' '))

'''words2[4][16]
下載檔案 → 首先對要下載的點按右鍵知道他的網址
'''
firstmonth = datetime.date(1991, 1, 1)
minthnumbers_data = []
minthnumbers_data_num = []

for months in range(0,len(filenames)-4):
    minthnumbers_data.append(firstmonth + relativedelta( months =+ months ))
'''time to number'''
for i in minthnumbers_data:
    minthnumbers_data_num.append(i.strftime("%Y%m"))

for dates in minthnumbers_data_num:
    urllib.request.urlretrieve('ftp://ftp-cdc.dwd.de/pub/CDC/grids_germany/daily/evapo_p/grids_germany_daily_evapo_p_%s.tgz'
                               % dates
                               , 'grids_germany_daily_evapo_p_%s.tgz'% dates )  
print ("downloading with urllib")

