# 1. Write a program to find check if a string has only octal digits.
# Given string ['789', '123', '004']

import re
octal_strings = ['789', '123', '004']
def is_octal(s):
    return bool(re.fullmatch(r'[0-7]+', s))
for s in octal_strings:
    print(f"{s}: {is_octal(s)}")

# 2. Extract the user id, domain name and suffix from email addresses.
#'''emails="zuck@facebook.com",
#    "sunder33@google.com",
#   "jeff42@amazon.com" '''
    
import re
emails = [
    "zuck@facebook.com",
    "sunder33@google.com",
    "jeff42@amazon.com"
]
for email in emails:
    match = re.match(r'([^@]+)@([^@]+)\.([^@]+)', email)
    if match:
        user, domain, suffix = match.groups()
        print(f"User: {user}, Domain: {domain}, Suffix: {suffix}")

# 3. Split the following irregular sentence into proper words.

import re
sentence = "A, very   very; irregular_sentence"
words = re.split(r'[,;_\s]+', sentence.strip())
print(" ".join(words))  

# 4. Clean up the following tweet so that it contains only the user's message. 
#  That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
import re
tweet = """Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"""
tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'\bRT\b|\bcc:?', '', tweet)
tweet = re.sub(r'[!.,:;]', '', tweet)
tweet = re.sub(r'\s+', ' ', tweet).strip()
print(tweet)  


# 5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
#Code to retrieve the HTML page is given below:
#import requests
#r=requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here

import re
html = """
<html>
  <head><title>Your Title Here</title></head>
  <body>
    <h1>Link Name</h1>
    <h2>This is a Header</h2>
    <h3>This is a Medium Header</h3>
    <p>This is a new paragraph! </p>
    <p>This is a another paragraph!</p>
    <b>This is a new sentence without a paragraph break, in bold italics.</b>
  </body>
</html>
"""

texts = re.findall(r'>([^<>]+)<', html)
texts = [t.strip() for t in texts if t.strip()]
print(texts)


# 6. Given below list of words, identify the words that begin and end with the same
'''character.
  civic
  trust
  widows
  6
  M
  maximum
  museums
  aa
  as'''

import re
words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]
same_start_end = [w for w in words if re.fullmatch(r'(.).*\1', w)]
print(same_start_end)

