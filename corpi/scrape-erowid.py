#!/usr/bin/env python

# Adapted from https://github.com/longears/horsey-books/blob/master/scrape-erowid.py

# Fetch random Erowid experience reports and save them into the "text/" folder.
# Runs forever until you hit control-C to quit it

from __future__ import division

import os, sys, time, urllib2, random, re, glob


#-------------------------------------------------------------------------------------------
# HELPERS AND SETUP

def writeFile(fn,data):
    f = file(fn,'w'); f.write(data); f.close()

def removeHTML(s):
    htmlRegexes = ['</?.{1,30}?>']
    for htmlRegex in htmlRegexes:
        s = re.sub(htmlRegex, '', s)
    return s

baseurl = 'https://www.erowid.org/experiences/exp.php?ID=%s'
maxID = 67000
dir = 'text/'
if not os.path.exists(dir):
    os.mkdir(dir)


#-------------------------------------------------------------------------------------------
# MAIN

print '---------------------------------------------------------------------------------\\'
print
print 'Downloading random Erowid experience reports'
print
print 'Hit control-C to quit'
print
while True:
    print '-----'
    time.sleep(1)
    id = random.randint(1,maxID)
    url = baseurl % id

    if glob.glob('%s%s *.txt'%(dir,id)):
        print 'We already downloaded that one.  Skipping.'
        continue

    print 'Fetching url: %s'%url
    page = urllib2.urlopen(url).read()

    if 'Unable to view experience ' in page:
        print 'No report at that ID number.'
        continue

    fn = dir + 'erowid' + '_' + str(id) + '.txt'

    print 'Filename: %s'%fn

    # get main text and remove common unicode characters
    try:
        body = page.split('Start Body -->')[1].split('<!-- End Body')[0]
    except:
        body = page
    body = body.replace('\r','')
    body = body.replace('\x92',"'")
    body = body.replace('\x93','"')
    body = body.replace('\x94','"')
    body = body.replace('\x97',' -- ')
    body = removeHTML(body)
    body = body.strip()

    writeFile(fn, body)
