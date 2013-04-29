#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as db
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
  cur.execute('select * from Sensors order by TimeG desc limit 1')
  rows = cur.fetchall()

except db.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    if con:    
        con.close()


template =  "<!DOCTYPE html>\n"
template += "<html><head><title>Station ID</title>\n"
template += "<link href='styles.css' rel='stylesheet' type='text/css'>\n"
template += "</head><body>\n"

template += '<div id="content">\n'

# ENTER CALL SIGN HERE:
template += '<div id="page-header"><h1>WJ3FF-3</h1></div>'

template += '<img id="idimage" src="latest.jpg">'

template += '<div id="statbox">'

template += "<h2>NSL-10</h2>"

template += '<p id="odd">Time: '
template += (rows[0][3])[11:] # Chopping off date
template += "</p>\n"

template += '<p id="even">B Alt: '
template += str(rows[0][20])
template += "</p>\n"

template += '<p id="odd">GPS Alt: '
template += str(rows[0][2])
template += "</p>\n"

template += '<p id="even">Lat: '
template += (str(rows[0][0]))[:8] # Truncating
template += "</p>\n"
template += '<p id="odd">Long: '
template += (str(rows[0][1]))[:8] # Truncating
template += "</p>\n"

template += '<p id="even">Pressure: '
template += str(rows[0][19])
template += "</p>\n"

template += '<p id="odd">P Temp: '
template += str(rows[0][21])
template += "</p>\n"

template += '<p id="even">G Temp: '
template += str(rows[0][18])
template += "</p>\n"

template += "</div>"

template += '</div>\n'

template += "</body></html>\n"

print template
