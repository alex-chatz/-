
import urllib
import json

#zitaw imerominia
day = raw_input("Enter the day:")
month = raw_input("Enter the month:")
year = raw_input("Enter the year:")


#travaw ta dedomena
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+day+"-"+month+"-"+year+".json"
site = urllib.urlopen(url)
data = site.read()

draws =[]
jload = json.loads(data)
	
for i in range(0,len(jload["draws"]["draw"])):
	draws.append(jload["draws"]["draw"][i]["results"])

#vriskw tin sixnotita twn arithmwn
frequency = [0 for i in range(80)]
for i in range(0,len(draws)):
	for j in range(20):
		frequency[draws[i][j]-1] += 1
 #emfanizw tin sixnotita
for i in range(0,len(frequency)):
	if i < 9:		
		print "",i+1, ":", frequency[i]
	else:
		print i+1, ":", frequency[i]
		
print "These are the results for the date: "+day+"-"+month+"-"+year