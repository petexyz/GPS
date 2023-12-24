from gps3 import agps3
gps_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print(str(data_stream.time) + ', ' + str(data_stream.alt) + ', ' + str(data_stream.lat) + ', ' + str(data_stream.lon))
