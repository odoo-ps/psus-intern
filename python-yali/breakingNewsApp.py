#review class

#exercise
from abc import ABC,abstractmethod
class Publisher(ABC):
    """this is Publisher interface class"""

    @abstractmethod
    def attach(self,subscriber):
        """Add a subscriber to the publisher"""
        pass

    @abstractmethod
    def detach(self,subscriber):
        """remove a subscriber to the publisher """   
        pass
  


class NewYorkTimesBreakingNews(Publisher):
    """this class extends Publisher interface class"""


    def __init__(self):
        """the constructor"""
        self._news_category=None
        self._news_title=None
        self._subscriber=[]


    def attach(self,subscriber):
        """this method will add a new subscriber"""
        self._subscriber.append(subscriber)


    def detach(self,subscriber):
        """this method will remove a subscriber"""
        self._subscriber.remove(subscriber)


    def publish_news_item(self,news_category,news_title):
        """
        this method will anounce the breaking news and
        also call the self notify method here

        """
        self._news_category=news_category
        self._news_title=news_title
        print(f"NYT: Breaking News: {self._news_title} [category={self._news_category}]")
        self.notify(self._news_category,self._news_title)


    def notify(self,news_category,news_title):
        """this method will notify the subscriber the breaking news"""
        print("NYT: Notifying subscribers...")
        self._news_category=news_category
        self._news_title=news_title
        for subscriber in self._subscriber:
            sub='BusinessNewsSubscriber'
            print()
            #sub().breaking_news(self._news_category,self._news_title)
            print()
            subscriber.breaking_news(self._news_category,self._news_title)


#subscriber
class Subscriber(ABC):
   """The Subscriber interface"""

   @abstractmethod
   def breaking_news(self,news_category,news_title):
      """get breaking news from publisher"""
      pass

class BusinessNewsSubscriber(Subscriber):
   """the concrete subscriber BusinessNewsSubscriber class"""

   def breaking_news(self,news_category,news_title):
      """React to category under business news only"""
      if(news_category=="business"):
          print(f"SUBSCRIBER: Business Breaking: {news_title}")
     
class PoliticsNewsSubscriber(Subscriber):
   """the concrete subscriber PoliticsNewsSubscriber class"""

   def breaking_news(self,news_category,news_title):
      """React to category under politics news only"""
      if(news_category=="politics"):
          print(f"SUBSCRIBER: Politics Breaking: {news_title}")

class KeyWordSubscriber(Subscriber):
   """the concrete subscriber KeyWordSubscriber class"""

   def  __init__(self,keyword):
       """the constrcutor take keyword as parameter"""
       self.keyword=keyword.lower()
       #print(self.keyword)

   def breaking_news(self,news_category,news_title):
      """React to keyword which is case insensitive on the news only"""
      if self.keyword in news_title.lower():
          print(f"SUBSCRIBER: Filter[{self.keyword}]: {news_title}")
    

nyt = NewYorkTimesBreakingNews()
subscriber_a = BusinessNewsSubscriber()
nyt.attach(subscriber_a)
subscriber_b =PoliticsNewsSubscriber()
nyt.attach(subscriber_b)
subscriber_c = KeyWordSubscriber("Chesa")
nyt.attach(subscriber_c)

nyt.publish_news_item("business", "Starbucks may close its bathrooms to the public again.")
nyt.publish_news_item("politics", "Chesa is out in San Francisco, but his agenda is alive in California.")

