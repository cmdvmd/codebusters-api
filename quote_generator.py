with open('quotes.txt', 'r', encoding='utf-8') as quotes_file:
    quotes = [line.strip() for line in quotes_file.readlines()]
