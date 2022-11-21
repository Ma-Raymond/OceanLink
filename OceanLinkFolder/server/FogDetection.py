import random

def rand_light_gen():
  # Create weighted random number generating system
  num = random.randint(-5, 1000)
  if num >= -5 and num <= 0:
    return -1
  elif num > 0 and num <=50:
    return (num / 2.5)
  elif num > 50 and num <= 125:
    return (((num - 50) / 7.5) + 10)
  elif num > 125 and num <= 275:
    return (((num - 125) / 15) + 20)
  else:
    return ((num - 275) / (77.5/7) + 30)
  
  

def vis_sensor(light_intensity, longitude, latitude):
  if light_intensity < 0:
    return "System Error"
  elif light_intensity <= 10:
    return "It is currently extremely dangerous to sail to the desired location (" + str(longitude) + ", " + str(latitude) + ") due to intense fog(" + str(round(100-light_intensity)) + "%). Please detour to the nearest port."
  elif light_intensity <= 20:
    return "It is currently dangerous to sail to the desired location (" + str(longitude) + ", " + str(latitude) + ") due to mild fog(" + str(round(100-light_intensity)) + "%). Please take extreme precautions or detour to the nearest port."
  elif light_intensity <= 30:
    return "It is currently risky to sail to the desired location (" + str(longitude) + ", " + str(latitude) + ") due to weak fog(" + str(round(100-light_intensity)) + "%). Please take appropriate safety precautions."
  else:
    return "It is safe to travel to the desired location (" + str(longitude) + ", " + str(latitude)+ ") with " + str(round(100-light_intensity)) + "% fog."


def fogMain(lon,lat):
    lightIntensity = rand_light_gen()
    return(vis_sensor(lightIntensity, lon, lat))