from snapchat import *
>>> me = SnapChat("leetraxler4021")
>>> me.check_username()
'sdushantha is already taken!'
>>> # Since the usename is taken, that means it is a valid username
>>> me.get_snapcode(bitmoji=False, size=500)
(..., 'PNG', '500x500')
>>> # The dotted part (...) is the raw data of the image
>>> # You use this data to write it into a file or do whatever you like