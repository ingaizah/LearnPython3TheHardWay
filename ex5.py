#More Variables n Names
#NOTE the Escape Sequence \\\n

name='Ray N. Njau'
age=18 #NB;NOTE NO 'QUOTES'-its a consonant NOT a String
height=74 #inches
weight=57 #Kgs
eyes='blue'
teeth='white'
hair='black'

#print "Lets talk about %s." %name

print('\nMy name is {0}'.format(name))
print('I am {0} inches tall'.format(height))
print('I am {0} Kgs.'.format(weight))

print('\nI\'ve got {0} eyes and {1} teeth.'.format(eyes,teeth))
print('Pretty cute huh..?')
print('My hair is jungle {0} in colour.'.format(hair))
# NB;NOTE you don't have to break the string '',hair,'' with commas to
# insert/CALL the variable

print('\nIf I add {0},{1},and {2},I get {3}.'.format(age,height,weight,
                                                   age+height+weight))
