import tiktoken

def test_tiktoken_encoding(encoding_name: str, test_text: str):
    try:
        # Attempt to fetch the encoding
        print(f"Trying to fetch encoding for: {encoding_name}")
        enc = tiktoken.get_encoding(encoding_name)
        
        # Encode and decode a test string
        print(f"Encoding the text: {test_text}")
        encoded = enc.encode(test_text)
        print(f"Encoded tokens: {encoded}")

        decoded = enc.decode(encoded)
        print(f"Decoded text: {decoded}")
        
        # Check if decoded text matches the original
        if decoded == test_text:
            print("Success: Decoded text matches the original.")
        else:
            print("Error: Decoded text does NOT match the original.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide encoding name and test text
test_encoding_name = "cl100k_base"  # Replace with the encoding you're using
test_text = "Hello, this is a test string!"  # Replace with your test string

# Run the test
test_tiktoken_encoding(test_encoding_name, test_text)
