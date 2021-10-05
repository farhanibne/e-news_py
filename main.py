from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search('bangladesh')
result = googlenews.result()
for x in result:
    print("-"*50)
    print("Tittle--",x['title'])
    print("Date/Time--",x['date'])
    print("Description--",x['desc'])
    print("Link--",x['link'])