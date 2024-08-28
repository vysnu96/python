import requests
from bs4 import BeautifulSoup
import json
# curl -X POST https://api.telegram.org/bot7422793066:AAGn7AxNO5dqF6wrf40uydFfw9vL_LygOHw/sendMessage -H "Content-Type: application/json" -d "{\"chat_id\" : \"-4241845023\", \"text\":\"test\"}"
# for now()
import datetime
# for timezone()
import pytz
# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

URL = "https://api.telegram.org/bot7422793066:AAGn7AxNO5dqF6wrf40uydFfw9vL_LygOHw/sendMessage"
header = {"Content-Type": "application/json"}
payload = '''{\"chat_id\" : \"-4241845023\", \"text\":\"%s\"}'''%current_time_str
res = requests.post(URL, headers=header, data=payload)
print(res.json())
