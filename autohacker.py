#!/usr/bin/python3

# TODO: Sherlock saves folder.

from os import *
import os
from termcolor import colored, cprint
import subprocess
from time import sleep

system('tput init')
print("Initialising")
system('clear')

###################### USERNAME ######################

getting_name = subprocess.Popen('python -c "from os import *;print(str(system(\'whoami\'))[:-1])"', shell=True, stdout=subprocess.PIPE)
final_name = getting_name.stdout.read()
uname = str(final_name)
proper_name = str(uname[2:-5])

###################### USERNAME ######################

###################### INIT RECON ######################

def put_recon_values(): #puting values into the recon list to be called later
	global recon_list
	recon_list = ['nmap','sherlock','phoneinfoga','rustscan'] #list of current tools. The name here and the file name in the folder MUST be the exact same (excluding the file extension)

###################### INIT RECON ######################

###################### INIT MISC ######################

def put_misc_values():
	global misc_list
	misc_list = ['web_search','password_manager','calculator','ping','traceroute','whois','madlibs']

###################### INIT MISC ######################

####################### FANCY COLORS #######################

def col(r, g, b, background=False): #found this on stack overfolw to get colored outputs in a fancy way!
	return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

######################## FANCY COLORS #######################

###################### HOMEPAGE ######################

def homepage():
	print()
	system("bash banner.sh") # To print the home screen banner. Ofc lol
	
###################### HOMEPAGE ######################

def inpp():
	global proper_name #getting the terminal username into the function
	
	endd = '\033[0m' #reset color to normal. This is no longer required, but look into it later
	if os.geteuid()==0: #  root
		root = '#'
		# print(col(255, 200, 0) + col(13,44,84, True) + f'{proper_name} {root} ', end='')

	else: # normal user.
		root = '$'
		# print(col(24, 255, 255) + col(14, 13, 60, True) + f'{proper_name} {root} ', end='')

	cprint(" ┌──",'red',end='')
	cprint("Auto",'cyan',end='')
	# cprint("─",'red',end='')
	cprint("Hacker",'cyan',end='')
	cprint("─",'red',end='')
	cprint("[",'yellow',end='')
	if root == '#':
		print(col(255, 200, 0) + col(13,44,84,True) + f'{proper_name}' +"\033[0m",end='')
	else:
		print(col(24, 255, 255) + col(4, 13, 60,True) + f'{proper_name}' +"\033[0m",end='')
	cprint("]",'yellow')
	cprint(f" └─{root}",'red',end='')
	print(" ",end='')
	opt = str(input(col(118, 16, 235)))
	
	system('tput sgr0')

	# checkex = opt.lower()
	if opt == '0':
		helpp()
	elif opt == '1':
		recon()
	elif opt == '2':
		print("Social engineering")
		inpp()
	elif opt == '3':
		print("Non automated")
		inpp()
	elif opt == '4':
		misc()
	elif opt == '5':
		brut()
	elif opt == '6':
		print("Database")
	elif opt.lower() == 'exit' or opt == '99': #Exit program
		try:
			cprint("BYE BYE. Happy Hacking.","red","on_white")
			input()
			system("clear")
			print("\nAutohacker Closed.\n Stay out of Trouble, Unknown Friend.")
			sleep("1.5")
			system("clear")
			exit()
		except Exception as e:
			cprint("BYE BYE. Happy Hacking.","red","on_white")
			input()
			system("clear")
			print("\nAutohacker. Closed. *sad sobbing sounds*")
			# print(f"\nOh and btw, i had an error \n{e}")
			exit()
		# cprint("BYE BYE. Happy Hacking.","red","on_white")
		# input()
		# system("clear")
		# print("\nAutohacker. Closed. *sad sobbing sounds*")
		# exit()
	elif opt.lower() == 'github':
		print("Here is the github link -> https://www.gitlab.com/")
		input()
		inpp()
	elif opt.lower() == 'zoom':
		system('bash termsize.sh')
		system('clear')
		inpp()
	elif opt.lower() == 'banner':
		homepage()
		inpp()
	elif opt.lower() == 'clear':
		system('clear')
		inpp()
	elif opt.lower() == 'help':
		print('psst. Try \'Banner\' and then \'0\'')
		inpp()
	elif opt.lower()[0:5] == 'saves':
	 	if len(opt) == 5 or len(opt) == 5:
	 		system('ls saves/')
	 		
	 	else:
	 		file = opt[6:]
	 	
	 		system(f'sensible-pager saves/{file}')
	 		# system('python3 field.py')
	 	inpp()

	else:
		print('\n')
		system(opt) 
		print("\n")
		inpp()



