# Expanded glossary with 10 programming terms
glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A way to repeat a block of code multiple times.',
    'function': 'A block of reusable code that performs a specific task.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A sequence of characters enclosed in quotes.',
    'list': 'An ordered collection of items that is changeable.',
    'boolean': 'A data type that can be either True or False.',
    'tuple': 'An ordered, unchangeable collection of items.',
    'if statement': 'A control structure used to make decisions.',
    'comment': 'A line that is ignored by Python and used to explain code.'
}

# Loop through the dictionary and print each term and its meaning
for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")