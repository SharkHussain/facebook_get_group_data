import facebook

#!/usr/bin/python
# coding: utf-8
import requests



app_id ="663245868933778"#"1658776737975045"
app_secret ="64e7c9e11a155e8d54feaea8e3a1a468"#"3e6fdf814874085debad1e7377d99a90"
def get_fb_token(app_id, app_secret):
    url = 'https://graph.facebook.com/oauth/access_token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret
    }
    response = requests.post(url, params=payload)
    return response.json()['access_token']

#your_access_token="EAAXkpg46iwUBACry9LZCZC0KLZAuhil9c0XXExTR2YRe7LSDlLtbuMZAZBDSRuowP6bp5SEcIKjyMwLUOZBhBvDAb7adSzRAubaFjVLJjZBdZAuLbbDJFDE7uwsYMwodRfsHczTvLWdLSo6v9ZALISPzclhKjFnZA6Dm8bCwM2rHJyzSFS5u83JJg48lm7VTQpwSqEZAkzIB3ZCOxBJ2IwJauPQf9LzZCp6lJNVXQQNnq9Hwul34qsSzwl3y3"


#token="EAAXkpg46iwUBAIZBybl99ZCpp2Pz5HXCTE7aHAPVAvlQIHmyW5tH1jFp3ZC8aJ8SlO9SuA3LZA3MOopZAxiM4oag7n6rwAUiwaeLIpzcLpRuy8waHncCdxOwGqJ25pUZBKEvtigyl6iAz6gDqh4zIZCLksRW8uv8CBg0xN571IZCwLEom6SET7UaiHLHe9HQLblXR96duCd6JhQ7aF0T0FMjGKrHwS4RrlLwKF5j2jZCPDRvUQ17wLCPe"
app_id ="1658776737975045"


token="1658776737975045|mNU7yjnHy3a5f14LKkDn44aKC98"

app_id ="663245868933778"#"1658776737975045"
app_secret ="64e7c9e11a155e8d54feaea8e3a1a468"#"3e6fdf814874085debad1e7377d99a90"
token=get_fb_token(app_id, app_secret)

token="EAAXkpg46iwUBABzBDS0gyIEwXOLZAlpb3lBzN1tweFHLG1uH8JaOAZCkDVEZB4klprt6RuAHi14kR4Fnow924X1jRzvT2QzlAMnlAJqO8x7A5LD3HUa1Q5NrZC3Tb9HOnY3aloZBLZCrPmzuBNvA6VKIGnCk1ucUKXnqjunKmZBi70LWSdjfNkNtlnFDPAkWjFyastftFx8LWMQpUidJjoG5ZBGNddKQdVZBt8jOly2Ld0Lq7dTePUjs1"

graph = facebook.GraphAPI(access_token=token, version="3.1")

source_d="132638208621637"
source_d="429634238102495"
#source_d="1564214813867995" #Good house keeping - Book room
source_d="3443873145692754" #Thrift deals uk
source_group_posts=graph.get_object(id=source_d + "/feed")["data"]


#source_group_posts = graph.get_object(id=source_group_id + "/feed")["data"]

# Iterate through the posts
for post in source_group_posts:
    # Check if the post is a link or a text post
    if "message" in post or "link" in post:
        # Get the message and link (if any)
        message = post.get("message", "")
        link = post.get("link", "")
        print(message)

        # Create the post data
        # post_data = {
        #     "message": message,
        #     "link": link
        # }

        # Post the data to the target group
        #graph.put_object(parent_object=target_group_id, connection_name="feed", message=message)



#https://amzn.to/3WE3rwt

#https://amzn.to/3ksiGv9

#https://www.amazon.co.uk/dp/1942761988?psc=1&linkCode=ll1&tag=dealhunter0ae-21&linkId=32c4e078a899a6363484c3a3390662c3&language=en_GB&ref_=as_li_ss_tl

#https://www.amazon.co.uk/gp/product/B00AUDCIIO?psc=1&linkCode=ll1&tag=dealhunter0ae-21&linkId=32c4e078a899a6363484c3a3390662c3&language=en_GB&ref_=as_li_ss_tl


#this needs to be appended: ?psc=1&linkCode=ll1&tag=dealhunter0ae-21&linkId=32c4e078a899a6363484c3a3390662c3&language=en_GB&ref_=as_li_ss_tl




from requests import get

def get_real_url_from_shortlink(url):
    resp = requests.get(url)
    return resp.url


import amsin


import re

import click
import requests
from bs4 import BeautifulSoup
#import pyperclip

u="https://www.amazon.co.uk/dp/1942761988?psc=1&linkCode=ll1&tag=dealhunter0ae-21&linkId=32c4e078a899a6363484c3a3390662c3&language=en_GB&ref_=as_li_ss_tl"

@click.command()
@click.argument('url')
def amsin(url):
    """Turn a long amazon link into a short amzn link."""
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    asin = soup.find(text=re.compile('ASIN:')).parent.next_sibling
    url = 'https://amzn.com/' + asin.strip()
    print(url)
    #pyperclip.copy(url)




import requests
import re

url=requests.get(u).text
amz_link = re.findall(r'cashbackUrl = .*;', url)
print(amz_link[0].replace('cashbackUrl =', '').replace('"', '').replace(';', '').strip())
