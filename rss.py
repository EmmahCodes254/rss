import feedparser
from dateutil.parser import parse

class RssFeed:
    def _init_(self):
        self.urls=[{
        "category":"Politics",
        "url":"https://www.standardmedia.co.ke/rss/politics.php"
        },
        {
        "category":"Columnists",
        "url":"https://www.standardmedia.co.ke/rss/columnists.php"
        },
        {"category":"Business",
        "url":"https://www.standardmedia.co.ke/rss/business.php",
        },
        {"category":"Eve Woman",
        "url":"https://www.standardmedia.co.ke/rss/evewoman.php"
        },
        
        {"category":"Sports",
        "url":"https://www.standardmedia.co.ke/rss/sports.php"
        }
        ]
        self.payload=[]
    def run(self):
        for a in self.urls:
            feed=feedparser.parse(a['url'])
            f=feed['entries']
            article_data={}

            for x in f:
                
                article_data['title']=x['title']
                article_data["link"]= x['id']
                article_data["published_date"]=parse(x['published'])
                article_data["summary"]=x['summary']
                media=x['media_content'][0]
                article_data["image_link"]=media['url']
            self.payload.append({"category":a['category'],"content":article_data})
    
    def response(self):
        return self.payload