# import os
# PROMPT = """
#         Respond to the next answer. Keep in mind that the query that is created must be explicit at all times from which table the feature comes.
#         Take in mind:
#         - Adding the table name when referencing columns that are specified in multiple table
#         - The limit of row is {number_rows}
#         {question}
#         """


# QUESTION_GENERATIVE_AI = "How many clients do I have?"
# API_KEY = "YOUR_KEY_HERE"
# # API_KEY = os.environ['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']
# # KEY_OPENAI = "yourkey"

# # or you can use API_KEY = os.environ['OPENAI_API_KEY']

import os
from dotenv import load_dotenv

# Try to load .env file only in local development
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dotenv_path = os.path.join(BASE_DIR, ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Get environment variables (Render will provide them automatically)
API_KEY = os.getenv("API_KEY")
NUMBER_ROWS = os.getenv("NUMBER_ROWS", "5")  # default = 5 if not set

PROMPT = f"""
        Respond to the next answer. Keep in mind that the query that is created must be explicit at all times from which table the feature comes.
        Take in mind:
        - Adding the table name when referencing columns that are specified in multiple table
        - The limit of row is {NUMBER_ROWS}
        {{question}}
        """

QUESTION_GENERATIVE_AI = "How many clients do I have?"