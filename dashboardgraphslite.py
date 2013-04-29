#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as db
#import MySQLdb as mdb
import sys
import time

import cgitb
cgitb.enable()
import cgi

def openDB():
  global con
  DB_FILENAME = "/home/pi/10DOFii/10DOF_data.db"
  con = db.connect(DB_FILENAME)

openDB()

try:
  cur = con.cursor()
  cur.execute('select * from Sensors order by TimeG desc limit 10')
  rows = cur.fetchall()
  #for row in rows:
  #   print row[3]

except db.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    if con:    
        con.close()


template =  "<!DOCTYPE html>\n"
template += "<html><head><title>All Graphs</title>\n"
template += "<link href='styles.css' rel='stylesheet' type='text/css'>\n"
#template += "<!--[if lte IE 8]><script language='javascript' type='text/javascript' src='flot/excanvas.min.js'>$"
template += "<script language='javascript' type='text/javascript' src='flot/jquery.js'></script>\n"
template += "<script language='javascript' type='text/javascript' src='flot/jquery.flot.js'></script>\n"
template += "<script language='javascript' type='text/javascript' src='flot/jquery.flot.time.js'></script>\n"
template += "<script type='text/javascript'>\n"

# Magnetometer Heading Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[12])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d2 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[13])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d3 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[14])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#headingchart", [ {data: d1, lines: { show: true }, points: { show: false }},'
template += '{data: d2, lines: { show: true}, points: { show: false}},'
template += '{data: d3, lines: { show: true}, points: { show: false}} ],'
template += ' {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Accelerometer Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[4])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d2 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[5])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d3 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[6])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#achart", [ {data: d1, lines: { show: true }, points: { show: false }},'
template += '{data: d2, lines: { show: true}, points: { show: false}},'
template += '{data: d3, lines: { show: true}, points: { show: false}} ],'
template += ' {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Gyroscope Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[15])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d2 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[16])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += "var d3 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[17])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#gyrochart", [ {data: d1, lines: { show: true }, points: { show: false }},'
template += '{data: d2, lines: { show: true}, points: { show: false}},'
template += '{data: d3, lines: { show: true}, points: { show: false}} ],'
template += ' {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# GPS Altitude Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[2])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#altgchart", [ {data: d1, lines: { show: true }, points: { show: false }} ] , {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Pressure Sensor's Altitude Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[20])
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#altpchart", [ {data: d1, lines: { show: true }, points: { show: false }} ] , {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Pressure Chart Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[19]) #20
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#preschart", [ d1 ] , {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Pressure Temperature Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[21]) #22
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#temppchart", [ d1 ] , {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# Gyroscope Temperature Data
template += "$(function() {\n var d1 = ["
for row in rows:
    hrMinSec = time.strptime(str(row[3]), "%Y-%m-%d %H:%M:%S")
    template += "["
    template += str((time.mktime(hrMinSec)*1000))
    template += ","
    template += str(row[18]) #19
    template += "],"
template = template[:(len(template)-1)]
template += "];\n"
template += '$.plot("#tempgchart", [ d1 ] , {xaxis: {mode: "time", timeformat: "%H:%M"}} ); });\n'

# HTML page
template += "</script>\n"
template += "</head><body>\n"
template += '<div id="content">\n'

template += '<div id="page-header"><h1>NSL-10 Data Dashboard</h1></div>'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>Map</h2></div>\n'
template += '<script type="text/javascript">he_track = "WJ3FF-2"; he_width = 330; he_height = 300;</script>'
template += '<script type="text/javascript" src="http://aprs.fi/js/embed.js"></script>\n'
template += '</div>\n'
# APRS.fi map embed options are at http://aprs.fi/page/embed
# Map updates automatically, does not need refresh. Charts do NOT update automatically.

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>Heading</h2></div>\n'
template += '<div id="headingchart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>Gyroscope</h2></div>\n'
template += '<div id="gyrochart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>Accelerometer</h2></div>\n'
template += '<div id="achart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>Pressure</h2></div>\n'
template += '<div id="preschart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>P Temperature</h2></div>\n'
template += '<div id="temppchart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>G Temperature</h2></div>\n'
template += '<div id="tempgchart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>P Altitude</h2></div>\n'
template += '<div id="altpchart"></div>\n'
template += '</div>\n'

template += '<div class="chart-container">\n'
template += '<div id="header"><h2>GPS Altitude</h2></div>\n'
template += '<div id="altgchart"></div>\n'
template += '</div>\n'

template += '</div>\n'

template += "</body></html>\n"

print template
