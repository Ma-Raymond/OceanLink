import random
import time

def UltDistSens(NearOrFar,radius,Dlong,Dlat,speed):
  object_list = ['Whale','Sunken Ship','Glacier','Megaladon','Another Ship','School of Fish', 'big rock']
  
  weights = random.choices(object_list, weights=(30, 10, 30, 10, 50, 50, 50,), k=1)
  while True:
    if (NearOrFar == "near"):
      if (int(speed) >= 80):
        
        return str(' '.join(weights)) + " has been found within a radius of " +str(radius)+ "km to you. SLOW DOWN IMMEDIATELY!!"
        
      else:
        return str(' '.join(weights)) + " has been found within a radius of " +str(radius)+ "km to you, remember to slow down."
     
    
    elif (NearOrFar == "far"):
      if (int(speed) >= 80):
        return str(' '.join(weights))+" has been found within a radius of" + str(radius) + "km around coordinates, Latitude: " + str(Dlat) + " and Longitude: " + str(Dlong) + "SLOW DOWN GRADUALLY."
      
      else:
        return str(' '.join(weights))+" has been found within a radius of" + str(radius) + "km around coordinates, Latitude: " + str(Dlat) + " and Longitude: " + str(Dlong)
     
  
    else:
      return "That was not a valid input, click on the detection module again."

def objectMain(distance,radius,lat,lon,speed):
    return(UltDistSens(distance,radius,lat,lon,speed))

#first input could be 'near' or 'far', if it is not either, user must retry 
#2nd input is radius distance in km
#3rd input is latitude input
#4th input is longitude