import requests
import json


q = """
{
  allPerros {
    edges {
      node {
        name
        years
        breed
      }
    }
  }
}
"""


resp = requests.post("http://localhost:5000/tails", params={'query': q})
jsonResponse = json.loads(resp.text)
print(jsonResponse)
print(jsonResponse['data']['allPerros']['edges'][1])