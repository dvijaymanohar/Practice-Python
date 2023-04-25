import sys
# Import the os module
import os

a = 'c:\\'
b = 'myFirstDirectory\\'
# print(os.path.join(a, b).replace('\\', '\'))


a = 'c:'
b = 'myFirstDirectory'
c = 'mySecondDirectory'
d = 'myThirdDirectory'
e = 'myExecutable.exe'

print(os.path.join('c:' + os.sep, 'myFirstDirectory', 'mySecondDirectory', 'myThirdDirectory', 'myExecutable.exe'))



# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))


print(os.path.join(cwd + os.sep + '..' + os.sep, 'myFirstDirectory', 'mySecondDirectory', 'myThirdDirectory', 'myExecutable.exe'))


# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))