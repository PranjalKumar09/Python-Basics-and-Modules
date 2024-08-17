import requests
from bs4 import BeautifulSoup 


url = "http://www.google.com"

response = requests.get(url)

# print(response.url) # http://www.google.com
"""print(response.text) # <!doctype ...
# it copies all source code of given site 
"""

print(response.content) 

soup = BeautifulSoup(response.text , 'html.parser')

"""print(soup.prettify())  # it organizes all sourve code 
"""
"""for heading in soup.find_all('h2'):
    print(heading.text)
"""





