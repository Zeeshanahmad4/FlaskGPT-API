# FlaskGPT-API

FlaskGPT-API is a Python microservice built using the Flask framework that empowers developers to smoothly integrate ChatGPT services into their applications for end-users. It not only manages the authentication token but also modifies the incoming requests before routing them to the ChatGPT API. By leveraging this microservice, developers can avoid exposing their API keys to users, thereby offering a secure means to introduce ChatGPT functionalities into their apps.

## Key Features

- User authentication.
- Secured handling of ChatGPT API requests with OpenAI.
- SQLite database to store user data, conversation logs, and authentication details.
- Usage of Celery tasks to asynchronously manage resource-demanding tasks.
- Comprehensive logging for future analysis and improvement.
- Supports both free and premium subscription tiers, each with its own usage restrictions.

## Installation

To install FlaskGPT-API, follow these steps:

1. Clone the repository:

bashCopy code

`git clone https://github.com/yourusername/flaskgpt-api.git` 

2. Navigate into the cloned directory:

bashCopy code

`cd flaskgpt-api` 

3. Install the necessary dependencies:

bashCopy code

`pip install -r requirements.txt` 

4. Make sure to insert your OpenAI API key into the settings.py file:

pythonCopy code

`OPENAI_API_KEY = "your-openai-api-key"` 

5. Run the application:

bashCopy code

`python app.py` 

## API Endpoints

FlaskGPT-API can be interacted with via the following API endpoints:

1. Authenticate user: POST /authenticate/<email>/<password>
    
2. Process ChatGPT query: POST /query/<userid>/<chatid>/<account>/<deviceid>/<query>
    
3. Retrieve user chat: GET /chats/<userid>/<chatid>
    
4. Create a new user: POST /users/create
    

Please refer to the API documentation for more details on request and response structures.

## Requirements

- Flask
- Celery
- SQLite
- OpenAI

## Contributions

Your contributions are always welcome! Feel free to submit a pull request or raise an issue.

## License

This project is licensed under the terms of the MIT license.
