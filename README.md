# Alaska Daily News 🗞️

A web application that searches for free news from Alaska and sends a summary with the most common words to your email once a day.

## Features

- 📰 Fetches news from Alaska news sources via RSS feeds
- 🔤 Analyzes and extracts the most common words from news articles
- 📧 Sends daily email summaries with word frequency analysis
- 🌐 Web interface to view news and word analysis in real-time
- ⏰ Automated daily scheduling for email delivery
- 🎨 Beautiful, responsive UI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kelstae/DailyNews.git
cd DailyNews
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example configuration file:
```bash
cp config.example.py config.py
```

2. Edit `config.py` with your email settings:
```python
# Email Configuration
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Use app-specific password for Gmail
EMAIL_RECIPIENT = "recipient@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Schedule Configuration
DAILY_SEND_TIME = "09:00"  # Send email at 9:00 AM daily

# Number of top words to extract
TOP_WORDS_COUNT = 20
```

### Gmail Setup

If using Gmail, you need to:
1. Enable 2-factor authentication on your Google account
2. Generate an app-specific password at https://myaccount.google.com/apppasswords
3. Use this app password in the `EMAIL_PASSWORD` field

## Usage

### Start the Web Application

```bash
python app.py
```

The application will:
- Start the web server at `http://localhost:5000`
- Launch the daily scheduler in the background (if configured)
- Send automated emails at the configured time each day

### Web Interface

Visit `http://localhost:5000` in your browser to:
- Fetch and view current Alaska news
- See word frequency analysis
- Manually trigger email sending
- View recent news headlines

### Manual News Fetching (without web server)

You can also use the services directly in Python:

```python
from news_service import AlaskaNewsService

news_service = AlaskaNewsService()
analysis = news_service.fetch_and_analyze(top_n=20)

print(f"Analyzed {analysis['news_count']} articles")
print(f"Top words: {analysis['top_words']}")
```

## How It Works

1. **News Fetching**: The app fetches news from Alaska news RSS feeds
   - Anchorage Daily News
   - Alaska's News Source (KTUU)

2. **Text Analysis**: 
   - Extracts text from news titles and descriptions
   - Removes HTML tags and special characters
   - Filters out common stop words (the, and, is, etc.)
   - Counts word frequency

3. **Email Generation**:
   - Creates an HTML email with:
     - Word frequency table
     - Recent news headlines
     - Links to full articles

4. **Scheduling**:
   - Uses Python's `schedule` library
   - Runs daily at configured time
   - Automatically fetches, analyzes, and emails

## Project Structure

```
DailyNews/
├── app.py                 # Flask web application
├── news_service.py        # News fetching and analysis
├── email_service.py       # Email sending functionality
├── scheduler.py           # Daily scheduling logic
├── config.py             # Configuration (create from config.example.py)
├── config.example.py     # Example configuration
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web interface template
└── README.md            # This file
```

## API Endpoints

- `GET /` - Web interface
- `GET /api/news?top_words=20` - Fetch and analyze news
- `POST /api/send-now` - Send email immediately

## Dependencies

- Flask - Web framework
- requests - HTTP library
- schedule - Job scheduling
- python-dotenv - Environment configuration
- beautifulsoup4 - HTML parsing
- feedparser - RSS feed parsing

## Troubleshooting

### Email not sending
- Verify your email credentials in `config.py`
- For Gmail, ensure you're using an app-specific password
- Check your firewall allows SMTP connections

### No news fetched
- Check your internet connection
- RSS feeds may be temporarily unavailable
- Try different news sources by modifying `news_service.py`

### Scheduler not running
- Ensure `config.py` is properly configured
- Check the console for error messages
- Verify the time format in `DAILY_SEND_TIME` (HH:MM)

## Contributing

Feel free to open issues or submit pull requests to improve the application!

## License

MIT License - feel free to use and modify for your needs. 
