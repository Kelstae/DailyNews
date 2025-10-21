import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict

class EmailService:
    """Service to send emails with news analysis."""
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def create_email_body(self, analysis: Dict) -> str:
        """Create HTML email body from news analysis."""
        html = f"""
        <html>
            <body>
                <h2>Alaska Daily News Summary - {datetime.now().strftime('%B %d, %Y')}</h2>
                
                <h3>Top Words Found in Today's News</h3>
                <p>Analyzed {analysis['news_count']} news articles from Alaska sources.</p>
                
                <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
                    <tr style="background-color: #f2f2f2;">
                        <th>Rank</th>
                        <th>Word</th>
                        <th>Frequency</th>
                    </tr>
        """
        
        for idx, (word, count) in enumerate(analysis['top_words'], 1):
            html += f"""
                    <tr>
                        <td>{idx}</td>
                        <td><strong>{word}</strong></td>
                        <td>{count}</td>
                    </tr>
            """
        
        html += """
                </table>
                
                <h3>Recent News Headlines</h3>
                <ul>
        """
        
        for item in analysis['news_items']:
            html += f"""
                    <li>
                        <a href="{item['link']}">{item['title']}</a>
                    </li>
            """
        
        html += """
                </ul>
                
                <p style="margin-top: 30px; color: #666;">
                    <em>This is an automated daily news summary from Alaska news sources.</em>
                </p>
            </body>
        </html>
        """
        
        return html
    
    def send_email(self, recipient_email: str, subject: str, analysis: Dict) -> bool:
        """Send email with news analysis."""
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            
            # Create HTML body
            html_body = self.create_email_body(analysis)
            
            # Attach HTML content
            html_part = MIMEText(html_body, 'html')
            msg.attach(html_part)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            print(f"Email sent successfully to {recipient_email}")
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
