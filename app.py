from flask import Flask, render_template
import scrapW
app = Flask(__name__)

@app.route('/')
def index1():
    news_data=scrapW.link_data
    news_data2=scrapW.link_data2
    news_data3=scrapW.link_data3


    return render_template('index.html', news_data=news_data, news_data2=news_data2, news_data3=news_data3)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')





















    # news_sites=[
    # {'name':'Site 1','myURL':'https://www.cnet.com/tech/'}
    # ]


    # news_data = []
    # response = requests.get(site['url'])
    # soup = BeautifulSoup(response.content, 'html.parser')
            
    # # Extract the relevant information from the HTML
    # headlines = soup.find_all('h2', class_='headline')
    # summaries = soup.find_all('p', class_='summary')
    # links = soup.find_all('a', href=True)
            


    

    #for site in news_sites:






















# from flask import Flask, render_template
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Define the news sites you want to scrape
#     news_sites = [
#         {'name': 'Site 1', 'url': 'https://www.cnet.com/tech/'}
#         # {'name': 'Site 2', 'url': 'https://www.engadget.com/'},
#         # {'name': 'Site 3', 'url': 'https://www.wired.com/category/security/'},
#         # {'name': 'Site 4', 'url': 'https://mashable.com/tech'}
#     ]

#     news_data = []
    
#     # Scrape each news site
#     for site in news_sites:
#         try:
#             response = requests.get(site['url'])
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Extract the relevant information from the HTML
#             headlines = soup.find_all('h2', class_='headline')
#             summaries = soup.find_all('p', class_='summary')
#             links = soup.find_all('a', href=True)
            
#             # Store the extracted data in a dictionary
#             for headline, summary, link in zip(headlines, summaries, links):
#                 news_item = {
#                     'site': site['name'],
#                     'headline': headline.text.strip(),
#                     'summary': summary.text.strip(),
#                     'link': link['href']
#                 }
#                 news_data.append(news_item)
#         except:
#             # Handle any errors that occur during scraping
#             pass
    
#     return render_template('index.html', news_data=news_data)

# if __name__ == '__main__':
#     app.run(debug=True)
































# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return 'Thank you for contacting us...'



