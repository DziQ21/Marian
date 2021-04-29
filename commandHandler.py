
name="Marian"
def handleCommand(tekst):
    if(tekst.find(name)!=-1):
        tekst=tekst[tekst.find(name)::]
        print(tekst)