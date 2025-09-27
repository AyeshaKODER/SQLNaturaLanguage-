import os
PROMPT = """
        Respond to the next answer. Keep in mind that the query that is created must be explicit at all times from which table the feature comes.
        Take in mind:
        - Adding the table name when referencing columns that are specified in multiple table
        - The limit of row is {number_rows}
        {question}
        """


QUESTION_GENERATIVE_AI = "How many clients do I have?"
API_KEY = "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"
# API_KEY = os.environ['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']
# KEY_OPENAI = "yourkey"

# or you can use API_KEY = os.environ['OPENAI_API_KEY']
