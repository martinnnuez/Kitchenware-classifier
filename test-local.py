import requests

# Locally deployment
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

# AWS deployment
# url = " https://j8yf18moi7.execute-api.us-east-1.amazonaws.com/test/predict"

# Example image
# data = {'url': 'https://storage.googleapis.com/kagglesdsdata/competitions/42532/4724339/images/0000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20221207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221207T161008Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=2603df96a71f8ef00d6bea2e1540626e057b8874de18601df650ef695d6a677f7705ca0397cfd6c8f0c55d87c250db99ae4551065907e0e734e61beb0a7f2d8fcab9c099c49c7ff14fb69f784c57b45865360f49559b8913ffa6b777238085091738ad6af68561f96dbd571b7dbf31f797424ad05e1b808c979674f8b2eafc43924824812b71b1710b5e8bddcf6426e98bd9195b1cb1da9b6493e5ee2cb03d19f8a76cfa292b29672f5052b13925ce38e0185924f048a0f1e398776f6e0cb1bca879ed239f52e2a300b2752fe3cf89d2d9ffd5724d9cc10aa344b66328e9bf372e9f5aeb8a0ec3e5c22af607f4c8cd217bc0843ee16b8cd44954d2173c937c2b'}

data = {'url': ''}

result = requests.post(url, json=data).json()
print(result)
