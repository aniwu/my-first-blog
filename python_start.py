#Schleifen
def hallo(name):
    print ('Hallo ' + name + '!')

people = ['Max*', 'Rosel', 'Vivien', 'Barbara', 'Anita']
for name in people:
    hallo (name)
    print ('Nächster Mensch!')

for i in range (0, 11, 2):
    print (i)