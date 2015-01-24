import RequestSender
import TestMaker
import time
import uuid
import datetime

log = open("log","w")
instanceId = str(uuid.uuid1()) 
requestsPerBurst = 1
numEventsPerBurst = 1
burstNumber = 0

while(1):
#  sender = RequestSender.RequestSender(
#    "http://localhost:9000/info",
#    "http://localhost:9000/infoBatch",
#    "http://localhost:9000/info.v2",
#    "http://localhost:9000/infoBatch.v2",
#    log)

  #sender = RequestSender.RequestSender(
  #  "https://eventing.coursera.org/info",
  #  "https://eventing.coursera.org/infoBatch",
  #  "https://eventing.coursera.org/info.v2",
  #  "https://eventing.coursera.org/infoBatch.v2",
  #  log)
  tester = TestMaker.TestMaker(sender, "US", instanceId, 1)
  #tester.sendGetTestv1(
  #  numEventsPerBurst,
  #  burstNumber * numEventsPerBurst,
  #  burstNumber)
  #tester.sendPostTestv1(
  #  numEventsPerBurst,
  #  burstNumber * numEventsPerBurst,
  #  burstNumber)
  #tester.sendBatchTestv1(
  #  requestsPerBurst,
  #  numEventsPerBurst,
  #  burstNumber * requestsPerBurst,
  #  burstNumber)
  #tester.sendGetTestv2(
  #  numEventsPerBurst,
  #  burstNumber * numEventsPerBurst,
  #  burstNumber)
  #tester.sendPostTestv2(
  #  numEventsPerBurst,
  #  burstNumber * numEventsPerBurst,
  #  burstNumber) 
  tester.sendBatchTestv2(
    requestsPerBurst,
    numEventsPerBurst,
    burstNumber * requestsPerBurst,
    burstNumber
  )
  currentTime = datetime.datetime.today()
  nextWakeUp = datetime.datetime(
    currentTime.year,
    currentTime.month,
    currentTime.day,
    currentTime.hour + 1)
  log.write("Finished burst: " + str(burstNumber) + " at time:" + str(currentTime) +" \n")
  burstNumber += 1 
  time.sleep((nextWakeUp-currentTime).seconds)


