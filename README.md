Genie - Chat LLMs Simplified

Genie is a minimal web app built with Flask, designed to help users with limited technical knowledge interact with advanced chat models like ChatGPT. The app offers a simple, easy-to-use interface for communicating with powerful language models.
Features

    Simple and intuitive user interface
    Chat with language models like ChatGPT
    Easy setup using environment variables

Installation
Prerequisites

Make sure you have the following installed:

    Python 3.7+
    pip (Python package installer)

Steps

    Clone the repository
    Clone the repository to your local machine:

git clone https://github.com/yourusername/genie.git
cd genie

Install dependencies
Install the required Python packages using the requirements.txt file:

pip install -r requirements.txt

Set up environment variables
To interact with OpenAI’s API, you'll need to set your OPENAI_API_KEY.

    Option 1: Using a .env file
        Create a .env file in the root directory of your project.
        Add the following line:

    OPENAI_API_KEY=your-api-key-here

Option 2: Manually setting the environment variable

    You can also manually set the environment variable in your terminal:

        export OPENAI_API_KEY=your-api-key-here

    (For Windows, use set instead of export.)

Run the Flask app
Start the application with:

    python app.py

    The app should now be running at http://127.0.0.1:5000/.

Usage

Once the app is running, open a web browser and go to http://127.0.0.1:5000/. You can start chatting with the model by typing in the input box and receiving responses.
Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome!
License

This project is licensed under the MIT License - see the LICENSE file for details.
