import random
import json

# Load quotes from a JSON file
def load_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Get a random quote
def get_random_quote(quotes):
    return random.choice(quotes)

if __name__ == "__main__":
    quotes = load_quotes("quotes.json")
    random_quote = get_random_quote(quotes)
    print(f"{random_quote['text']} - {random_quote['author']}")
