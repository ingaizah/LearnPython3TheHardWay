# Strings and Text

x = "There are {0} types of people".format(10)
binary='binary'
do_not="don't"
y="Those who know {0} and those who {1}".format(binary,do_not)

print('\n',x) # x is a Variable Needs NO QUOTES IS NOT a String
print(y) #print('y') will SIMPLY print y not var rep by y

print('\nI said;{0}'.format(x))
print('I also said;{0}'.format(y))

funny=True
joke="\nKnock Knock joke ain't funny no more?!"
print(joke,funny)

w="This is the left side of ..."
e="a string with a right side"
print(w+e)
