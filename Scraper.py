from bs4 import BeautifulSoup
import csv
import requests
from random import choice

url = "https://www.amazon.com/Razer-Ornata-Gaming-Keyboard-\
Low-Profile/product-reviews/B09X6GJ691/ref=cm_cr_arp_d_p\
aging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pa\
geNumber=1"

def main():
    session = requests.Session()
    request = session.get(url, headers=headers)
    print(request.status_code)

    soup = BeautifulSoup(request.content, "html.parser")

    reviewsCount = soup.find("div", attrs={"data-hook":"cr-filter-info-review-rating-count"})
    print(reviewsCount.text.strip().replace(",","")[0:4])

    h3_tag = soup.find("h3", attrs={"data-hook": "arp-local-reviews-header"})
    print(h3_tag.text.strip())
    
def staticUserAgentRotator():
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
    "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    ]
    return choice(user_agents)

headers = {
    'accept': 'text/html,*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
    'device-memory': '4',
    'downlink': '9.65',
    'dpr': '1',
    'ect': '4g',
    'referer': url,
    'rtt': '250',
    'sec-ch-device-memory': '4',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-viewport-width': '1825',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': staticUserAgentRotator(),
    'viewport-width': '1825',
    'x-requested-with': 'XMLHttpRequest',
    }


if __name__ == "__main__":
    main()

