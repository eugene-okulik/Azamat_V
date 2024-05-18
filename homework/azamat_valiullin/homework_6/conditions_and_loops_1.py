text = """
Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero
"""

words = text.split()
updated_text = []
for word in words:
    if "," in word:
        new_word = word.replace(",", "ing,")
    elif "." in word:
        new_word = word.replace(".", "ing.")
    else:
        new_word = word + "ing"
    updated_text.append(new_word)

print(" ".join(updated_text))
