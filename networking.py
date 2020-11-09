import os
import sys
# from dotenv import load_dotenv      #I used dotenv for storing my gmail app password. You can skip if you wish to enter you password directly to the monitor_uptime() funstion as done below.
# load_dotenv()
from urllib.request import Request, urlopen, URLError
import http.client
from urllib.parse import urlparse

sys.path.append('network_scanner/')
import network_scanner
sys.path.append('server_monitoring/')
import server_monitoring
sys.path.append('packet_testing/')
import packet_testing

print("\t\t\t\t*************************************")
print("\t\t\t\t*************************************\n")
print("\t\t\t\t      WELCOME TO NETWORKING TOOL\n")
print("\t\t\t\t*************************************")
print("\t\t\t\t*************************************")
repeat = True
while repeat:
    print("\nWe have the following features.\n1. Network Scanner\n2. Server Monitor\n3. Packet Loss Testing.")
    user_choice = int(input("Enter the operation you want to perform [1,2 or 3]:  "))
    if user_choice == 1:        #Network Scanner
        target_IP = str(input("Please specify target IP address/ range to scan:  "))
        if target_IP is not None:
            network_scanner.IP_scanner(target_IP)
        else:
            print("Invalid input")
    
    elif user_choice == 2:      # Server monitoring tool 
        # GMAIL_PASSWORD = os.getenv("PASSWORD")      #this is just used for protecting my gmail password. You can skip. 
        required_url = input("Enter the url you want to monitor:  ")
        try:
            # request = Request(required_url)
            # response = urlopen(request)
            site = urlparse(required_url)        
            conn = http.client.HTTPConnection(site[1])      
            conn.request("HEAD", site[2])       
            status = conn.getresponse()
            status_code = status.status
        except:
            print("The input url is invalid.")
        else:
            server_monitoring.monitor_uptime(required_url, 
                ["reciever1@example.com", "reciever2@example.com"], 
                "sender@example.com", 
                "sender_gmail_password")        # You can replace "sender_gmail_password" with GMAIL_PASSWORD and uncomment line no. 3, 4 and 33 if you want to use dotenv. 
                                                # Don't forget to check pre_requisties no. 3 because using dotenv is recommended.

    elif user_choice == 3:      #Packet loss testing tool.
        target_IP = input("Enter the IP where you want to sent packet. (Leave blank for default i.e. Google DNS):  ")
        if target_IP == "":
            packet_testing.packet_testing()
        else:
            packet_testing.packet_testing(target_IP)
    
    else:
        print("Invalid choice of operation. Enter 1, 2 or 3.")
    
    continue_again = True
    while continue_again:
        again = str(input("\nDo you want to continue [y/n]?  "))
        yes = ("Y","y","yes","YES")
        no = ("N","n","no","NO")
        if again in yes:
            pass
            continue_again = False
        elif again in no:
            repeat = False
            continue_again = False
            print("\nHope you liked it. \n\t\t\t\t\t\t\t HAVE A GREAT DAY AHEAD!!!")
        else:
            print("Invalid choice.")
            print("Please enter y if you want to continue and n if you want to exit.")

