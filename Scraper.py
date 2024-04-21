import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
def main():
    productUrl = "https://www.amazon.com/Razer-Ornata-Gaming-Keyboard-Low-Profile/dp/B09X6GJ691/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1"
    page = 1
    failes = 0
    while True:
        print("Page: " + str(page))
        response = requests.get(getUrl(productUrl, page), headers=headers)
        page +=1
        if not response.status_code == 200:
            print(f"Request failed ({response.status_code}), move to next page")
            print(response)
            failes+=1
            if failes == 2:
                break
            continue   
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all('div', {'data-hook': 'review'})

        for review in reviews:
            try:
                author = review.find('span', {'class': 'a-profile-name'}).text.strip()
            except:
                author = None    
            try:
                rating = review.find('span', {'class': 'a-icon-alt'}).text.strip()
            except:
                rating = None    
            try:
                date = review.find('span', {'class': 'a-size-base'}).text.strip()
            except:
                date = None    
            try:
                text = review.find('span', {'data-hook': 'review-body'}).text.strip()
            except:
                text = None    
            try:
                verified = review.find('div', {'class': 'a-row a-spacing-mini review-data review-format-strip'}).a.text.strip()
            except:
                verified = None    
            try:
                style = review.find('div', {'class': 'a-row a-spacing-mini review-data review-format-strip'}).find("span",{"data-hook":"format-strip-linkless"}).text.strip()
            except:
                style = None    
            try:
                title = review.find('a', {'data-hook': 'review-title'}).find_all("span")[2].text.strip()
            except:
                title = None    
            scrapedAt = str(datetime.now())

            print(f"Author: {author}\nRating: {rating}\nDate: {date}\ntitle: {title}\nText: {text}\nVerified: {verified}\nStyle: {style}\nScrapedAt: {scrapedAt}")
            saveToCsv(author, rating, date, text, verified, style, title, scrapedAt)

        print("-"* 50)

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,*/*',
    'accept-language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

def getUrl(url, pageNum):
  review = url.replace("/dp/", "/product-reviews/") + "&pageNumber=" + str(pageNum)
  return url

def saveToCsv(author, rating, date, text, verified, style, title, scraped_at):
  # Check if the CSV file exists
  if not os.path.exists("reviews.csv"):
      # If not, create and write headers
      with open("reviews.csv", "w", newline="", encoding="utf-8") as file:
          writer = csv.writer(file, quoting=csv.QUOTE_ALL)
          writer.writerow(["Author", "Rating", "Date", "Text", "Verified", "Style", "Title", "ScrapedAt"])
  # Append new data with proper quoting
  with open("reviews.csv", "a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file, quoting=csv.QUOTE_ALL)
      writer.writerow([author, rating, date, text, verified, style, title, scraped_at])


if __name__ == "__main__":
  main()