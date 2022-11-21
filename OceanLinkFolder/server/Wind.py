import random

windSpeeds = []
for i in range(0, 7, 1):
  windSpeeds.append(random.randint(0, 87))
  windSpeeds.append(random.randint(0, 87))
  windSpeeds.append(random.randint(0, 128))

windSpeeds.append("null")
previousSpeed = windSpeeds[random.randint(0, len(windSpeeds) - 1)]


def getWindSpeed(prevSpeed):
  #simulating a wind sensor by generating values
  if prevSpeed == "null":
    speed = "null"
    return speed

  else:
    changes = [1, 2, 1, 3, 4, 1, 2, -1, -2, -3, -1, -2, -2, -4, 0, 0, 0, 0, 0]
    newSpeed = prevSpeed + changes[random.randint(0, len(changes) - 1)]
    speeds = []
    for i in range(0, 50, 1):
      speeds.append(newSpeed)

    speeds.append("null")
    speed = speeds[random.randint(0, len(speeds) - 1)]
    if speed == "null":
      return speed
    elif (speed < 0):
      speed = speed * -1
    return speed


def windDetection(oldSpeed, windSensorWorking):
  windSpeed = getWindSpeed(oldSpeed)
  if windSpeed == "null":
    windSensorWorking = False

  if windSensorWorking:
    #print(windSpeed)
    if (windSpeed >= 0 and windSpeed <= 19):
      return [
        "Wind Speed is " + str(windSpeed) +
        " km/h, little to no wind. No Danger", windSpeed
      ]

    elif (windSpeed >= 20 and windSpeed <= 50):
      return [
        "Wind Speed is " + str(windSpeed) + " km/h, strong breeze. Be Careful",
        windSpeed
      ]

    elif (windSpeed >= 51 and windSpeed <= 87):
      return [
        "Wind Speed is " + str(windSpeed) +
        " km/h, very strong winds. Potentially Dangerous", windSpeed
      ]

    else:
      return [
        "Wind Speed is " + str(windSpeed) +
        " km/h, you're in a storm! Extremely Dangerous", windSpeed
      ]

  else:
    return ["Wind Sensor Broken! Send Someone to repair it!", windSpeed]

def windMain():
    result = windDetection(previousSpeed, True)
    result = windDetection(result[1], True)
    return(result) # First comment vs second is speed