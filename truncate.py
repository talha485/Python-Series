def truncate(text, max_len):
    if (len(text)>max_len):
        return text[:max_len] + "..."
    else:
        return text
text = input("Enter text :")
max_len = int(input("Enter max length : "))
result = truncate(text, max_len)
print(result)