import schedule
import time
from datetime import datetime
from news_service import AlaskaNewsService
from email_service import EmailService

class DailyScheduler:
    """Scheduler to send daily news emails."""
    
    def __init__(self, email_service: EmailService, news_service: AlaskaNewsService, 
                 recipient_email: str, send_time: str, top_words_count: int = 20):
        self.email_service = email_service
        self.news_service = news_service
        self.recipient_email = recipient_email
        self.send_time = send_time
        self.top_words_count = top_words_count
    
    def send_daily_news(self):
        """Fetch news, analyze, and send email."""
        print(f"Starting daily news analysis at {datetime.now()}")
        
        # Fetch and analyze news
        analysis = self.news_service.fetch_and_analyze(self.top_words_count)
        
        if analysis['news_count'] == 0:
            print("No news found. Skipping email.")
            return
        
        # Send email
        subject = f"Alaska Daily News Summary - {datetime.now().strftime('%B %d, %Y')}"
        success = self.email_service.send_email(self.recipient_email, subject, analysis)
        
        if success:
            print(f"Daily news sent successfully at {datetime.now()}")
        else:
            print(f"Failed to send daily news at {datetime.now()}")
    
    def start(self):
        """Start the scheduler."""
        # Schedule daily task
        schedule.every().day.at(self.send_time).do(self.send_daily_news)
        
        print(f"Scheduler started. Will send daily news at {self.send_time}")
        print(f"Recipient: {self.recipient_email}")
        print("Press Ctrl+C to stop.")
        
        # Run scheduler
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
