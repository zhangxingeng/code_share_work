from pysymphony.tooling import LocalTool
from pysymphony.settings import settings

# Define the abbreviation lookup function
def lookup_abbreviation(abbreviation: str) -> str:
    """Looks up the full form of an abbreviation."""
    abbreviations = {
        'AI': 'Artificial Intelligence',
        'ML': 'Machine Learning',
        'NLP': 'Natural Language Processing',
        'CV': 'Computer Vision',
        'DL': 'Deep Learning',
        # Add more abbreviations as needed
    }
    return abbreviations.get(abbreviation, f"Unknown abbreviation: {abbreviation}")

# Register the abbreviation lookup function as a local tool
settings.add_local_tool(fn=lookup_abbreviation)

def agent():
    import re

    # Initialize conversation history
    conversation = []

    # User provides context with abbreviations
    context = input("User: ")
    conversation.append({'role': 'user', 'content': context})

    # Assistant processes the context
    while True:
        # Find abbreviations in the context (assumed to be all caps words)
        abbreviations_found = set(re.findall(r'\b[A-Z]{2,}\b', context))

        # Use the tool to expand abbreviations
        expanded = {}
        for abbr in abbreviations_found:
            full_form = lookup_abbreviation(abbr)
            expanded[abbr] = full_form

        # Enrich the context by replacing abbreviations with full forms
        enriched_context = context
        for abbr, full_form in expanded.items():
            enriched_context = enriched_context.replace(abbr, f"{full_form} ({abbr})")

        # Assistant composes an answer based on the enriched context
        answer = f"The enriched context is: {enriched_context}"
        print(f"Assistant: {answer}")
        conversation.append({'role': 'assistant', 'content': answer})

        # User checks if the answer is satisfactory
        feedback = input("User (Is the answer satisfactory? yes/no): ").strip().lower()
        conversation.append({'role': 'user', 'content': feedback})

        if feedback == 'yes':
            break
        else:
            # User provides additional context or corrections
            correction = input("User: ")
            conversation.append({'role': 'user', 'content': correction})
            # Update the context with the new information
            context += " " + correction

    # Print the conversation history
    print("\nConversation History:")
    for msg in conversation:
        print(f"{msg['role'].capitalize()}: {msg['content']}")

# Run the agent
agent()
