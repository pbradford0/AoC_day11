#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/11

import sys
import re

def increment_1(input):
  password = ""
  new_pass = []
  re_iol = re.compile("[iol]")
  re_dubs = re.compile('.*(.)\\1.*(.)\\2.*')
  #reverse the password to do the maths
  password = input[::-1]
  #a = 97, z = 122
  #increment first char by 1. if z, set to a, then carry the 1
  while True:
    #convert old password into ints
    for char in password:
      new_pass.append(ord(char))
    for x,char in enumerate(new_pass):
      if char >= 97 and char < 122:
        new_pass[x] += 1
        break
      new_pass[x] = 97
    #deconvert new password from ints to chars and anti-reverse
    password = ""
    for char in reversed(new_pass):
    password += chr(char)
    if not re.match(re_iol, password):
      if re.match(re_dubs, password):
          break
  
  return password

def pass_change(filename):
  password = ""
  
  #return a lowercase 8char string
  input = open(filename, 'rU').read()
  print "Santa's old password is: " + input
  password = input
  while True:
    password = increment_1(password)
    
    
  #re-reverse it now that the maths are done
  #password = password[::-1]
  return password

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