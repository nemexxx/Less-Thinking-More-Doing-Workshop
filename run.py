"""Open the site locally in your default browser.

Usage:  python3 run.py          -> opens the English page
        python3 run.py de       -> opens the German page
"""

import os
import sys
import webbrowser

page = "index-de.html" if "de" in sys.argv[1:] else "index.html"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), page)

webbrowser.open(f"file://{path}")
