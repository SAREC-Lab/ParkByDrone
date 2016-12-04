from imgRecognize import CVision
from dronekit import connect, VehicleMode, LocationGlobalRelative, time
# from GoPro import GoPro
import math

# Coordinates of the SB flying club
SB_Lat = 41.519205
SB_Lon = -86.239949
connection_string = "/dev/ttyUSB0,57600"
target_altitude = 30

def create_vehicle():
	# Connect to the Vehicle. 
	#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
	print "\nConnecting to vehicle on: %s" % connection_string
	vehicle = connect(connection_string, wait_ready=True, heartbeat_timeout=30 )

	vehicle.mode = VehicleMode("GUIDED")

	vehicle.wait_ready()

	# Get some vehicle attributes (state)
	print "Get some vehicle attribute values:"
	print " GPS: %s" % vehicle.gps_0
	print " Battery: %s" % vehicle.battery
	print " Last Heartbeat: %s" % vehicle.last_heartbeat
	print " Is Armable?: %s" % vehicle.is_armable
	print " System status: %s" % vehicle.system_status.state
	print " Mode: %s" % vehicle.mode.name    # settable
	print " Stable version %s" %vehicle.version.is_stable()
	print " Vehicle version %s" %vehicle.version


	print "Arming motors"
	# Copter should arm in GUIDED mode
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True    

	# Confirm vehicle armed before attempting to take off
	while not vehicle.armed:      
	    print " Waiting for arming..."
	    time.sleep(1)

	print "Taking off!"
	vehicle.simple_takeoff(3) # Take off to target altitude
	# Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
	#  after Vehicle.simple_takeoff will execute immediately).

	print "Altitude: %s" %vehicle.location.global_relative_frame.alt

	aTargetAltitude = 20
	while True:
	    print " Altitude: ", vehicle.location.global_relative_frame.alt 
	    #Break and return from function just below target altitude.        
	    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
	        print "Reached target altitude"
	        break
	    time.sleep(1)

	return vehicle

if __name__ == "__main__":

	vehicle = create_vehicle()
	photo_location = LocationGlobalRelative(SB_Lat, SB_Lon, 30)
	vehicle.simple_goto(photo_location)

	dist = get_distance_metres(vehicle.location.global_frame, photo_location)
	while(dist > 5):
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
	vision = CVision('./localPicture.jpg', './imgRecognize/target.JPG')
	lat, lon = vision.get_coordinates(target_altitude, vehicle.location.global_frame) # pass in vehicle.location


	open_spot_location = LocationGlobalRelative(lat, lon, 10)
	vehicle.simple_goto(open_spot_location)
	dist = get_distance_metres(vehicle.location.global_frame, open_spot_location)
	while(dist > 5):
		print "Distance To Open Spot:", dist
		time.sleep(3)
		dist = get_distance_metres(vehicle.location.global_frame, open_spot__location)
	print "Arrived At Open Spot"
	time.sleep(30)

	vehicle.mode = VehicleMode("LAND")
	time.sleep(10)
	vehicle.close()

	print("Program Complete")
