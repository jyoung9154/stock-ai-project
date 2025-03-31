import requests
import html
import re
from bs4 import BeautifulSoup

def get_popular_stocks_naver():
    url = "https://finance.naver.com/sise/lastsearch2.naver"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    stocks = {}
    
    rows = soup.select(".type_5 tr")
    print(f"🔍 종목 데이터 개수: {len(rows)}")  # 디버깅용 출력
    
    for row in rows[1:11]:  # 인기 검색 상위 10개만
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        name = cols[0].get_text(strip=True)
        code = cols[1].get_text(strip=True)
        stocks[name] = code
    
    return stocks

def get_naver_news(query):
    client_id = "wNhYXuAbjramfbYVOR2G"
    client_secret = "6PVGfQZwsJ"
    url = "https://openapi.naver.com/v1/search/news.json"
    params = {"query": query, "display": 5, "sort": "sim"}
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    print(f"🔍 '{query}' 뉴스 개수: {len(data.get('items', []))}")  # 디버깅용 출력
    
    news_list = []
    for item in data.get("items", []):
        title = html.unescape(re.sub(r"<.*?>", "", item["title"]))  # HTML 태그 제거 & 특수문자 복원
        link = item["link"]
        news_list.append({"title": title, "link": link})
    
    return news_list

def get_news_content(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 다른 셀렉터를 사용하여 뉴스 본문 추출
    content = soup.select_one('div#newsEndContents, div#articleBodyContents')
    
    if content:
        # HTML 태그 제거 및 텍스트만 추출
        content_text = html.unescape(re.sub(r"<.*?>", "", content.get_text(strip=True)))
        return content_text
    return "❌ 본문을 가져올 수 없습니다."


def get_popular_stocks_news():
    stocks = get_popular_stocks_naver()
    
    for name, code in stocks.items():
        print(f"[📌 {name} ({code}) 관련 뉴스]")
        print("=" * 50)
        news = get_naver_news(name)
        if not news:
            print("❌ 관련 뉴스 없음")
        else:
            for i, article in enumerate(news, 1):
                print(f"{i}. {article['title']} ({article['link']})")
                content = get_news_content(article['link'])  # 뉴스 본문 크롤링
                print(f"   내용: {content}")
        print("\n")

if __name__ == "__main__":
    get_popular_stocks_news()
