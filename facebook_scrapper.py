from facebook_scraper import get_posts

#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
#instantiate the Facebook_scraper class

page_name = "rockingdealsuk"
posts_count = 100
browser = "chrome"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 600 #600 seconds
headless = True
#meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

#this one is using group_id
meta_ai=Facebook_scraper(132638208621637, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

#3443873145692754
meta_ai=Facebook_scraper(3443873145692754, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)


json_data = meta_ai.scrap_to_json()


data=json.loads(json_data)


for key in data.keys():
    da=data.get(key)['content']
    dat=data.get(key)['posted_on']
    print(dat)
    print(da)
    print('')



#####################################################################################
#Better to use group_id

from facebook_scraper import get_posts

for post in get_posts(page_name, pages=100):
    #print(post['text'][:50])
    print(post['text'])


for post in get_posts(132638208621637, pages=10):
    #print(post['text'][:50])
    #print(post['text'])
    print(post['time'])