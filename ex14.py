# Getting user input and Passing it along

from sys import argv

k=__name__
name=input('\nWhat\'s your name,please..?\n>')

print('Hi {0},Am running from {1}'.format(name,k))
print('--->I\'d like to ask thee a few Questions.')
likes=input('\nDo you really like Me..?\n>')

lives=input('Where do you live..?\n>')
comp=input('What make of a comp are you using..?\n>')

print('''
SO you said {0} about liking me.
You live in {1}. Not sure where that is.
And you have {2} computer.
Thanks {3}.
'''.format(likes,lives,comp,name))
