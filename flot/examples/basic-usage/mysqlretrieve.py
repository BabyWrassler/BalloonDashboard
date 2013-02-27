#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

import urllib2

import cgitb
cgitb.enable()
import cgi
import json

def getPage():
    url="http://localhost/jsondatasingle.py"
 
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()

con = None

namesPage = getPage()
#print namesPage
jsonData = json.loads(namesPage[:len(namesPage)-1])

try:
    con = mdb.connect('localhost', 'root', 'bubbles', 'balloon');
    cur = con.cursor()

#    i=1
#    cur.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (jsonData[i]['timestamp'],jsonData[i]['latitude'],jsonData[i]['longitude'],jsonData[i]['altitude'],jsonData[i]['gxaxis'],jsonData[i]['gyaxis'],jsonData[i]['gzaxis'],jsonData[i]['axaxis'],jsonData[i]['ayaxis'],jsonData[i]['azaxis'],jsonData[i]['mxaxis'],jsonData[i]['myaxis'],jsonData[i]['mzaxis'],jsonData[i]['pressure'],jsonData[i]['temp'],jsonData[i]['humidity']))
#    con.commit()

    cur.execute('select * from data order by time desc limit 10')
    rows = cur.fetchall()
#    for row in rows:
#        print row[0]

except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()

#print "Timestamp: ", jsonData[i]['timestamp'], "."

template =  "<!DOCTYPE html>\n"
#print template
template += "<html><head><title>Basic Flot Graph</title>\n"
template += "<link href='../examples.css' rel='stylesheet' type='text/css'>\n"
#template += "<!--[if lte IE 8]><script language='javascript' type='text/javascript' src='../../excanvas.min.js'>$"
template += "<script language='javascript' type='text/javascript' src='../../jquery.js'></script>\n"
template += "<script language='javascript' type='text/javascript' src='../../jquery.flot.js'></script>\n"
template += "<script type='text/javascript'>\n"

template += "$(function() {\n var d1 = ["
for row in rows:
    template += "["
    template += "1"#str(row[0])
    template += ","
    template += "2"#str(row[3])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#altchart", [ d1 ]); });\n'

template += "$(function() {\n var d1 = ["
for row in rows:
    template += "["
    template += str(row[0])
    template += ","
    template += str(row[13])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#preschart", [ d1 ]); });\n'

template += "$(function() {\n var d1 = ["
for row in rows:
    template += "["
    template += str(row[0])
    template += ","
    template += str(row[14])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#tempchart", [ d1 ]); });\n'

template += "$(function() {\n var d1 = ["
for row in rows:
    template += "["
    template += str(row[0])
    template += ","
    template += str(row[15])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#humchart", [ d1 ]); });\n'


template += "</script>\n"
template += "</head><body>\n"
template += '<div id="content">\n'

template += '<div class="demo-container">\n'
template += '<div id="header"><h2>Altitude</h2></div>\n'
template += '<div id="altchart"></div>\n'
template += '</div>\n'

template += '<div class="demo-container">\n'
template += '<div id="header"><h2>Pressure</h2></div>\n'
template += '<div id="preschart"></div></div>\n'
template += '</div>\n'

template += '<div class="demo-container">\n'
template += '<div id="header"><h2>Temperature</h2></div>\n'
template += '<div id="tempchart"></div></div>\n'
template += '</div>\n'

template += '<div class="demo-container">\n'
template += '<div id="header"><h2>Humidity</h2></div>\n'
template += '<div id="humchart"></div>\n'
template += '</div>\n'

template += '</div>\n'


#template += namesPage # Last row added to mysql database
template += "</body></html>\n"

print template
