
# %%
import requests
endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format('maxr')

payload = { 'apikey' :'YZDGQZLHYMYP9KZBLWYC6EWLMTGKQ4AF'}

content = requests.get(url = endpoint, params = payload)
data=content.json()
data

# %%
