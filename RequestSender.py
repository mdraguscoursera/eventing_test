import requests

class RequestSender:

  def __init__(self, endPoint, endPointBatch, logFile):
    self.endPoint = endPoint
    self.logFile = logFile
    self.endPointBatch = endPointBatch


  def checkResponse(self, response):
    print(response.url)
    if response.status_code != 200: 
      self.logFile.write("Error on request: with url" + response.url + " Status code " + response.status_code + " with content" + response.content + "\n")
    else:
      self.logFile.write("Successful request with url" + response.url + "\n")
 

  def sendGetRequest(self, parameters):
    r = requests.get(self.endPoint, params = parameters)
    self.checkResponse(r)

  def sendPostRequest(self, parameters):
    r = requests.get(self.endPoint, params = parameters)
    self.checkResponse(r)

  def sendBatchPostRequest(self, parameters):
    r = requests.post(self.endPointBatch, params = parameters)
    self.checkResponse(r) 
    


