# Networking Tool

This is a basic networking tool with maily three features integrated in a single program. All these are built entirely on python.

First of all, we have a **Basic Network Scanner** *(IP Scanner to be specific)*. It can scan an IP/ a range of IP and display its MAC address as well as Operating System.

Secondly, we have a **Server Monitoring Tool** that monitors uptime continuously (update each 2 seconds here). An alert email can also be sent *(here I have sent to myself for demo only.)* if the server is continuously down for 1 minute, 5 minutes and the multiple of 10 minutes.

Lastly, we also have a **Packet Loss Testing Tool** that determines a packet loss. The default here is set to Google DNS Server (8.8.8.8), but user can also input an ip if they want to test before sending packet.

---

### Pre-requisties:

- Make sure you have Python installed before you go on. *(I have build on python 3.6.9. Any version > 3.6 works perfectly.)*
- Run the command, `pip install --pre scapy[basic]` or `sudo apt install python3-scapy` *(if you don't have pip installed).*
- To store you password securely in server monitoring tool, you need .env file. For that, run the command `pip install python-dotenv`. Make a .env file and store your gmail password there in the format **PASSWORD = your_gmail_app_password**.

---

### Instruction for running:

Run the file networking.py with root priviledges. 
For linux, run `sudo python3 networking.py`. 