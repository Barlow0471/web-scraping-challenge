from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape_mars():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')
    for title in titles:
        print(title.text)

    news_p = soup.find_all('div', class_='article_teaser_body')
    for p in news_p:
        print(p.text)

    mars_dict = {
        'news_title': titles,
        'news_p': news_p
    }

    browser.quit()  

    return mars_dict