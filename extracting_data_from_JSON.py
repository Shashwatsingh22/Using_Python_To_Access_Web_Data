import urllib.request,urllib.parse,urllib.error
import json

main_url=input("Enter location: ")
print("Retrieving",main_url)
ur_cap=urllib.request.urlopen(main_url)
data=ur_cap.read().decode()
print("Retrieved",len(data),"characters")
js=json.loads(data)    

s_sum=0
count=0
for u in js["comments"]:
    s_sum=s_sum+u["count"]
    count=count+1

print("Count:",count)
print("Sum:",s_sum)