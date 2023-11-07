import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

url = input("Enter the URL: ")

shortened_url = shorten_url(url)
print("Shortened URL:", shortened_url)
