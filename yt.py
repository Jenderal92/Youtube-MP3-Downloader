import requests as shin_code
from colorama import Fore as shinx
import re,socket, random

def Banner():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print "==================================================="
	print shinx.YELLOW + "[!] Mp3 Converter Youtube  |" + shinx.WHITE +" "+ shinx.GREEN + "PYTHON CODE" + shinx.WHITE
	print shinx.YELLOW + "[!] Contact : " + shinx.WHITE+"https://icq.im/Shin403"
	print shinx.YELLOW + "[!] Host : " + shinx.WHITE+"Shin@"+host_name
	print shinx.YELLOW + "[!] LocalHost : " + shinx.WHITE + host_ip
	print "=============" 
Banner()

urll = raw_input(shinx.RED + 'Enter YT Link : ' +shinx.WHITE).replace('https://youtu.be/','')
try:
	urls = "https://api.vevioz.com/file/mp3/"+urll
	r = shin_code.get(urls).content
	if '<h2 class="text-lg text-teal-600 font-bold m-2 text-center">' in r:
		REX = re.findall('<h2 class="text-lg text-teal-600 font-bold m-2 text-center">(.*?)</h2>',r)
		for REW in REX:
			print('TITLE : ' + shinx.GREEN + REW  +shinx.WHITE)
	if '<div class="download flex flex-wrap sm:inline-flex text-center items-center justify-center">' in r:
		REG = re.findall('/mp3/320/(.*?)" class="shadow-xl bg-blue-600 text-white hover:text-gray-300 focus:text-gray-300 focus:outline-none rounded-md p-2 border-solid border-2 border-black ml-2 mb-2 w-25">',r)
		for REH in REG:
			print('PARSE : ' +shinx.GREEN + REH + shinx.WHITE)
			print(shinx.GREEN + '\nLoading Download ......'+ shinx.WHITE)
	r2 = shin_code.get("https://cdn-40.vevioz.com/download/"+urll+"/mp3/320/"+REH)
	open(REW+".mp3", "wb").write(r2.content)
	print(shinx.GREEN + 'Sucess Download !!! , files stored in this directory.' + shinx.WHITE)
	download(r2)
		
except:
	pass
		
