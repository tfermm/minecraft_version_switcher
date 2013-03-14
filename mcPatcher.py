import urllib2
import os
valid = 'false'
print "WARNING: this program deletes your current minecraft.jar file"
print "Any mods you have installed into your minecraft.jar file will be lost\n"
while (valid == 'false'):
	print "Type a number than enter to make a selection"
	print "1 patch minecraft to 1.4.4"
	print "2 patch minecraft to 1.4.2"
	print "3 patch minecraft to 1.3.2"
	print "4 quit"
	choice = raw_input("Selection: ")
	if choice == '1':
		mcjar = urllib2.urlopen("http://assets.minecraft.net/1_4_4/minecraft.jar")
		version = "\x00\n1352902011000"
		valid = 'true'
	if choice == '2':
		mcjar = urllib2.urlopen("http://assets.minecraft.net/1_4_2/minecraft.jar")
		version = "\x00\n1351157607000"
		valid = 'true'
	elif choice == '3':
		mcjar = urllib2.urlopen("http://assets.minecraft.net/1_3_2/minecraft.jar")
		version = "\x00\n1345124077000"
		valid = 'true'
	elif choice == '4':
		valid = 'exit' 
	else:
		print "you didn't enter a valid option"
if valid == 'true':
	print "Patching..."
	path = os.environ.get('APPDATA')# using get will return `none` if key is not present rather than raise a `KeyError`
	path += '\\.minecraft\\bin\\'
	os.remove(path + 'minecraft.jar')
	os.remove(path + 'version')
	output = open(path + 'minecraft.jar','wb')
	output.write(mcjar.read())
	output.close()
	output = open(path + 'version','wb')
	output.write(version)
	output.close()
	print "Done"
else:
	print "Bye"
