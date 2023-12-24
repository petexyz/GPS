import os
import time
from gps3 import agps3

gps_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()

file = 'gps-output.txt'

if os.path.exists(file):
 os.remove(file)

f = open (file, 'w')

gps_socket.connect()
gps_socket.watch()

for new_data in gps_socket:
 if new_data:
  data_stream.unpack(new_data)
		
  if data_stream.time == 'n/a':
   continue

  print(str(data_stream.time) + ', ' + str(data_stream.alt) + ', ' + str(data_stream.lat) + ', ' + str(data_stream.lon))
  f.write(str(data_stream.time) + ', ' + str(data_stream.alt) + ', ' + str(data_stream.lat) + ', ' + str(data_stream.lon))
  f.write("\n")
  time.sleep(2)
        
