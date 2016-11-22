#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/11

import sys

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = pass_change(sys.argv[1])
  print "Santa's new password is: " + str(a)
  
  #b = longest_route(sys.argv[1])
  #print "The longest route is distance" + str(b)

if __name__ == '__main__':
  main()