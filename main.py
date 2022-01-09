import requests
import os
import time 

gre = "\033[1;32m"
ver = "\033[1;91m"

print(f"""{gre}
------------------------------
|By danieldev-usr            |
|IP or domain data extraction|
|/info for more informations |
------------------------------ """)

while True:
	print("  ")
	x = input("[IP/DOMAIN]>>> ")
	ip = requests.get(f'http://ip-api.com/json/{x}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query').json()
	
	if "message" not in ip:
		print(" ")
		print("|Task status: {}                 \n".format(ip["status"]))
		time.sleep(0.1)
		print("|Continent: {}               \n".format(ip["continent"]))
		time.sleep(0.1)
		print("|Continent code: {}                     \n".format(ip["continentCode"]))
		time.sleep(0.1)
		print("|Country: {}                 \n".format(ip["country"]))
		time.sleep(0.1)
		print("|Country code: {}                      \n ".format(ip["countryCode"]))
		time.sleep(0.1)
		print("|Region: {}                            \n ".format(ip["region"]))
		time.sleep(0.1)
		print("|Region name: {}                    \n".format(ip["regionName"]))
		time.sleep(0.1)
		print("|City: {}                           \n".format(ip["city"]))
		time.sleep(0.1)
		print("|District: {}                          \n".format(ip["district"]))
		time.sleep(0.1)
		print("|Zip: {}                                 \n".format(ip["zip"]))
		time.sleep(0.1)
		print("|Lat: {}                                \n ".format(ip["lat"]))
		time.sleep(0.1)
		print("|Lon: {}                               \n ".format(ip["lon"]))
		time.sleep(0.1)
		print("|Timezone: {}               \n".format(ip["timezone"]))
		time.sleep(0.1)
		print("|Offset: {}                  \n ".format(ip["offset"]))
		time.sleep(0.1)
		print("|Currency: {}             \n".format(ip["currency"]))
		time.sleep(0.1)
		print("|Isp: {}                       \n".format(ip["isp"]))
		time.sleep(0.1)
		print("|Org: {}                    \n ".format(ip["org"]))
		time.sleep(0.1)
		print("|As: {}                      \n ".format(ip["as"]))
		time.sleep(0.1)
		print("|Asname: {}            \n ".format(ip["asname"]))
		time.sleep(0.1)
		print("|Reverse: {}             \n".format(ip["reverse"]))
		time.sleep(0.1)
		print("|Mobile: {}               \n".format(ip["mobile"]))
		time.sleep(0.1)
		print("|Proxy: {}                  \n".format(ip["proxy"]))
		time.sleep(0.1)
		print("|Hosting: {}               \n".format(ip["hosting"]))
		time.sleep(0.1)
		print("|Query: {}                 \n ".format(ip["query"]))
	
	
	elif x == "/info":
		print(f"{ver}   ")
		print("API: http://ip-api.com")
		print("Creator: @daniewkiwi (ig)")
		print("Bugs or feedbacks (ig)")
		print(f"{gre}    ")
	
	else:
		print("[Red alert]: IP or Domain incorrect..!")