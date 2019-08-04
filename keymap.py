import getch

def doKeyEvent(key):
    if key == '\x00' or key == '\xe0': # non ASCII
       key = getch.getch() # fetch second character
    print(ord(key)),

def doQuitEvent(key):
    raise SystemExit


# First, clear the screen of clutter then warn the user 
# of what to do to quit
lines = 25 # set to number of lines in console
for line in range(lines): print

print("Hit space to end...")
print("")

# Now mainloop runs "forever"
while True:
   ky = getch.getch()
   length = len(ky)
   if length != 0:
      # send events to event handling functions
      if ky == " ": # check for quit event
         doQuitEvent(ky)
      else: 
         doKeyEvent(ky)