# read the data from the URL and print it
import urllib.request
# open a connection to a URL using urllib
URL='https://www.gtu.ac.in'
webUrl  = urllib.request.urlopen(URL)

# read the data from the URL and print it
data = webUrl.read()
print ("(a):Source Code",data)

print("(b):Url",URL)
print("(c):Header",webUrl.headers)
#get the result code and print it
print ("(d):Status code: " + str(webUrl.getcode()))



