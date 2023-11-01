import requests
from bs4 import BeautifulSoup
import json

def get_url():
    to_get="https://www.bbc.com/news/topics/c2vdnvdg6xxt"
    pre_url="https://www.bbc.com"
    urls=[]
    
    page = requests.get(to_get)
    soup = BeautifulSoup(page.content, 'html.parser')
    links=soup.find_all("a",class_="ssrcss-1mrs5ns-PromoLink exn3ah91")
    for link in links:
        url=pre_url+str(link['href'])
        urls.append(url)
    return urls

def news_content():
    urls=get_url()
    data=[]
    content=""    
    for url in urls:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            title=soup.find("h1", { "id" : "main-heading" }).text
            a=soup.find_all('div',class_="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")
            img_url=soup.find('img',class_="ssrcss-evoj7m-Image edrdn950")
            img_url=img_url['src']
            for a in a:
                content=content+str(a.text)

            if title and content != "":
                error_code=0
                unsummarized_news={
                    'title':f'{title}',
                    'content':f'{content}',
                    'url':f'{url}',
                    'img_url':f'{img_url}',
                    'error_code':f'{error_code}'
                }
                data.append(unsummarized_news)
        
        except Exception as e:
            error_code=1
        
    return data

data=news_content()

with open('unsummarized_news.json', 'w') as fp:
    for data in data:
        json.dump(data, fp)
