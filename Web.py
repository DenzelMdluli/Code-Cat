import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/south-africa/johannesburg"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract temperature (timeanddate.com uses <div class="h2"> for temp)
    temp = soup.find("div", class_="h2")
    if temp:
        print("Temperature:", temp.get_text(strip=True))
    else:
        print("Temperature not found")

    # Extract weather description (try alternative selector)
    desc = soup.find("p")  # just grab the first <p> as a fallback
    if desc:
        print("Condition:", desc.get_text(strip=True))
    else:
        print("Condition not found")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
