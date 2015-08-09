
from qrtools import QR
import sys
#import argparse

arg = sys.argv
code = QR(filename=arg[1])
if code.decode():
  print "QR decoded data is : ", code.data
  print code.data_type
  print code.data_to_string()