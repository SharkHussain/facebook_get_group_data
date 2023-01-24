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