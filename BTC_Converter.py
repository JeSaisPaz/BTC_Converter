import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
btc = response.json()
optionmenu = input("""
*-*-*-*-*-*-*-*-*
  Menu actions:
!help
!convert
*-*-*-*-*-*-*-*-*
Command >
""")

if optionmenu == "!help":
	print("""
*-*-*-*-*-*-*-*-*
 Curency aviable:
USD - $
EUR - €
GBP - £
*-*-*-*-*-*-*-*-*
""")
elif optionmenu == "!convert":
	option = input("Which currency do you want to convert ? > ")
	print("1 BTC = " + btc["bpi"][option]["rate"] + " " +option) 
else:
	exit("Err")