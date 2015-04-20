#Dealing with Files

poem = '''
Programming is fun,
when the work is done,
if you wanna make your work also fun;
    use Python!
'''

f=open('poem.txt','w')# Open file for 'w'riting
f.write(poem) # Write txt to file
f.close() # Close file

f=open('poem.txt','r')# Default mode is 'r'ead
while True:
    line=f.readline()
    if len(line) == 0:#NB;NOTE the assignment operator(==)
        break
    print(line,end='')
f.close()
