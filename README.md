# Trava URL Shortener
This problem requires both technical and strategic thinking. Here's how I would approach it:

Step 1: Understanding the Problem & Gathering Requirements
- First, I’d acknowledge the CEO’s concern and ask follow-up questions:
- How short is “short”?
- Is preserving readability important, or just reducing length?
- How often are these links shared?
- Are there security concerns about exposing filter details?

Step 2: Possible Approaches
- There are multiple ways to approach URL shortening:
- Encoding Parameters Efficiently

  * Convert query parameters into a more compact, encoded format (e.g., Base64, Hashids).
  * Example:
    https://app.coolcompany.com/users?short=abc123 
- URL Shortener Service (Backend-Driven)
  * Store full query parameters in a database and return a short ID.
  * Example:
    https://app.coolcompany.com/u/xyz789 
- Compression Techniques
- Use URL-safe compression like Brotli to minimize space.
  * Client-Side Storage
  * Store filters in LocalStorage and reference them via a short token in the URL.

Step 3: Choosing an Approach
- If filters are frequently reused, option 2 (Shortener Service) is ideal.
- If sharing links externally is a rare need, option 1 (Encoding) might be better.
- Given that this is an internal app, I lean towards option 2, as it’s scalable.
  
Step 4: Implementation Plan
Step 4.1: Backend API for URL Shortening
- Create an API to store and retrieve filter states.
Step 4.2: Frontend Integration
- Modify how the table generates URLs to use the short URL format.
Step 4.3: Testing & Monitoring
- Ensure unit tests cover encoding/decoding.
- Add monitoring (e.g., track how often short URLs are used).

Step 5: Code Implementation
- I'll create a Python FastAPI service for this feature.

- Next Steps
* Deployment
* Deploy this service to AWS Lambda or a small Flask/Gunicorn server.
* Integration into Frontend
* Modify the table page to use the /shorten endpoint.
* Performance & Scaling
* Move storage from in-memory to Redis or a database.
* Security Considerations
* Ensure sensitive data isn’t exposed in the stored filters.

## API Endpoints

### `POST /shorten`
- Request Body: JSON representing filter/sort state
- Response: Short URL with unique identifier

### `GET /expand/{id}`
- Path Parameter: ID returned by `/shorten`
- Response: Original filter/sort state JSON

## How to Run Locally
```bash
git clone <your-repo-url>
cd trava-url-shortener
pip install -r requirements.txt
uvicorn app.main:app --reload
```

