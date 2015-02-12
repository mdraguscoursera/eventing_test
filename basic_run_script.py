import RequestSender
import TestMaker
import time
import uuid
import datetime

log = open("log","w")
instanceId = str(uuid.uuid4()) 
# this is only used for batch requests where the number
# of requests and the number of events differs
requestsPerBurst = 10 
numEventsPerBurst = 100
burstNumber = 0

while(1):
#  sender = RequestSender.RequestSender(
#    "http://localhost:9000/info",
#    "http://localhost:9000/infoBatch",
#    "http://localhost:9000/info.v2",
#    "http://localhost:9000/infoBatch.v2",
#    log)

  time.sleep(10)
  currentTime = datetime.datetime.now()
  sender = RequestSender.RequestSender(
    "https://eventing.coursera.org/info",
    "https://eventing.coursera.org/infoBatch",
    "https://eventing.coursera.org/info.v2",
    "https://eventing.coursera.org/infoBatch.v2",
    log)
  tester = TestMaker.TestMaker(sender, "US", instanceId, 1)
  try: 
    tester.sendGetTestv1(
      numEventsPerBurst,
      burstNumber * numEventsPerBurst,
      burstNumber)
    log.write("Finished GET V1\n")
    tester.sendPostTestv1(
      numEventsPerBurst,
      burstNumber * numEventsPerBurst,
      burstNumber)
    log.write("Finished POST V1\n")
    tester.sendBatchTestv1(
      requestsPerBurst,
      numEventsPerBurst / requestsPerBurst,
      burstNumber * requestsPerBurst,
      burstNumber)
    log.write("Finished BATCH V1\n")
    tester.sendGetTestv2(
      numEventsPerBurst,
      burstNumber * numEventsPerBurst,
      burstNumber)
    log.write("Finished GET V2\n")
    tester.sendPostTestv2(
      numEventsPerBurst,
      burstNumber * numEventsPerBurst,
      burstNumber) 
    log.write("Finished POST V2\n")
    tester.sendBatchTestv2(
      requestsPerBurst,
      numEventsPerBurst / requestsPerBurst,
      burstNumber * requestsPerBurst,
      burstNumber
    )
    log.write("Finished BATCH V2\n")
  except:
    print "Unexpected error:", sys.exc_info()[0]
  nextHour = currentTime + datetime.timedelta(hours=1)
  nextWakeUp = datetime.datetime(nextHour.year, nextHour.month, nextHour.day, nextHour.hour, 15)
  log.write("Finished burst: " + str(burstNumber) + " at time:" + str(currentTime) +" \n")
  log.flush()
  burstNumber += 1 
  time.sleep((nextWakeUp-currentTime).seconds)


