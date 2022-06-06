from getGraph import useGraph

print('This is a simple quadratic function derivative calculator, enjoy!')

print("----------------------------------------")
print("This will create an explanation file, open it if you want to urderstand whats happening!")

def getDerivativesFile():
    file = open("derivatives.txt", "a")
    file.close()
    file = open("derivatives.txt", "r+")
    if file.read() == '':
        file.write("Yes i am the first text\n")
        file.close()
    else:
        file.write("MORE!\n")
        file.close()
        
getDerivativesFile()
useGraph()
