from imgRecognize import CVision
from dronekit import connect, VehicleMode, LocationGlobalRelative, time
from GoPro import GoPro
import math

# Coordinates of the SB flying club
SB_Lat = 41.519205
SB_Lon = -86.239949
connection_string = "/dev/ttyUSB0,57600"
target_altitude = 30 # flight altitude in meters

def create_vehicle():
	# Connect to the Vehicle. 
	#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
	print "\nConnecting to vehicle on: %s" % connection_string
	vehicle = connect(connection_string, wait_ready=True)


	print "Arming motors"
	# Copter should arm in GUIDED mode
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True    

	# Confirm vehicle armed before attempting to take off
	      
	
	print "Taking off!"
	vehicle.simple_takeoff(target_altitude) # Take off to target altitude
	# Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
	#  after Vehicle.simple_takeoff will execute immediately).

	print "Altitude: %s" %vehicle.location.global_relative_frame.alt

	aTargetAltitude = 30
	while True:
	    print " Altitude: ", vehicle.location.global_relative_frame.alt 
	    #Break and return from function just below target altitude.        
	    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
	        print "Reached target altitude"
	        break
	    time.sleep(1)

	return vehicle

if __name__ == "__main__":

        #time.sleep(30)
	vehicle = create_vehicle()
	photo_location = LocationGlobalRelative(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, 30)
	vehicle.simple_goto(photo_location)

	dist = get_distance_metres(vehicle.location.global_frame, photo_location)
	while(dist > 2):
		print "Distance To Location:", dist
		time.sleep(3)
		dist = get_distance_metres(vehicle.location.global_frame, photo_location)
	print "Arrived At Photo Location"

	##############################################################################################
	# TAKE PHOTO - At this point, drone should be hovering 30 metres above the specificed location
	##############################################################################################
	go = GoPro()
	go.take_picture()
	# Dowloads into the file "localPicture.jpg"
	go.download_photo()
	##############################################################################################
	# Pass Photo To Image Recognition
	##############################################################################################
	vision = CVision('./localPicture.png', './imgRecognize/target.jpg')
        print vision.find_image()
	lat, lon = vision.get_coordinates(target_altitude, vehicle.location.global_frame) # pass in vehicle.location
        

	open_spot_location = LocationGlobalRelative(float(lat), float(lon), 10)
	vehicle.simple_goto(open_spot_location)
	dist = float(get_distance_metres(vehicle.location.global_frame, open_spot_location))
	while(float(dist) > 5):
		print "Distance To Open Spot:", dist
		time.sleep(3)
		float(dist = get_distance_metres(vehicle.location.global_frame, open_spot__location))
	print "Arrived At Open Spot"
	#time.sleep(30)

	vehicle.mode = VehicleMode("LAND")
	time.sleep(10)
	vehicle.close()

	print("Program Complete")