###################### BRUTING #########################
def brut():
	print("Bruting not ready yet")
	inpp()
###################### MISCLANEOUS TOOLS ######################

def misc():   # add recon style color coding here as well.
	try:
		global misc_list
		add = ''
		misc_x = []
		misc_input = 0
		put_misc_values()
		system("clear")
		cprint("MISCLANEOUS", "red")
		for x in range(len(misc_list)):
			if misc_list[x] == 'web_search':
				add = '[w3m]'
				if not os.path.exists("usr/bin/s3m"):
					system('tput setaf 196')
					print(f'{x}) {misc_list[x]} {add}')
					misc_list[x] = False
					misc_x.append(x)
				else:
					system('tput setaf 148')
					print(f'{x}) {misc_list[x]} {add}')

				system('tput sgr0')
			elif misc_list[x] == "password manager":
					system(f"tput setaf 148 ; echo {x}) {misc_list[x]} {add}")
					# (f"{x}) {misc_list[x]} {add}")

		misc_input = int(input(":"))

		if misc_input == 0 and misc_x.__contains__(misc_input):
			cprint("Would you like to install links2 (y/n)","white" ,"on_blue", end=': ')
			mopt = input()
			if mopt.lower() == 'y':
				system("clear ; sudo apt install w3m -y -f --fix-missing && clear")
				misc()
			else:
				misc()
		else:
			if misc_input == 0:
				webs()
	except KeyboardInterrupt:
		inpp()
	except ValueError:
		misc()

def madlibs():
	# system("python3 madlibs.py")
	print("Madlibs not ready yet.")
	inpp()

def pswdmanager():
	print("Yet to add the password manager")
	inpp()


def calculator():
	print("Yet to add the calculator.")
	inpp()

def webs():
	print("Work on web search later. Pick a single browser.")
	#run a check_install and ask y/n from there. Take the below code there only.
#this is will be much more logical and also more oragnised.
	# system("clear")
	# try:
	# 	cprint("Websearch", "yellow", "on_grey")
	# 	query = input("Search query: ")
	# 	argg = input("custom arguments for w3m (optional): ")
	# 	engine = input("""Pick a search engine
	#      Surface Web

	#   1. Google.com
	#   2. DuckDuckGo.com
	#   3. Bing.com
	#   4. Ecosia.com
	#   5. Ask.com

	#      Darknet (Excluding Ahmia, all others use onion.dog darknet proxy)

	#   6. Ahmia (without darknet proxy)
	#   7. Torch
	#   8. Not Evil
	#   9. Candle (not ready)

	# :
	#   """) #get candle ready.
	# 	if engine == '1':
	# 		system(f"w3m https://www.google.com/search?q={query} {argg}")
	# 	elif engine == '2':
	# 		system(f"w3m https://duckduckgo.com/?q={query} {argg}")
	# 	elif engine == '3':
	# 		system (f"w3m https://www.bing.com/search?q={query} {argg}")
	# 	elif engine == '4':
	# 		system(f" w3m https://www.ecosia.org/search?q={query} {argg}")
	# 	elif engine == '5':
	# 		system (f"w3m https://www.ask.com/web?o=0&l=dir&qo=homepageSearchBox&q={query} {argg}")
	# 	elif engine == '6':
	# 		system (f"w3m https://www.ahmia.fi/search/?q={query} {argg}")
	# 	elif engine == '7':
	# 		system (f"w3m http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion.dog/cgi-bin/omega/omega?P={query} {argg}")
	# 	elif engine == '8':
	# 		system (f"w3m http://deeeepv4bfndyatwkdzeciebqcwwlvgqa6mofdtsvwpon4elfut7lfqd.onion.dog/Search/{query} {argg}")
	# 	#elif engine == '9': #this is candle. Currently not ready. Add how to check if a website is online.
	# 	#	system(f" w3m http://")
	# 	else:
	# 		cprint("\n I guess you know what numbers are. If you are trying to go \"back\"... here is a hint for you ;)", "red")
	# 		input()
	# 		webs()

	# 	system('clear')
	# 	homepage()
	# 	inpp()
	# except KeyboardInterrupt:
	# 	misc()
	inpp()
