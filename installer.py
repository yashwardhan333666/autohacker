#! /usr/bin/python3

import os
from sys import platform
import time as t
import subprocess

#python -c "import platform;print(platform.linux_distribution()[0])"

# opt = input("\nInstall required tools?\n[program crashes if not installed if running for first ever time]\n\n(y/n) : ")

def clear():
	if os.name.lower() == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def last():

	clear()
	print('\n\n  Follow ethics. Neither me, 5PID3RH7CK3R, nor any of the respesctive delevopers of any of the automated tools are responsible for your actions.')
	print('\n  No point itterating the classic "Use this for educational purposes only".')
	print('  Its just a formality that does nothing rather than be ignored lol.\n\n  I know you try hacking Google and your friend\'s Facebook once every while ;)')

	trust = str(input('\n  >> '))
	trust = trust.strip()
	if trust.lower() == 'pinky promise':
		print("\n  Thanks, Partner in Crime! (not literally lol)")
		t.sleep(1.5)
		os.system("python3 autohacker.py")
		exit()
	else:
		print("\n  Breaking my trust already? :'( ")
		print("  The only way i let you pass is with a pinky promise")
		input('  Press enter if you promise to type and follow the pinky promise!')
		last()



# below 3 lines execute the python command (importing platform module and getting os name with it) and saves the outupt in 'osname' var
subprocess = subprocess.Popen('python -c "import platform;print(platform.linux_distribution()[0])"', shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
osname = str(subprocess_return)

clear()

t.sleep(0.5)
print("\n\n  Welcome to autohacker's installation script :) ")
t.sleep(0.5)
print('\n\n ',os.name, osname[2:-3])

if os.name != 'posix' or osname.lower()[2:-3] != 'debian':
	print("\n  Oops...")
	print("\n  The code is being run on the wrong operating system.\n")
	print("  This code has been written for and tested on linux [ Debian ] Operating System")
	continuee = input ("\n  You can continue execution if you know what you are doing.\n  However, I do not gurantee stability\n\n  (y/n) >> ")
	if not continuee.lower() == 'y':
		print("""\n\n  Good decision. Reach out to the developer on 
  Discord -> 5PID3RH7CK3R#8174
  Mail    -> 5PID3RH7CK3R@protonmail.com
  		  -> 5PID3RH7CK3R@gmail.com""")
		clear()
		exit()
	else:
		clear()

t.sleep(0.5)	
print("  Okay")

t.sleep(0.5)
input("""\n\n  Here is how the script will unfold

  1)   Homescreen [This] 

  2)   Installation selection screen
            Actual installation

  3)   Information on terminal size
            Terminal size adjustment

  4)   Autohacker Starts.
  
  press enter to continue. """)

clear()	

print ("Installing Stuff for Autohacker")
print("\nThis script only downloads and upgrades the packages required for autohacker to run properly.")
print ("Install of any missing hacking tools can be done from inside autohacker at your will.")

opt = input("""\nInstall Essential Requirements?

[Must install if executing for the first time]

Y for Yes ; Anything else for No

(Recomended Y even if not the first time) >> """) 

opt = opt.strip()

clear()

opt2 = input("""\nInstall Optional Requirements? 

[This is not Bloat]

Y for Yes ; Anything else for No 

(Recomended Y) >> """)

opt2 = opt2.strip()

clear()

if opt2.lower() != 'y' :
	print ("If you face funny behaviour in the program, come back here and install optional requirements.")
	input("Press enter")

clear()
print('\n\nInstallation will start in 10 seconds. Read the following.\n')
print("Installation MAY take some time to complete depending upon the provided conditions.\n\n\n") 
print("Do NOT press the 'Enter' key during the installation, even if you feel it has stopped.\nCheck your internet or restart the installer if this happens.\n\n[ Forcefully exiting is fine, but not suggested. Essentially, it's just apt and pip that is running via this 'fancy' script haha ;) ]\n\n")

t.sleep(10)

if opt.lower() == 'y':
	
	os.system("sudo apt update -y && sudo apt install python3-pip -y ; sudo apt install --only-upgrade python3-pip")
	os.system("pip3 install termcolor ; pip3 install --upgrade termcolor")
	#os.system("pip install pyautogui")

if opt2.lower() == 'y':
	#os.system("sudo apt-get install w3m -y")
	os.system("pip3 install clipboard==0.0.4")
	os.system("sudo apt install hashid -y ")

os.system("sudo apt autoremove -y ; sudo apt clean")

clear()
print("""
On the next screen please ensure that - 

Terminal width is at 95      (max recomended 145)
                AND/OR
Terminal heigh is at 40      (max recomended  45)

Above are the recomended values. 
However, depending on your terminal settings and font, you may pick at will.\nYou can change your zoom inside autohacker if you see some visual elements looking weird or extending to the end of the screen""") # cols - 157, height 37
print("""
----------------------------------------------------------------------------

In most terminals - 

Zoom in  ->   Ctrl Shift +     OR     Ctrl +
Zoom out ->   Ctrl Shift -     OR     Ctrl -

You can change this from your terminal settings.

----------------------------------------------------------------------------
""")

input("""Press enter to continue. """)

os.system("bash termsize.sh")

last()
