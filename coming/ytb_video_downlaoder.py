import webbrowser

url = input("Enter your YouTube URL : ")

url =url[:12]+'ss'+url[:12]
webbrowser.open(url)