# Copilot Instructions for DailyNews

## Project Overview
DailyNews is an automated system that sends daily news emails to subscribers. The project focuses on collecting, curating, and delivering news content via email on a scheduled basis.

## Project Goals
- Aggregate news from various sources
- Format and curate daily news digests
- Send personalized email newsletters to subscribers
- Maintain subscriber preferences and delivery schedules

## Coding Standards

### General Guidelines
- Write clear, self-documenting code
- Use meaningful variable and function names
- Keep functions small and focused on a single responsibility
- Add comments for complex logic or business rules
- Follow DRY (Don't Repeat Yourself) principle

### Style Preferences
- Use consistent indentation (2 or 4 spaces based on language convention)
- Prefer readability over cleverness
- Use async/await for asynchronous operations
- Handle errors gracefully with proper error messages

## Technology Stack
The specific technology stack will depend on implementation choices, but typical components may include:
- **Backend**: Python, Node.js, or similar for email processing and scheduling
- **Database**: PostgreSQL, MongoDB, or similar for storing subscriber data and preferences
- **Email Service**: SMTP, SendGrid, Mailgun, or similar for email delivery
- **Scheduling**: Cron jobs, task queues, or cloud-based schedulers

## Key Components

### News Aggregation
- Fetch news from configured sources (RSS feeds, APIs, web scraping)
- Parse and normalize news content
- Filter and categorize news items

### Email Generation
- Template-based email creation
- Personalization based on subscriber preferences
- Responsive HTML email design

### Subscriber Management
- Store and manage subscriber information
- Handle subscription/unsubscription requests
- Manage email preferences and frequency

### Delivery System
- Schedule daily email sends
- Handle bounce and delivery failures
- Track email opens and engagement (optional)

## Testing Guidelines

### Testing Best Practices
- Write unit tests for core business logic
- Test edge cases and error handling
- Mock external services (news APIs, email services) in tests
- Maintain test coverage for critical paths

### Test Structure
- Place tests in appropriate test directories
- Name test files clearly (e.g., `test_news_aggregator.py`, `email_service.test.js`)
- Use descriptive test names that explain what is being tested
- Follow AAA pattern: Arrange, Act, Assert

## Security Considerations
- Never commit API keys, credentials, or secrets to the repository
- Use environment variables for configuration
- Validate and sanitize user input
- Implement rate limiting for API calls
- Use secure email practices (SPF, DKIM, DMARC)

## Documentation
- Update README.md with setup instructions
- Document API endpoints and their usage
- Include examples for common use cases
- Document environment variables and configuration options

## Dependencies Management
- Keep dependencies up to date
- Document required versions
- Use lock files (package-lock.json, requirements.txt, etc.)
- Minimize dependencies when possible

## Error Handling
- Log errors with appropriate context
- Implement retry logic for transient failures
- Send alerts for critical failures
- Provide user-friendly error messages

## Performance Considerations
- Optimize database queries
- Implement caching where appropriate
- Handle large subscriber lists efficiently (batch processing)
- Monitor email delivery rates and performance
