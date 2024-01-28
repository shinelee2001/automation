import pyperclip
import re

text = str(pyperclip.paste())
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

result = (list(set(emails)))
print(result)