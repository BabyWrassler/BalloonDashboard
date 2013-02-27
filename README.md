BalloonDashboard
================

Python and MySQL used to create an HTML dashboard for a near-space balloon carrying a Raspberry Pi.

The RPi will run a Python script that reads the sensors, averages the data, and writes it to an XML
file and a MySQL database. The dashboardgraphs.py file in this repo will be served by the RPi to 
computers on the ground. It reads the data back out of the MySQL database and graphs it.
