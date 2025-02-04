import re

def square_evens(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def find_long_words(words):
    return [word for word in words if len(word) > 3]

def convert_to_uppercase(names):
    return [name.upper() for name in names]

def find_first_letters(words):
    return [word[0] for word in words]

def regex_extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def regex_extract_phone_numbers(text):
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return re.findall(phone_pattern, text)

def regex_extract_capitalized_words(sentence):
    capital_pattern = r'\b[A-Z][a-z]*\b'
    return re.findall(capital_pattern, sentence)

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Squared evens:", square_evens(numbers))

    words = ["a", "an", "the", "python", "code", "AI"]
    print("Long words:", find_long_words(words))
    print("First letters:", find_first_letters(words))

    names = ["alice", "bob", "charlie"]
    print("Uppercase names:", convert_to_uppercase(names))

    text = "test@test.com, test.com, test@123"
    print("Extracted emails:", regex_extract_emails(text))

    phone_text = "Call 123-456-7890 or 987-654-3210 for support."
    print("Extracted phone numbers:", regex_extract_phone_numbers(phone_text))

    sentence = "Hello World, this Is a Test."
    print("Capitalized words:", regex_extract_capitalized_words(sentence))

    print("Running tests...")
    run_tests()
    print("All tests passed!")

def run_tests():
    assert square_evens([2, 4, 6]) == [4, 16, 36]
    assert find_long_words(["AI", "python", "code"]) == ["python", "code"]
    assert convert_to_uppercase(["alice", "bob"]) == ["ALICE", "BOB"]
    assert find_first_letters(["hello", "world"]) == ["h", "w"]
    assert regex_extract_emails("Emails: user@example.com, invalid-email, hello@domain.net") == ["user@example.com", "hello@domain.net"]
    assert regex_extract_phone_numbers("Reach me at 555-123-4567 or 444-987-6543.") == ["555-123-4567", "444-987-6543"]
    assert regex_extract_capitalized_words("Hello World, this Is a Test.") == ["Hello", "World", "Is", "Test"]

if __name__ == "__main__":
    main()
