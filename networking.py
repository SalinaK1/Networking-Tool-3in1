import os
import sys
from dotenv import load_dotenv
load_dotenv()
from urllib.request import Request, urlopen, URLError

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
        GMAIL_PASSWORD = os.getenv("PASSWORD")
        required_url = input("Enter the url you want to monitor:  ")
        try:
            request = Request(required_url)
            response = urlopen(request)
        except:
            print("The input url is invalid.")
        else:
            server_monitoring.monitor_uptime(required_url, 
                ["sk02433018@student.ku.edu.np", "salina.koirala@aiesec.net"], 
                "saleena.koirala1@gmail.com", 
                GMAIL_PASSWORD)

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