###################### MISCLANEOUS TOOLS ######################

###################### Whois, Traceroute and Ping ######################

def wois(): #whois search
	system("clear")
	wadr = input("Adress: ")
	wpara = input("Additional parameters for whois (optional): ")
	cprint("crtl+c ONCE to exit whois. Press enter to start", "white", "on_red")
	input()
	system(f"whois {wpara} {wadr}")
	print("\n\nExecuted - ")
	cprint(f"\nwhois {wpara} {wadr}" , "white","on_blue")
	print("\nPress enter to continue" )
	input()
	misc()
def traceroute():
	system("clear")
	tadr = input("Adress: ")
	traip = input("""Traceroute over/for -
1. IPv4
2. IPv6
3. I just want the normal traceroute
Number: """)
	if traip == '1' or traip == '4':
		print("Trace over IPv4")
		iptra = 4
	elif traip == '2' or traip == '6':
		print("Trace over IPv6")
		iptra = 6
	else:
		print("Okay. Normal traceroute it is!")
		iptra = ''
	tpara = input ("Additional parameters for traceroute (optional): ")
	cprint("crtl+c ONCE to exit traceroute. Press enter to start", "white", "on_red")
	input()
	system(f"traceroute {tpara} {tadr}")
	print("\n\nExecuted - ")
	cprint(f"\ntraceroute{iptra} {tpara} {tadr}" , "white","on_blue")
	print("\nPress enter to continue" )
	input()
	misc()
def ping():
	system('clear')
	padr = input ("Adress: ")
	piip= input ("""Ping over/for - 
1. IPv4
2. IPv6 
3. I just want a normal ping.
Number: """) 
	if piip == '1' or piip == '4':
		print("Ping over IPv4")
		ippi = 4
	elif piip == '2' or piip == '6':
		print("Ping over IPv6")
		ippi = 6
	else:
		print("Okay. Normal ping it is!")
		ippi = ''
	ppara = input ("Additional parameters for ping (optional): ")
	cprint("Ctrl+C ONCE to stop ping. Press Enter to start", "white","on_red")
	input()
	system(f"ping{ippi} {ppara} {padr}")
	print("\n\nExecuted - ")
	cprint(f"\nping{ippi} {ppara} {padr}" , "white","on_blue")
	print("\nPress enter to continue" )
	input()
	system("clear")
	misc()

###################### Whois, Traceroute and Ping ######################

###################### RECON main ######################

