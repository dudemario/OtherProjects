import requests
url = "https://apisb.rbc.com/PersonalBanking/BranchSession/createSession"
auth = ("pYbJAET7Yy4yuwj8LblnBvrs8i63sb8f", "nMh0yGiBpQB6YAfH")
r = requests.get(url, auth=auth)
sessionId = eval(r.text)["result_content"]
#sessionId = r.text[1:-1].split(",")[1].split(u':')[1]
search = raw_input()
data = {"session_id":sessionId,"search":search,"max":1}
url = "https://apisb.rbc.com/PersonalBanking/BranchLocator/findBranches"
r = requests.get(url, auth=auth, data=data)
dates = {0:"Sun",
         1:"Mon",
         2:"Tue",
         3:"Wed",
         4:"Thurs",
         5:"Fri",
         6:"Sat",
         }
results = eval(r.text)["result_content"]["params"]

'''
minDist = 99999999999
closest = ""
for i in xrange(1,6):
    try:
        if results["altDistance"+str(i)] < minDist:
            minDist = results["altDistance"+str(i)]
            closest = results["altName"+str(i)]
    except(KeyError):
        pass

print "Closest Branch: "+ closest
'''

for i in xrange(1,6):
    try:
        print "Name: " + results["altName"+str(i)]
        print "Address: " + results["altAddressA"+str(i)]+", "+results["altCity"+str(i)]+", "+results["altPostalCode"+str(i)]
        url = "https://maps.googleapis.com/maps/api/directions/json?origin="+search+"&destination="+"+".join(results["altAddressA"+str(i)].split(" "))+"&key=AIzaSyAcyu2lyjW8Pl-cvR_muF0I4kswcPOCMoc"
        #url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=AIzaSyAcyu2lyjW8Pl-cvR_muF0I4kswcPOCMoc"
        r = requests.get(url)
        print (eval(r.text))
        rDist = eval(r.text)["routes"][0]["legs"][0]["distance"]["text"]
        rTime = eval(r.text)["routes"][0]["legs"][0]["duration"]["text"]
        print "Distance: " + rDist
        print "Time to Travel: " + rTime
        print ("Distance: " + results["altDistance"+str(i)])
        for key in dates:
            try:
                print("Hours on " + dates[key] + ": " + results["altHours"+dates[key]+str(i)])
            except (KeyError):
                pass
    except (KeyError):
        break

