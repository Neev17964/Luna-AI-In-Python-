from newsapi import NewsApiClient

# Initialize the NewsAPI client
newsapi = NewsApiClient(api_key='560e6b303371474bbc4bcc4ba0204248')

# Get available sources for India
sources = newsapi.get_sources(country='us')

# Print all the sources
for source in sources['sources']:
    print(source['name'], "-", source['url'])


# News API sources in India are:- 
# Google News (India) - https://news.google.com
# The Hindu - http://www.thehindu.com
# The Times of India - http://timesofindia.indiatimes.com


# News API sources in USA are:- 
# ABC News - https://abcnews.go.com
# Al Jazeera English - https://www.aljazeera.com
# Ars Technica - https://arstechnica.com
# Associated Press - https://apnews.com/
# Axios - https://www.axios.com
# Bleacher Report - http://www.bleacherreport.com
# Bloomberg - http://www.bloomberg.com
# Breitbart News - http://www.breitbart.com
# Business Insider - http://www.businessinsider.com
# Buzzfeed - https://www.buzzfeed.com
# CBS News - http://www.cbsnews.com
# CNN - http://us.cnn.com
# CNN Spanish - http://cnnespanol.cnn.com/
# Crypto Coins News - https://www.ccn.com
# Engadget - https://www.engadget.com
# Entertainment Weekly - http://www.ew.com
# ESPN - https://www.espn.com
# ESPN Cric Info - http://www.espncricinfo.com/
# Fortune - http://fortune.com
# Fox News - http://www.foxnews.com
# Fox Sports - http://www.foxsports.com
# Google News - https://news.google.com
# Hacker News - https://news.ycombinator.com
# IGN - http://www.ign.com
# Mashable - https://mashable.com
# Medical News Today - http://www.medicalnewstoday.com
# MSNBC - http://www.msnbc.com
# MTV News - http://www.mtv.com/news
# National Geographic - http://news.nationalgeographic.com
# National Review - https://www.nationalreview.com/
# NBC News - http://www.nbcnews.com
# New Scientist - https://www.newscientist.com/section/news
# Newsweek - https://www.newsweek.com
# New York Magazine - https://nymag.com/
# Next Big Future - https://www.nextbigfuture.com
# NFL News - http://www.nfl.com/news
# NHL News - https://www.nhl.com/news
# Politico - https://www.politico.com
# Polygon - http://www.polygon.com
# Recode - http://www.recode.net
# Reddit /r/all - https://www.reddit.com/r/all
# Reuters - https://www.reuters.com
# TechCrunch - https://techcrunch.com
# TechRadar - https://www.techradar.com
# The American Conservative - http://www.theamericanconservative.com/
# The Hill - https://thehill.com
# The Huffington Post - http://www.huffingtonpost.com
# The Next Web - http://thenextweb.com
# The Verge - http://www.theverge.com
# The Wall Street Journal - http://www.wsj.com
# The Washington Post - https://www.washingtonpost.com
# The Washington Times - https://www.washingtontimes.com/
# Time - http://time.com
# USA Today - http://www.usatoday.com/news
# Vice News - https://news.vice.com
# Wired - https://www.wired.com