import time

class TestMaker:

  def __init__(self, requestSender, region, instanceId, burstFreq):
    self.requestSender = requestSender
    self.region = region
    self.instanceId = instanceId
    self.burstFreq = burstFreq
    self.burstSequenceNumber = 0

  def __makeValue(self,
    requestSequenceNumber,
    indexInBurst,
    eventsPerBurst,
    requestsPerBurst,
    burstSequenceNumber):
    import uuid
    params = {
      "timestamp": int(time.time()),
      "source_region": self.region,
      "instance_id": self.instanceId,
      "request_sequence_number": requestSequenceNumber,
      "burst_sequence_number": burstSequenceNumber,
      "index_in_burst": indexInBurst,
      "burst_freq": self.burstFreq,
      "events_per_burst": eventsPerBurst,
      "requests_per_burst": requestsPerBurst,
      "event_guid": str(uuid.uuid4())
    }
    return params

  def sendGetTestv1(self, numRequests, currentRequests, burstSequenceNumber):
    for index in range(numRequests):
      import json
      values = json.dumps(
        self.__makeValue(
          currentRequests + index,
          index,
          numRequests,
          numRequests,
          burstSequenceNumber))
      self.requestSender.sendGetRequest({
        "key": "testing.eventing_beacon_single_get",
        "value": values})
       
  def sendPostTestv1(self, numRequests, currentRequests, burstSequenceNumber):
    for index in range(numRequests):
      values = self.__makeValue(
        currentRequests + index,
        index,
        numRequests,
        numRequests,
        burstSequenceNumber)
      self.requestSender.sendPostRequest({
        "key": "testing.eventing_beacon_single_post",
        "value": values})
     

  def sendBatchTestv1(self, numRequests, numPerBatch, currentRequests, burstSequenceNumber):
    for index in range(numRequests):
      batchEnvelope = {"client" : "eventing_test"}
      requests = []
      for batchIndex in range(numPerBatch):
        values = self.__makeValue(
          currentRequests + index,
          batchIndex + index * numPerBatch,
          numRequests * numPerBatch,
          numRequests,
          burstSequenceNumber)
        values['batchIndex'] = batchIndex
        requests.append({
          "timestamp": int(time.time()),
          "key": "testing.eventing_beacon_batch_post",
          "value": values})
      batchEnvelope["events"] = requests
      self.requestSender.sendBatchPostRequest(batchEnvelope)
 
  def __makeV2Event(self, key, value):
    import uuid
    import json
    return {
      "key": key,
      "value": json.dumps(value),
      "clientType": "web",
      "url": "this_is_not_a_url",
      "app": "phoenix",
      "cookieId": "cookieId",
      "referrerUrl": "referrerUrl",
      "guid": str(uuid.uuid4()),
      "visitId": str(uuid.uuid4()),
      "clientVersion": "testClientVersion"
    }

  def sendGetTestv2(self, numRequests, currentRequests, burstSequenceNumber):
    for index in range(numRequests):
      values = self.__makeValue(
          currentRequests + index,
          index,
          numRequests,
          numRequests,
          burstSequenceNumber)
      self.requestSender.sendGetRequestV2(
        self.__makeV2Event("testing.eventing_v2_beacon_single_get", values))
 
  
  def sendPostTestv2(self, numRequests, currentRequests, burstSequenceNumber):
    for index in range(numRequests):
      values = self.__makeValue(
        currentRequests + index,
        index,
        numRequests,
        numRequests,
        burstSequenceNumber)
      self.requestSender.sendPostRequestV2(
        self.__makeV2Event("testing.eventing_v2_beacon_single_post", values)) 

  def sendBatchTestv2(self, numRequests, numPerBatch, currentRequests, burstSequenceNumber):   
    for index in range(numRequests):
      batchEnvelope = {
        "app" : "phoenix",
        "clientType" : "web",
        "cookieId": "this is not a cookieId",
        "clientVersion" : "clientVersion"}
      requests = []
      for batchIndex in range(numPerBatch):
        import uuid
        values = self.__makeValue(
          currentRequests + index,
          batchIndex + index * numPerBatch,
          numRequests * numPerBatch,
          numRequests,
          burstSequenceNumber)
        values['batchIndex'] = batchIndex
        requests.append({
          "clientTimestamp": int(time.time()),
          "key": "testing.eventing_v2_beacon_batch",
          "value": values,
          "guid" : str(uuid.uuid4()),
          "visitId": str(uuid.uuid4()),
          "url": "this is not a url"})
      batchEnvelope["events"] = requests
      self.requestSender.sendBatchPostRequestV2(batchEnvelope)
 
