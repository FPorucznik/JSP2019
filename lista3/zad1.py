litera=input()
litera=litera.lower()
samogloski='eyoiaąęóu'
if samogloski.__contains__(litera):
    print("Twoja litera jest samogłoską")
else:
    print("Twoja litera jest spółgłoską")

