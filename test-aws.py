import requests

# Locally deployment
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# AWS deployment
url = " https://j8yf18moi7.execute-api.us-east-1.amazonaws.com/test/predict"

# Example image
data = {'url': 'https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221212%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221212T152149Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=734c5c334ce764fd60340d524e4a50ec3e5e35b44850f43100da2e5d75efaf8dafc3ae5d82f3caee653aee184aa75cdc183e2587a5689b5d25c16f0d2ead957e15f579305c68448331b63c8a78b1a67e67947cae95efb7dc75a1d8ad0ad8a20a41119cc7cfa9ca538be5658b279ac354d915be9bc6d125ff83b9c742cd1649d7dd53b29655b094b14077fa8e71ecaf03c8374d901ec4a20eb7768c4ec084994a265decfc02b49f48b9cddc685dffc8a328e7a1a909835136469410607f846a3f6d5f6f0ff0215d65256cfcc349a4fe08fc82890e76620b4e4e7584c4f61aa06ce8c529a98d906b88ff87fa2b89641f3cae5e0598a186523e7cce9ed96b07bcd7'}

# data = {'url': ''}

result = requests.post(url, json=data).json()
print(result)
