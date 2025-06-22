#capitalize : Task to make the first letter of every words as capital

def capitalize_words(text):
    return text.title()

if __name__ == "__main__":
    input_string = input("Enter a sentence: ")
    capitalized_string = capitalize_words(input_string)
    print("Capitalized Sentence:", capitalized_string)
