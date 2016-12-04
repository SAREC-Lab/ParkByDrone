from imgRecognize import CVision
from GoPro import GoPro
from dronekit import connect,VehicleMode, LocationGlobalRelative, time
go = GoPro()
go.take_picture()
# Dowloads into the file "localPicture.jpg"
go.download_photo()
        #######################################################################$
        # Pass Photo To Image Recognition
        #######################################################################$
vision = CVision('./localPicture.jpg', './imgRecognize/target.JPG')
test = LocationGlobalRelative(41.000,42.000,0)
lat, lon = vision.get_coordinates(target_altitude, test)
print lat
print lon

open_spot_location = LocationGlobalRelative(lat, lon, 10)

