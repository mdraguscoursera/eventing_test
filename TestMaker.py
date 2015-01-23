class TestMaker:

  def __init__(self, requestSender, region, instanceId, burstFreq):
    self.requestSender = requestSender
    self.region = region
    self.instanceId = instanceId
    self.burstFreq = burstFreq
    self.burstSequenceNumber = 0

  def __makeValue(self, requestSequenceNumber, indexInBurst):
    import time
    params = {
      "timestamp": int(time.time()),
      "source_region": self.region,
      "insetance_id": self.instanceId,
      "request_sequence_number": requestSequenceNumber,
      "burst_sequence_number": self.burstSequenceNumber,
      "index_in_burst": indexInBurst,
      "burst_freq": self.burstFreq
    }
    return params

  def sendGetTestv1(self, numRequests, currentRequests):
    self.burstSequenceNumber += 1
    for index in range(numRequests):
      import json
      values = json.dumps(self.__makeValue(currentRequests + index, index))
      print(values)
      self.requestSender.sendGetRequest({"key": "testing.eventing_beacon_single_get", "value": values})
       
  



  

