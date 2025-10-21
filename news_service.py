import feedparser
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from typing import List, Dict

class AlaskaNewsService:
    """Service to fetch and process Alaska news."""
    
    def __init__(self, newsapi_key: str = None):
        # NewsAPI key (optional - can use free tier at https://newsapi.org)
        self.newsapi_key = newsapi_key
        
        # RSS feeds for Alaska news sources
        self.news_feeds = [
            'https://www.adn.com/arc/outboundfeeds/rss/',  # Anchorage Daily News
            'https://www.alaskapublic.org/feed/',  # Alaska Public Media
            'https://www.newsminer.com/search/?f=rss',  # Fairbanks Daily News-Miner
        ]
        # Common words to exclude from word frequency analysis
        self.stop_words = {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
            'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
            'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their',
            'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go',
            'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know',
            'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them',
            'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
            'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work',
            'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these',
            'give', 'day', 'most', 'us', 'is', 'was', 'are', 'been', 'has', 'had',
            'were', 'said', 'did', 'having', 'may', 'should', 'am', 'being'
        }
    
    def fetch_news_from_newsapi(self) -> List[Dict[str, str]]:
        """Fetch news from NewsAPI about Alaska."""
        if not self.newsapi_key:
            return []
        
        news_items = []
        try:
            url = 'https://newsapi.org/v2/everything'
            params = {
                'q': 'Alaska',
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 20,
                'apiKey': self.newsapi_key
            }
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for article in data.get('articles', []):
                    news_items.append({
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'link': article.get('url', '')
                    })
        except Exception as e:
            print(f"Error fetching from NewsAPI: {e}")
        
        return news_items
    
    def fetch_news_from_rss(self) -> List[Dict[str, str]]:
        """Fetch news from RSS feeds."""
        news_items = []
        
        for feed_url in self.news_feeds:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:10]:  # Get top 10 from each feed
                    news_items.append({
                        'title': entry.get('title', ''),
                        'description': entry.get('summary', ''),
                        'link': entry.get('link', '')
                    })
            except Exception as e:
                print(f"Error fetching feed {feed_url}: {e}")
                continue
        
        return news_items
    
    def get_demo_news(self) -> List[Dict[str, str]]:
        """Get demo/sample Alaska news for testing."""
        return [
            {
                'title': 'Alaska Legislature Considers New Climate Policy',
                'description': 'The Alaska State Legislature is debating a comprehensive climate policy that addresses rising temperatures and their impact on local communities, wildlife, and the fishing industry.',
                'link': 'https://example.com/alaska-climate-policy'
            },
            {
                'title': 'Record Tourism Numbers in Anchorage This Summer',
                'description': 'Anchorage reported record-breaking tourism numbers this summer, with visitors from around the world coming to experience Alaska\'s natural beauty, wildlife, and outdoor adventures.',
                'link': 'https://example.com/anchorage-tourism'
            },
            {
                'title': 'Alaska Fisheries Report Strong Salmon Season',
                'description': 'Commercial fisheries across Alaska are reporting a strong salmon season, with healthy fish populations and good weather conditions contributing to successful harvests.',
                'link': 'https://example.com/alaska-salmon-season'
            },
            {
                'title': 'New Arctic Research Station Opens in Fairbanks',
                'description': 'A state-of-the-art Arctic research facility has opened in Fairbanks, focusing on climate change, permafrost studies, and indigenous community collaboration.',
                'link': 'https://example.com/fairbanks-research'
            },
            {
                'title': 'Alaska Airlines Expands Service to Remote Communities',
                'description': 'Alaska Airlines announced expanded flight service to remote Alaska communities, improving transportation and connectivity for residents in rural areas.',
                'link': 'https://example.com/alaska-airlines-expansion'
            },
            {
                'title': 'Wildlife Officials Monitor Bear Activity Near Urban Areas',
                'description': 'Alaska Department of Fish and Game officials are monitoring increased bear activity near populated areas, providing safety guidelines for residents and visitors.',
                'link': 'https://example.com/alaska-bear-safety'
            },
            {
                'title': 'Oil Production Numbers Show Steady Growth',
                'description': 'Alaska\'s oil production has shown steady growth this quarter, with new drilling technology and investment supporting the state\'s energy sector and economy.',
                'link': 'https://example.com/alaska-oil-production'
            },
            {
                'title': 'Indigenous Leaders Meet on Cultural Preservation',
                'description': 'Indigenous leaders from across Alaska gathered to discuss cultural preservation, language revitalization, and protecting traditional practices for future generations.',
                'link': 'https://example.com/alaska-cultural-preservation'
            }
        ]
    
    def fetch_news(self) -> List[Dict[str, str]]:
        """Fetch news from Alaska news sources."""
        news_items = []
        
        # Try NewsAPI first if available
        if self.newsapi_key:
            news_items = self.fetch_news_from_newsapi()
        
        # Try RSS feeds if no NewsAPI or as fallback
        if not news_items:
            news_items = self.fetch_news_from_rss()
        
        # Use demo news if nothing else works (for testing/demo purposes)
        if not news_items:
            print("Using demo news for demonstration purposes")
            news_items = self.get_demo_news()
        
        return news_items
    
    def extract_text(self, news_items: List[Dict[str, str]]) -> str:
        """Extract text from news items."""
        text = ""
        for item in news_items:
            text += " " + item.get('title', '')
            text += " " + item.get('description', '')
        return text
    
    def clean_text(self, text: str) -> str:
        """Clean text by removing HTML tags and special characters."""
        # Remove HTML tags
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and keep only letters and spaces
        text = re.sub(r'[^a-z\s]', ' ', text)
        
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def get_basic_words(self, text: str, top_n: int = 20) -> List[tuple]:
        """Extract most common words from text."""
        # Clean the text
        clean = self.clean_text(text)
        
        # Split into words
        words = clean.split()
        
        # Filter out stop words and short words
        filtered_words = [
            word for word in words 
            if word not in self.stop_words and len(word) > 3
        ]
        
        # Count word frequency
        word_counts = Counter(filtered_words)
        
        # Return top N words
        return word_counts.most_common(top_n)
    
    def fetch_and_analyze(self, top_n: int = 20) -> Dict:
        """Fetch news and analyze to get basic words."""
        news_items = self.fetch_news()
        
        if not news_items:
            return {
                'news_count': 0,
                'top_words': [],
                'news_items': []
            }
        
        text = self.extract_text(news_items)
        top_words = self.get_basic_words(text, top_n)
        
        return {
            'news_count': len(news_items),
            'top_words': top_words,
            'news_items': news_items[:5]  # Include top 5 news items
        }
