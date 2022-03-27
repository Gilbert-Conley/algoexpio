from email.mime import base


def remove_chars(base,chars):
    new_string = base
    for char in chars:
        new_string = new_string.replace(char,"")

    return new_string

result = remove_chars("hellow world","l")
print(result)