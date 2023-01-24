from facebook_scraper import get_posts

#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
#instantiate the Facebook_scraper class

page_name = "RockingDealsUk"
posts_count = 10
browser = "chrome"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 600 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)


json_data = meta_ai.scrap_to_json()


data=json.loads(json_data)


for key in data.keys():
    #data.get(key)['content']
    print(key)