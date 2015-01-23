import RequestSender
import TestMaker


f = open("log","w")
sender = RequestSender.RequestSender("https://eventing.coursera.org/info", "https://eventing.coursera.org/infoBatch", f)


tester = TestMaker.TestMaker(sender, "US", "instanceId", 1)

tester.sendGetTestv1(100,0)




