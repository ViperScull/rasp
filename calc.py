import math

RADIUS = 6378137
RADIUS_POLAR = 6356752.31424518
E_SQUARE = 0.00669437999014115997
E2_SQUARE = 0.00673949674227627581

def calculateXYZ(lat, lon, h):
	lat = lat*math.pi/180
	lon = lon*math.pi/180
	N = RADIUS/math.sqrt(1-E_SQUARE*math.sin(lat)*math.sin(lat))

	X = (N+h)*math.cos(lat)*math.cos(lon)
	Y = (N+h)*math.cos(lat)*math.sin(lon)
	Z = (N*RADIUS_POLAR*RADIUS_POLAR/RADIUS/RADIUS + h)*math.sin(lat)
	
	return(X,Y,Z)

def calculateLLA(X,Y,Z):
	p = math.sqrt(X*X + Y*Y)
	teta = math.atan2(Z*RADIUS,p*RADIUS_POLAR)
		
	lon = math.atan2(Y,X)
	lat = math.atan2(Z+E2_SQUARE*RADIUS_POLAR*math.pow(math.sin(teta),3),p-E_SQUARE*RADIUS*math.pow(math.cos(teta),3))
	N = RADIUS/math.sqrt(1-E_SQUARE*math.sin(lat)*math.sin(lat))
	h = p/math.cos(lat) - N
	lat = lat*180/math.pi
	lon = lon*180/math.pi
	
	return(lat,lon,h)

	



