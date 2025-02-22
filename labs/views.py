from django.shortcuts import HttpResponse
import os
import subprocess
from datetime import datetime
import pytz

def htop(request):
    username = os.getenv('USER', 'codespace') 


  
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

   
    top_output = subprocess.getoutput('top -b -n 1')

    response = f"""
    <h1>System Information</h1>
    <p><b>Name:</b> Naman Katoch</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
