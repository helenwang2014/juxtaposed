'''
import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print "\n" "The difference comparision between text1 and text2 line_by_line"
print '\n'.join(diff)

'''



import difflib

file1 = raw_input("Enter the name of file1: ")

file2 = raw_input("Enter the name of file2: ")



diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())


print "The difference comparision between file1 and files2 is as follows"


	

print ''.join(diff)


