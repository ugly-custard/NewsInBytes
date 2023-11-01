import json
from gnews import GNews
from utils.summary import Summarizer

s = Summarizer()
n = GNews(language="en", country="IN")
news = n.get_top_news()
# news = n.get_news("topic")
output = []
i = 0
for new in news[:25]:
    out = {}
    print(f"Getting and summarizing article {i}")
    a = n.get_full_article(new['url'])
    out['title'] = a.title
    out['url'] = new['url']
    out['summary'] = s.generate_abstractive_summary(a.text)
    out['summary'] = out['summary'].partition(" ")[2][:-4]
    imgs = [img for img in a.images if not img.startswith("https://news.google.com")]
    out['img_url'] = imgs[0]
    output.append(out)
    i += 1

with open("summarized_news.json", "w") as file:
    json.dump(output, file, indent=2)
