#!/usr/bin/python
# -*- coding: utf8 -*-

import time
import MySQLdb as mysql
import sys

db = mysql.connect(user="root",passwd="212331",db="memory",host="localhost")
db.autocommit(True)
cur = db.cursor()
def getMem():
   with open('/proc/meminfo') as f:
       total =  int(f.readline().split()[1])   
       free =  int(f.readline().split()[1])   
       buffers =  int(f.readline().split()[1])   
       cache =  int(f.readline().split()[1])   
   mem_use = total-free-buffers-cache
   t = int(time.time())
   sql = 'insert into memory (memory,time) value (%s,%s)'%(mem_use/1024,t)
   cur.execute(sql)
   m = open('/tmp/monit.log','a+')
   old=sys.stdout
   sys.stdout=m
   print 'ok'
   sys.stdout=old
while True:
    time.sleep(3)
    getMem()
