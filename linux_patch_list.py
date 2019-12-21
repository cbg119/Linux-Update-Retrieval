import sys
import platform
import subprocess

dist_name = ((platform.dist())[0]).lower()

#print hostname
print(platform.node())

#print ip address(es) , had to split due to Popen not liking |'s
addresses = subprocess.Popen(["ip", "a"], stdout=subprocess.PIPE)
addresses = subprocess.Popen(["grep", "inet"], stdin=addresses.stdout, stdout=subprocess.PIPE).communicate()[0]
print(addresses + "\n")

if dist_name == "ubuntu":
	try:
		subprocess.Popen(["apt", "update"], stdout=open("/dev/null", "w"), stderr=subprocess.STDOUT)
		upgrade_list = subprocess.Popen(["apt", "list", "--upgradable"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
	except:
		print("Error calling apt. Exiting...")
		sys.exit()

elif dist_name == "redhat" or dist_name == "centos" or dist_name == "oracle" or dist_name == "amazon linux ami":
	try:
		upgrade_list = subprocess.Popen(["yum", "list", "updates"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
	except:
		print("Error calling yum. Exiting...")
		sys.exit()

else:
	print("Unrecognized Distribution")
	sys.exit()

print(upgrade_list)
