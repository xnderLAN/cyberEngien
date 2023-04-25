import requests
import os
import requests
from urllib3.exceptions import InsecureRequestWarning


# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

import sqlite3


def ghdb_insert(dork):
    conn = sqlite3.connect("/home/amon/dev/cyberEngien/src/db/data/data.db")
    cur = conn.cursor()

    sql_query = "INSERT INTO ghdb (dork) VALUES (?)"
    values = (str(dork))
    cur.execute(sql_query, values)

    conn.commit()
    conn.close()

cookies = {
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1682116290146%2Cregion:%27DZ%27}',
    '_ga': 'GA1.3.2101044378.1682116291',
    '_gid': 'GA1.3.764734352.1682116291',
    '_gat': '1',
    'XSRF-TOKEN': 'eyJpdiI6Img1dFwvN043UHBiWlp6TXYrdURjamlnPT0iLCJ2YWx1ZSI6Im5LcTQ2bVMxRVdjbmxuZUxTNldJdjVKSEVPWURRdUU0MDlaQmdQZzFvT21zWU1uc3k4QXF6VnNWclFMM2tiZTciLCJtYWMiOiJkNmUwODhiNjI0NzVmZmE3YWE0NjA3OThkZjUzYjFkNDI5YTZmMTg2YTg5ZDRkN2M2YzRhNTVkZTk0YmEzZmVkIn0%3D',
    'exploit_database_session': 'eyJpdiI6Im9ZQkZaYW0rek1CUXhBbEttK0tXSlE9PSIsInZhbHVlIjoiaHdKcm51bDlPTldzRVdPdnZqMXora3dlbDB5UGFFMm1Dbkd3ZzJCNmVsNWZFcFRER3RyV05SREY2RE9hNG8yUCIsIm1hYyI6IjRiODRjZjFhNTY2YjIwODFlMzQzNDJjZDFlN2Y4OGZjMzQ2MTJkYzU1MGQ5NzI2YmU1YWEyNGNjYzRhYzM3MDEifQ%3D%3D',
}

headers = {
    'Host': 'www.exploit-db.com',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.exploit-db.com/google-hacking-database',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Cookie': 'CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1682116290146%2Cregion:%27DZ%27}; _ga=GA1.3.2101044378.1682116291; _gid=GA1.3.764734352.1682116291; _gat=1; XSRF-TOKEN=eyJpdiI6Img1dFwvN043UHBiWlp6TXYrdURjamlnPT0iLCJ2YWx1ZSI6Im5LcTQ2bVMxRVdjbmxuZUxTNldJdjVKSEVPWURRdUU0MDlaQmdQZzFvT21zWU1uc3k4QXF6VnNWclFMM2tiZTciLCJtYWMiOiJkNmUwODhiNjI0NzVmZmE3YWE0NjA3OThkZjUzYjFkNDI5YTZmMTg2YTg5ZDRkN2M2YzRhNTVkZTk0YmEzZmVkIn0%3D; exploit_database_session=eyJpdiI6Im9ZQkZaYW0rek1CUXhBbEttK0tXSlE9PSIsInZhbHVlIjoiaHdKcm51bDlPTldzRVdPdnZqMXora3dlbDB5UGFFMm1Dbkd3ZzJCNmVsNWZFcFRER3RyV05SREY2RE9hNG8yUCIsIm1hYyI6IjRiODRjZjFhNTY2YjIwODFlMzQzNDJjZDFlN2Y4OGZjMzQ2MTJkYzU1MGQ5NzI2YmU1YWEyNGNjYzRhYzM3MDEifQ%3D%3D',
}

params = {
    'draw': '4',
    'columns[0][data]': 'date',
    'columns[0][name]': 'date',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'url_title',
    'columns[1][name]': 'url_title',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'cat_id',
    'columns[2][name]': 'cat_id',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'author_id',
    'columns[3][name]': 'author_id',
    'columns[3][searchable]': 'false',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'order[0][column]': '0',
    'order[0][dir]': 'desc',
    'start': '15',
    'length': '15',
    'search[value]': '',
    'search[regex]': 'false',
    'author': '',
    'category': '',
    '_': '1682116290905',
}

for i in range(1,512):
    params['draw']=str(i)
    os.system("clear")
    print(f"step: {i}/512")
    response = requests.get(
        'https://www.exploit-db.com/google-hacking-database',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )
    for j in response.json()['data']:
        ghdb_insert(j['url_title'].split("\">")[1].strip("</a>"))

