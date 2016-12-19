# This is a script to scrape youtube comments for number values
# for a given youtube video id,
# and compile them in an Excel-viewable .csv.


import re, os, io, json, requests
import html
import time

#Put your key here
api_key = "lolidk"

#Mooer Pedal contest video
video_id = "FOw7ViIp25A"

iNumRequests=1;
iNumMaxResults=100;
iMaxIndividualWeight=400;
bNextPage = False
#Initial request

#https://www.youtube.com/watch?v=FOw7ViIp25A
r = requests.get('https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=' + video_id + '&maxResults=' + str(iNumMaxResults) + '&key=' +api_key)

r.raise_for_status()

path_to_script = os.path.dirname(os.path.abspath(__file__))
my_filename = os.path.join(path_to_script, "_Comments")


with open(my_filename+".csv", "w+") as handle:
	print("Author,Comment,Guesses", file=handle)


while True:
	print("Page " + str(iNumRequests) + " of comments:")
	print("\t"+str(len(r.json()["items"])) + " result(s)\t", end="", flush=True)
	
	
	if "nextPageToken" not in r.json():
		print("\n***Last Page***")
		bNextPage = False;
	else:
		nextPageToken = r.json()["nextPageToken"]
		bNextPage = True;
		iNumRequests+=1




	for i in range(0, len(r.json()["items"])):

		if (i == int((len(r.json()["items"])/3))) or (i == int((2*len(r.json()["items"]))/3)):
			print('.', end="", flush=True)
		elif (i==(len(r.json()["items"])-1)):
			print('.')
	
		#Grab author, encode, remove comments for csv
		author = r.json()["items"][i]["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
		sEncodedAuthor = author.encode('ascii', 'replace')
		csvLine = sEncodedAuthor.decode('utf-8').replace(',','<comma>')+","
		
		#Grab comment content, encode, escape html values.
		sComment = r.json()["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]	
		sEncodedComment = sComment.encode('ascii', 'replace')
		sParsed = html.unescape(sEncodedComment.decode('utf-8'))
		sParsed = sParsed.replace('<br />', '\\n')
		csvLine += "\""+sParsed.replace(',','<comma>')+"\""+","

		#Parse any 3 digit numbers exceeding individual weights
		lNumberList = re.findall("\d{3}", sParsed)
		for Number in lNumberList:
			if int(Number) >= iMaxIndividualWeight:
				csvLine += Number
				break

		with open(my_filename+".csv", "a") as handle:
			print(csvLine, file=handle)

		
	if bNextPage == False:
		break;
	else:
		r = requests.get('https://www.googleapis.com/youtube/v3/commentThreads?pageToken=' + nextPageToken + '&part=snippet&videoId=FOw7ViIp25A&maxResults=' + str(iNumMaxResults) + '&key=' +api_key)
		r.raise_for_status()
		
print("Execution Completed.")
