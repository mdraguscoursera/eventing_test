import json
import requests
import logging


class RequestSender:

  def setupDebug(self):
    import requests
    import logging

    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    
    try:
      import http.client as http_client
    except ImportError:
      # Python 2
      import httplib as http_client
      http_client.HTTPConnection.debuglevel = 1
 
    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig() 
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
  
  def __init__(self, endPoint, endPointBatch, endPointV2, endPointBatchV2, logFile):
    self.endPoint = endPoint
    self.logFile = logFile
    self.endPointBatch = endPointBatch
    self.endPointV2 = endPointV2
    self.endPointBatchV2 = endPointBatchV2
    #self.setupDebug()

  def checkResponse(self, response):
    print(response.url)
    if response.status_code != 200: 
      self.logFile.write("Error on request: with url " + response.url + " Status code " + str(response.status_code) + " with content " + response.content + "\n")
 

  def sendGetRequest(self, parameters):
    r = requests.get(self.endPoint, params = parameters)
    self.checkResponse(r)

  def sendPostRequest(self, payload):
    r = requests.post(self.endPoint, data = payload)
    self.checkResponse(r)

  def sendBatchPostRequest(self, payload):
    import json
    headers = {"Content-Type": "application/json"}
    r = requests.post(self.endPointBatch, data = json.dumps(payload), headers = headers)
    self.checkResponse(r) 
    
  def sendGetRequestV2(self,parameters):
    headers = {
      "X-FORWARDED-FOR" : "192.0.0.1",
      "ACCEPT-LANGUAGE" : "en"
    }
    r = requests.get(self.endPointV2, params = parameters, headers = headers)
    self.checkResponse(r)
  
  def sendPostRequestV2(self, payload):
    headers = {
      "X-FORWARDED-FOR" : "192.0.0.1",
      "ACCEPT-LANGUAGE" : "en"
    }
    r = requests.post(self.endPointV2, data = payload, headers = headers)
    self.checkResponse(r)

  def sendBatchPostRequestV2(self, payload):
    import json
    headers = {
      "X-FORWARDED-FOR" : "192.0.0.1",
      "ACCEPT-LANGUAGE" : "en",
      "Content-Type": "application/json"
    }
    r = requests.post(self.endPointBatchV2, data = json.dumps(payload), headers = headers)
    self.checkResponse(r)



