# Configuration file example
# Copy this file to config.py and fill in your details

# Email Configuration
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Use app-specific password for Gmail
EMAIL_RECIPIENT = "recipient@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# News API Configuration (Optional)
# Get a free API key at https://newsapi.org
# If not provided, will use RSS feeds or demo news
NEWSAPI_KEY = None  # or "your-newsapi-key-here"

# Schedule Configuration (time in 24-hour format)
DAILY_SEND_TIME = "09:00"  # Send email at 9:00 AM daily

# Number of top words to extract
TOP_WORDS_COUNT = 20

# Flask Configuration
SECRET_KEY = "your-secret-key-here"
DEBUG = True
