import wikipedia

print(wikipedia.search("Barack"))
print(wikipedia.summary("GitHub"))
ny = wikipedia.page("New York")
print(ny.title)
print(ny.url)
