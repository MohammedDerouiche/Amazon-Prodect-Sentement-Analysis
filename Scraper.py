from bs4 import BeautifulSoup
import csv
import requests

url = "https://www.amazon.com/Razer-Ornata-Gaming-Keyboard-\
Low-Profile/product-reviews/B09X6GJ691/ref=cm_cr_arp_d_p\
aging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pa\
geNumber=1"

headers = {
    'accept': 'text/html,*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
    # 'cookie': 'session-id=132-5380286-2647855; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:DZ"; ubid-main=130-3526901-0216751; lc-main=en_US; aws_lang=ar; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; s_cc=true; aws-target-visitor-id=1694998289712-328247; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1694998290226-75568; aws-ubid-main=743-3256657-5304547; regStatus=registering; s_sq=awsamazonallprod1%3D%2526pid%253DPayment%252520Information%2526pidt%253D1%2526oid%253Dfunctionnn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSPAN; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19633%7CMCMID%7C61061035914776301464369059959080113389%7CMCAID%7CNONE%7CMCOPTOUT-1696287337s%7CNONE%7CvVersion%7C4.4.0; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A952696918201%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22Mohammed%2520Derouiche%22%2C%22keybase%22%3A%22%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; skin=noskin; session-token=rF3gxVrpt2qlAaMOLjzKVUwYea/wpA3TFN3aFfIZo1IymgX7Nnn1pWOSKWXO7YBC+6o9dUAXgj4WxV3ZQOcbqIq41QEKbeIeGzJuLhAEnuqQiy2RFSs3sTux4iHkdJNR5qoOw0cLtyFWVgLeXi1cLEYb9UdQpEq/GesyGkSL1dKH72NGDJRkSot8rJ9qcfgoayqzi42EMihDxNnk73bqiM4iO8WqHRaszRPN2btxAa39nibj1I2MXxEqjY1yqHHHN+vKpIDOSs23sBtOhuvU4fB5JCmcjCjvGHRdzW1eFZJGyzs/GxtULq8vIM+H6G19XNkqu2HipgfFDifY/Nngh9UhFcTgmBaR; csm-hit=tb:s-N9WVABA8E3QHRJWZ138K|1713485900704&t:1713485902677&adb:adblk_yes',
    'device-memory': '4',
    'downlink': '9.65',
    'dpr': '1',
    'ect': '4g',
    'referer': 'https://www.amazon.com/Razer-Ornata-Gaming-Keyboard-Low-Profile/product-reviews/B09X6GJ691/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=3',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'viewport-width': '1825',
    'x-requested-with': 'XMLHttpRequest',
}
request = requests.get(url, headers=headers)
print(request.status_code)

soup = BeautifulSoup(request.content, "html.parser")

h3_tag = soup.find("h3", attrs={"data-hook": "arp-local-reviews-header"})
print(h3_tag.text.strip())