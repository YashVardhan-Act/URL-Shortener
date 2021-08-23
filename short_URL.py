while True:
    import pyshorteners

    URL = input("Enter The URL: ")

    shortner = pyshorteners.Shortener()

    x = shortner.tinyurl.short(URL)

    print(x)