import subprocess

#TODO
#Check in mac

if os.name == 'posix':
	proc = subprocess.Popen('which python3.7', stdout=subprocess.PIPE)
	python = proc.stdout.read()
	
if os.name == 'nt':
	
else:
	
	
