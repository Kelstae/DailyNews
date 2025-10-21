from flask import Flask, render_template, jsonify, request
from news_service import AlaskaNewsService
from email_service import EmailService
from scheduler import DailyScheduler
import threading
import os

app = Flask(__name__)

# Load configuration
try:
    import config
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DEBUG'] = config.DEBUG
    
    # Initialize services
    news_service = AlaskaNewsService(newsapi_key=getattr(config, 'NEWSAPI_KEY', None))
    email_service = EmailService(
        smtp_server=config.SMTP_SERVER,
        smtp_port=config.SMTP_PORT,
        sender_email=config.EMAIL_SENDER,
        sender_password=config.EMAIL_PASSWORD
    )
    
    # Initialize scheduler
    scheduler = DailyScheduler(
        email_service=email_service,
        news_service=news_service,
        recipient_email=config.EMAIL_RECIPIENT,
        send_time=config.DAILY_SEND_TIME,
        top_words_count=config.TOP_WORDS_COUNT
    )
    
    config_loaded = True
except ImportError:
    print("Warning: config.py not found. Please copy config.example.py to config.py and configure it.")
    config_loaded = False
    news_service = AlaskaNewsService(newsapi_key=None)

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', config_loaded=config_loaded)

@app.route('/api/news')
def get_news():
    """API endpoint to fetch and analyze Alaska news."""
    try:
        top_words = request.args.get('top_words', 20, type=int)
        analysis = news_service.fetch_and_analyze(top_words)
        return jsonify({
            'success': True,
            'data': analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/send-now', methods=['POST'])
def send_now():
    """API endpoint to send email immediately."""
    if not config_loaded:
        return jsonify({
            'success': False,
            'error': 'Configuration not loaded. Please set up config.py first.'
        }), 400
    
    try:
        scheduler.send_daily_news()
        return jsonify({
            'success': True,
            'message': 'Email sent successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def start_scheduler():
    """Start the scheduler in a background thread."""
    if config_loaded:
        scheduler.start()

if __name__ == '__main__':
    # Start scheduler in background thread if config is loaded
    if config_loaded:
        scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
        scheduler_thread.start()
        print("Scheduler started in background thread")
    
    # Start Flask app
    app.run(debug=app.config.get('DEBUG', True), use_reloader=False)
