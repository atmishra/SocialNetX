import requests,json

def get_status_of_text(text):

    headers = {'content-type': 'application/json'}
    url = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'

    data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    params = {'apikey': '67a570b1d8c91f9be817c8d4e82a521b9a6aeb71', 'text': text, 'outputMode': 'json'}
    
    try:

      res = requests.get(url, params=params)

      json_data = json.loads(res.text)
      
      sentiment = json_data['docSentiment']['type']

      score = json_data['docSentiment']['score']

 except:

      sentiment = 'neutral'
      score = '1.0'
        
    return (sentiment,score)