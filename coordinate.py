import math

class coordinate(object):
	def __init__(self,lat,lon,h):
		self.lat = lat*math.pi/180
		self.lon = lon*math.pi/180
		self.h = h
	
	RADIUS = 6378137
	RADIUS_POLAR = 6356752.31424518
	E_SQUARE = 0.00669437999014115997
	E2_SQUARE = 0.00673949674227627581
	
	def calculateXYZ(self):
		N = self.RADIUS/math.sqrt(1-self.E_SQUARE*math.sin(self.lat)*math.sin(self.lat))

		X = (N+self.h)*math.cos(self.lat)*math.cos(self.lon)
		Y = (N+self.h)*math.cos(self.lat)*math.sin(self.lon)
		Z = (N*self.RADIUS_POLAR*self.RADIUS_POLAR/self.RADIUS/self.RADIUS + self.h)*math.sin(self.lat)
		
		return (X,Y,Z)
		
	def calculateLLA(self,X,Y,Z):
		p = math.sqrt(X*X + Y*Y)
		teta = math.atan2(Z*self.RADIUS,p*self.RADIUS_POLAR)

		lon = math.atan2(Y,X)
		lat = math.atan2(Z+self.E2_SQUARE*self.RADIUS_POLAR*math.pow(math.sin(teta),3),p-self.E_SQUARE*self.RADIUS*math.pow(math.cos(teta),3))
		N = self.RADIUS/math.sqrt(1-self.E_SQUARE*math.sin(lat)*math.sin(lat))
		h = p/math.cos(lat) - N
		lat = lat*180/math.pi
		lon = lon*180/math.pi

		return(lat,lon,h)
	
	def updateXYZ(self,X_p,Y_p,Z_p,x,y):
		X_q = -x*math.sin(self.lon) - y*math.cos(self.lon)*math.sin(self.lat) + X_p
		Y_q = x*math.cos(self.lon) - y*math.sin(self.lon)*math.cos(self.lat) + Y_p
		Z_q = x*math.cos(self.lat) + Z_p
		
		return (X_q,Y_q,Z_q)
	