import webbrowser
import random

links = ["https://www.youtube.com/watch?v=KQ6zr6kCPj8", "https://www.youtube.com/watch?v=KQ6zr6kCPj8", "https://www.youtube.com/watch?v=KQ6zr6kCPj8", "https://www.youtube.com/watch?v=KQ6zr6kCPj8", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=KQ6zr6kCPj8"]

print("Let's see if you're lucky. (press enter)")
input()
linkNum = random.randint(0, 5)

webbrowser.open(links[linkNum])
