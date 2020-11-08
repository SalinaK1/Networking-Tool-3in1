import os
import sys
from dotenv import load_dotenv
load_dotenv()

# importing server_monitoring.py
sys.path.append('server_monitoring/')
import server_monitoring

# Server monitoring tool
GMAIL_PASSWORD = os.getenv("PASSWORD")
server_monitoring.monitor_uptime("https://www.ku.edu.np/kuhackfest", 
    ["sk02433018@student.ku.edu.np", "salina.koirala@aiesec.net"], 
    "saleena.koirala1@gmail.com", 
    GMAIL_PASSWORD)
   