import urllib2
import os
valid = 'false'
print "WARNING: this program deletes your current minecraft.jar file"
print "Any mods you have installed into your minecraft.jar file will be lost\n"
while (valid == 'false'):
	print "Type a number than enter to make a selection"
	print "1 patch minecraft to 1.4.2"
	print "2 patch minecraft to 1.3.2"
	print "3 quit"
	choice = raw_input("Selection: ")
	if choice == '1':
		mcjar = urllib2.urlopen("http://assets.minecraft.net/1_4_2/minecraft.jar")
		valid = 'true'
	elif choice == '2':
		mcjar = urllib2.urlopen("http://assets.minecraft.net/1_3_2/minecraft.jar")
		valid = 'true'
	elif choice == '3':
		valid = 'exit' 
	else:
		print "you didn't enter a valid option"
if valid == 'true':
	print "Patching..."
	path = os.environ.get('APPDATA')# using get will return `none` if key is not present rather than raise a `KeyError`
	path += '\\.minecraft\\bin\\'
	os.remove(path + 'minecraft.jar')
	output = open(path + 'minecraft.jar','wb')
	output.write(mcjar.read())
	output.close()
	print "Done"
else:
        print "Bye"
