user_input = input("Введіть текст який ви хочете перетворити на #: ")
import string

def generate_hashtag(text):
    text = ''.join(c for c in text if c not in string.punctuation).title().replace(" ", "")
    return "#" + text[:140]
print(f"{user_input} -> {generate_hashtag(user_input)}")
