#import webbrowser
#webbrowser.open('https://inventwithpython.com/')

import webbrowser,sys
if len(sys.argv)> 1:
    address=''.join(sys.argv[1:])
    url=f"https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/"
    webbrowser.open(url)