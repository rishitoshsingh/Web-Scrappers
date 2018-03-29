from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as Soup
req = Request("https://pubg.me/weapons/throwables", headers={"User-Agent": "Chrome/64.0.3282.186"})
urlClient = uReq(req)
html_page = urlClient.read()
urlClient.close()
page_soup = Soup(html_page,"html.parser")
data = page_soup.findAll("div",{"class":"card-block stat-comparison weapon-comparison"})
data_table = data[0]

filename = "Throwables.csv"
file = open(filename,"w")
headers = "Item,Image,Overview,Throw Time,Throw Cooldown Duration,Fire Delay,Activation Time Limit,Detonation,Explosion Delay,Pickup Delay,Ready Delay\n"
file.write(headers)

rows = data_table.findAll("div",{"class":"row"})

for index in range(0,4):
	
	if(index != 0):
		dex = index * 2
	else:
		dex = index

	item_string = ""

	colsA = rows[0].findAll("div",{"class":"col"})
	colsB = rows[1].findAll("div",{"class":"col"})
	colsC = rows[2].findAll("div",{"class":"col"})
	
	item = colsA[index].find("div",{"class":"item-header"}).h3.string
	img = colsA[index].find("div",{"class":"item-image-wrap"}).img["src"]
	image = img.replace(",","|")
	overview = colsA[index].find("div",{"class":"item-header"}).p.string

	item_string = item + "," + image + "," + overview + ","

	valRed = colsB[dex].findAll("div",{"class","value value-red"})
	if(len(valRed)>0):
		for tag in valRed:
			val = tag.find("i")
			_ = val.extract()
			tag["class"] = "value value-white"
	valGreen = colsB[dex].findAll("div",{"class","value value-green"})	
	if(len(valGreen)>0):
		for tag in valGreen:
			val = tag.find("i")
			_ = val.extract()		
			tag["class"] = "value value-white"

	values = colsB[dex].findAll("div",{"class","value value-white"})
	
	temp_str = ""
	for value in values:
		temp_str = temp_str + value.string
		temp_str = temp_str + ","
	
	item_string = item_string + temp_str


	valRed = colsC[index].findAll("div",{"class","value value-red"})
	if(len(valRed)>0):
		for tag in valRed:
			val = tag.find("i")
			_ = val.extract()
			tag["class"] = "value value-white"
	valGreen = colsC[index].findAll("div",{"class","value value-green"})	
	if(len(valGreen)>0):
		for tag in valGreen:
			val = tag.find("i")
			_ = val.extract()		
			tag["class"] = "value value-white"

	values = colsC[index].findAll("div",{"class","value value-white"})
	temp_str = ""
	for value in values:
		temp_str = temp_str + value.string
		temp_str = temp_str + ","

	item_string = item_string + temp_str
	length = len(item_string)
	string = item_string[0:length-1] + "\n"

	file.write(string)

file.close()
