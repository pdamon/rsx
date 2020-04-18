from adafruit_rplidar import RPLidar
from math import floor

PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)

print(lidar.info)

scan_data = [0]*360
for scan in lidar.iter_scans():
    for(_,angle, distance) in scan:
        scan_data[min([359, floor(angle)])] = distance
    break

with open("data.csv", "w+") as out:
    out.write("ANGLE, DISTANCE\n")
    for i in range(len(scan_data)):
        out.write("{}, {}\n".format(i, scan_data[i]))
out.close()
lidar.stop()
lidar.disconnect()
