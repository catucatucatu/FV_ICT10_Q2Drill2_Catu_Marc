from pyscript import document,display

display('Dance Club Members:', target="output1")
grade7 = {"Raven Denum", "Atrisha Cañedo", "Anissa Pauig", "Yñigo Sindo"} # set for Grade 7
grade8 = {"Amanda Gadia", "Jay Cañedo", "Mikhaell Sindo"} # set for Grade 8
grade9 = {"Lance Catu", "Ayr Dela Cruz", "Kirsten Caagbay"} # set for Grade 9
grade10 = {"Maiselle Marin", "Maria Coronel"} # set for Grade 10
masterset = grade7|grade8|grade9|grade10 # puts together all sets
display(sorted(masterset), target="output1") # displays original set
def addname(e):
    document.getElementById('output1').innerHTML = "" # clears the previous
    fname = document.getElementById('first').value.strip() # get first name and strip spaces
    lname = document.getElementById('last').value.strip() # get last name and strip spaces
    newname = fname + " " + lname # makes the full name
    masterset.add(newname) # adds it to the set
    display(sorted(masterset), target='output1') # displays new set
