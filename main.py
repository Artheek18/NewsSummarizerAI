import requests
from send_email import send_email

topic = "apple"
lang = "en"

api_key = "1abb172f46224091956d2b49ef0da16a"
url = (f'https://newsapi.org/v2/everything?q={topic}&from'
       '=2026-02-20&to=2026-02-20&sortBy=popularity&apiKey=') + api_key + f'&language={lang}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
code = response.status_code
content = response.json()
#print(code)
#print(type(content))
print(content)

#article = content["articles"][0]

#title = article.get("title", "No title")
#description = article.get("description", "")
#body = f"{title}\n{description}\n\n"
#send_email(body)
body =''
for item in content['articles'][:20]:
    if item['author'] == None:
        body += ("Subject: Your Daily News\n\n" +
                 ("Unknown Author" +
                 '\n' + item['title'] +
                 '\n' + item['description'] +
                 '\n' + item['url'] + 2 * '\n'))
    else:
        body +=  ("Subject: Your Daily News\n\n" +
                 (item['author']
                 + '\n' + item['title']
                 + '\n' + item['description']
                 + '\n' +  item['url'] + 2*'\n'))

body = body.encode('utf-8')
send_email(message=body)

'''response = requests.get(url)
text = response.text
print(text)'''