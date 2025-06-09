import webbrowser
import os

# Full path to the HTML file
file_path = os.path.abspath("/Users/emelyjunker/Documents/Programming/Improv/index.html")
webbrowser.open(f"file://{file_path}")