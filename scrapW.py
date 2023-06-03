#!/usr/bin/env python
# coding: utf-8

# In[136]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# In[ ]:


### 1. PCMag


# In[107]:


# Specify the URL of the tech news site you want to scrape
base_url = 'https://www.pcmag.com/'
url = 'https://example.com/tech-news'

# Send a GET request to the website
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the relevant elements containing the news links and titles
    links = soup.find_all('a', class_='font-bold text-base')

    # Create a list to store the href and data_item values
    link_data = []

    # Iterate over the links and extract the href and data_item attributes
    for link in links:
        # Extract the href
        href = link.get('href')
        
        # Append the base URL to the href using urljoin
        full_url = urljoin(base_url, href)
        
        # Extract the data_item value
        data_item = link.get('data-item')
        
        # Create a tuple to store the full_url and data_item
        link_tuple = (full_url, data_item)
        
        # Add the link tuple to the list
        link_data.append(link_tuple)

    # Print the scraped data
#     for link_tuple in link_data:
#         full_url, data_item = link_tuple
#         print('Full URL:', full_url)
#         print('Data Item:', data_item)
#         print('------------------------')
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)


# In[ ]:





# In[131]:


## 2. Wired


# In[ ]:





# In[143]:

#### 2. TECH_RADAR

# Specify the URL of the tech news site you want to scrape
base_url2 = 'https://www.techradar.com/'
url2 = 'https://example.com/tech-news'

# Send a GET request to the website
response2 = requests.get(base_url2)

# Check if the request was successful
if response2.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML
    soup2 = BeautifulSoup(response2.text, 'html.parser')

    # Find the relevant elements containing the news links and titles
    links2 = soup2.find_all('a', class_='article-link')

    # Create a list to store the href and data_item values
    link_data2 = []

    # Iterate over the links and extract the href and data_item attributes
    for link2 in links2:
        # Extract the href
        href2 = link.get('href')
        
        # Append the base URL to the href using urljoin
        full_url2 = urljoin(base_url2, href2)
        
        # Extract the data_item value
        data_item2 = link2.get('aria-label')
        
        # Create a tuple to store the full_url and data_item
        link_tuple2 = (full_url2, data_item2)
        
        # Add the link tuple to the list
        link_data2.append(link_tuple2)

    # Print the scraped data
#     for link_tuple in link_data:
#         full_url, data_item = link_tuple
#         print('Full URL:', full_url)
#         print('Data Item:', data_item)
#         print('------------------------')
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)


# In[146]:



### 3. CNET






# Specify the URL of the tech news site you want to scrape
base_url3 = 'https://www.cnet.com/tech/'
url3 = 'https://example.com/tech-news'

# Send a GET request to the website
response3 = requests.get(base_url3)

# Check if the request was successful
if response3.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML
    soup3 = BeautifulSoup(response3.text, 'html.parser')

    # Find the relevant elements containing the news links and titles
    links3 = soup3.find_all('a', class_='o-linkOverlay')[:10]

    # Create a list to store the link data
    link_data3 = []
    
    for link3 in links3:
        # Extract the href and text
        href3 = link3.get('href')
        text3 = link3.get_text(strip=True)
        
        # Join the base URL and href to create the full URL
        full_url3 = urljoin(base_url3, href3)
        
        # Create a tuple to store the full URL and text
        link_tuple3 = (full_url3, text3)
        
        # Add the link tuple to the list
        link_data3.append(link_tuple3)

    # Return the link data
    #return link_data3

else:
    print('Failed to retrieve the web page. Status code:', response3.status_code)
    # Return an empty list or handle the error accordingly
    #return []





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[128]:


# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin


# In[94]:


# pcmag_url ="https://www.pcmag.com/"




# #wired
# #pcMag
# #forbes


# In[95]:


# r=requests.get(pcmag_url)


# In[96]:


# htmlContent=r.content


# In[97]:


# soup=BeautifulSoup(htmlContent,'html.parser')


# In[98]:


# links = soup.find_all('a',class_="font-bold text-base")
# print(links)


# In[99]:


# print(htmlContent)


# In[100]:


#parsing the html


# In[101]:


# links=list(links)


# In[102]:


# print(links[3])


# In[103]:


# link_data=[]


# In[104]:


# for links in link_data:
#     titles=links['data-item']
#     href=links['href']
#     link_tuple(titles,href)
#     link_data.append(link_tuple)


# In[105]:


# for link_tuple in link_data:
#     titles,href=link_tuple
# #     print('titles',titles)
#     print('href',href)
#     print('------------')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[85]:


# print(soup.prettify)


# In[86]:


# title=soup.nav


# In[87]:


# print(title)


# In[88]:


# paras=soup.find('p',class_="mt-2").get_text()


# In[89]:


# print(paras)


# In[79]:


# for i in range(10):
#     print(i)


# In[91]:


# anchors=soup.find('a',class_="font-bold text-base")
# all_links=set()


# In[92]:


# print(all_links)


# In[ ]:





# In[93]:


# for link in anchors:
#     if(link != '#'):
#         linkText="https://codewithharry.com" +link.get('href')
#         all_links.add(link)
#         print(linkText)


# In[ ]:




