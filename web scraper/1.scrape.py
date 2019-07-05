import numpy as np
import pandas as pd
import requests
html_table=pd.read_html("https://www.javatpoint.com/html-table")

for table in html_table:
    print(table.head())

payload = {
    'username': ' ',
    'pass': ''
}
with requests.Session() as session:
    print("RMEDY")
    post = session.post(POST_LOGIN_URL, data=payload)
    r = session.get(REQUEST_URL)
    print(r.text)   #or whatever else you want to do with the request data!
    html_table=pd.read_html(r.text)
    print(len(html_table))