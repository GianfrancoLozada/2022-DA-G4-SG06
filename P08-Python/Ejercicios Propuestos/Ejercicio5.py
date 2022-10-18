filename = "Ejercicios.py"
with open(filename) as filel:
    lines = filel.readlines ()
for line in lines:
    print (line.rstrip())
print(len(lines))
print("Clientito\n in lines") 
print(lines.count("Clientito\n"))