def recon():
	try:
		global recon_list # the list of tools
		recon_x = [] # list for the tool not installed on system
		recon_input = 0
		put_recon_values() # puting the values into the recon_list list (not required, ik, but eeh lol)
		system("clear") # clearing the screen
		cprint("RECON", "green") # Fancy output, make better in future
		for x in range(len(recon_list)): # looping through the items 
			if not os.path.exists(f'/usr/bin/{recon_list[x]}'): # if tool not found in default location, assume not installed
				system('tput setaf 196') # color for not installed
				print(f'{x})  {recon_list[x]}') # print tool name with index
				# recon_list[x] = False # replace tool name in recon_list with Flase
				recon_x.append(x) # append the not installed tool index number to recon_x
			else:
				system('tput setaf 148') # if tools is found in default location
				print(f'{x})  {recon_list[x]}') # print
			system('tput sgr0') # reset text formating
		print("99) Back to Home Page")
		try:
			recon_input = int(input("enter number: ")) # user input to pick a tool
		except:
			recon() # on invalid input 
		put_recon_values() # reset the values.... still not required, but better safe than sorry lol

		
		if recon_input == 99: # on exit
			system('clear')
			homepage()
			inpp()
		elif recon_x.__contains__(recon_input): # if not installed tool index matches user input
			print(f"{recon_list[recon_input]} not found on system ;( ") # inform user that the tool is not installed
			ask_install = input(f"Would you like to install {recon_list[recon_input]} (y/n) :") # ask if the tool is to be installed or not
			if ask_install.lower() == 'y': # if installing is to take place
				if recon_input == 0 or recon_input == 1 : # for tools that can be directly installed through apt
					system(f"clear ; echo 'Updating reposotries' ; sudo apt update -y ; clear ; echo 'installing {recon_list[recon_input]}' ; sudo apt install {recon_list[recon_input]}") # update and install
					system("clear")
					recon() # back to tool selection
				else:
					print(f"Run installer for {recon_list[recon_input]}") # yet to be done
					inpp()	# get back the prompt
			else:
				recon() # if not y for install of not installed tool, go back to the reconanance page
		else:
			print(f"{recon_list[recon_input]} Found on system! :)") # if it is 'not not' in /usr/share/<tool name> then the tool is obviously installed
			try:
				if recon_list[recon_input] == 'sherlock':
					try:
						system("clear")
						print("sherlock\n")
						sherlock_username = str(input("Enter username >> "))
						system(f"mkdir saves/sherlock & >/dev/null ; sherlock {sherlock_username} > saves/{sherlock_username}.txt") # test this out first
						input("\nPress enter to continue\n")
						inpp()
					except Exception as e:
						print(f"Had an error with sherlock\n{e}")
						inpp()
				else:
					system(f"python3 recon/{recon_list[recon_input]}.py")
			except Exception as e:
				print(f"Had an error\n{e}")

	except KeyboardInterrupt:
		system('clear')
		homepage()
		inpp()
	except ValueError:
		misc()

###################### RECON main ######################

###################### HELP ######################

def helpp():
	system("clear")
	print ()
	cprint("Autohacker Help Menu","blue", "on_white")
	try:
		hopt = input("""
Enter number. The help will be shown in your (Default / Choose) Text Editor.

[0] About

[1] Troubleshoot

[2] Home Screen and general usage

[*] Back

: """) 
	except KeyboardInterrupt:
		cprint("\n I guess you know what numbers are. If you are trying to go \"back\"... here is a hint for you ;)", "red")
		input()
	else:
		if hopt == '0':
			system("sensible-pager help/about.txt")
		elif hopt == '1':
			system("sensible-pager help/troubleshoot.txt")
		elif hopt == '2':
			system("sensible-pager help/homesc.txt")
		elif hopt == '3':
			system("sensible-pager help/web_search.txt")
		elif hopt.lower() == 'back':
			system('clear')
			homepage()
			inpp()
	# else:
	# 	cprint("\n I guess you know what numbers are. If you are trying to go \"back\"... here is a hint for you ;)", "red")
	# 	input()
	system("clear")
	helpp()

###################### HELP ######################


try:
	homepage()
	inpp()
except Exception as e:
	system('clear')
	print(f"Hey! Fix your code dumbo 5PID3RH7CK3R. There's an error\n{e}")