import os
import time

try:
raw_input('Executar "%s"? [Y/n]' % ''.join(map(lambda x: chr(x*4/8), [228, 218, 64, 90, 228, 204, 64, 94])))
except:
print "\nAdeus! "
import os, time
print "Executanto..."
time.sleep(3)
os.system("%s" % ''.join(map(lambda y: chr(y), map(lambda z: z*3/9, [102, 240, 174, 96, 324, 333, 324, 102, 96, 333, 312, 297, 303]))[::-1]))