from bs4 import BeautifulSoup
import requests
from database import create_db,get_connection,create_table
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url="https://www.geo.tv/latest-news"
response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
articles= soup.find_all("div", class_="entry-title")
news_list=[]
for article in articles:
    headline=article.find("h2")
    if headline:    
        news_list.append(headline.get_text(strip=True))

for i, news in enumerate(news_list, 1):
    print(f"{i}. {news}")

print("Inserting into database:.....")
create_db()
create_table()


conn=get_connection()
cursor=conn.cursor()
for news in news_list:
    query="""insert into headlines (headline) values (%s)"""
    cursor.execute(query,(news,))
conn.commit()
cursor.close()
conn.close()
print(f"Saved {len(news_list)} headlines to MySQL!")