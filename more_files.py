from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))
in_file=open(from_file)
in_data=in_file.read()
print("input filr is %r bytes long" %(len(in_data)))
print("does the output file exists? %r " %(exists(to_file)))
print("ready to hit RETURN to continue,CNTRL-C to abort")
input("?")
out_file=open(to_file,'w')
out_file.write(in_data)
print("alright done")
in_file.close()
out_file.close()
