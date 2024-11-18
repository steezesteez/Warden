
# Warden's Threshold

Warden's Threshold is an autonomous chatbot designed to retrieve data from APIs and provide intelligent responses.

## Features
- Pulls responses from an external API.
- Simple architecture with Flask.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Wardens_Threshold
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the chatbot server:
   ```bash
   python app.py
   ```

## Example
POST to `/chat` with JSON:
```json
{
  "message": "What is the weather?"
}
```

Response:
```json
{
  "reply": "It's sunny today."
}
```

## Deployment
Deploy with Docker or a cloud provider like Heroku.
