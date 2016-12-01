#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/11

import sys
import re

def increment_1(input):
  password = ""
  new_pass = []
  end_loop = False
  re_iol = re.compile("[iol]")
  re_dubs = re.compile('.*(.)\\1.*(.)\\2.*')
  #reverse the password to do the maths
  password = input[::-1]
  #a = 97, z = 122
  #increment first char by 1. if z, set to a, then carry the 1
  for char in password:
      new_pass.append(ord(char))
  while True:
    #convert old password into ints
    for x,char in enumerate(new_pass):
      if char >= 97 and char < 122:
        new_pass[x] += 1
        break
      new_pass[x] = 97
    #deconvert new password from ints to chars and anti-reverse
    password = ""
    for char in reversed(new_pass):
      password += chr(char)
    if re.match(re_iol, password):
      continue
    if not re.match(re_dubs, password):
      continue
    x=0
    while x < len(password[:-2]):
      if ord(password[x])+1 == ord(password[x+1]) and ord(password[x])+2 == ord(password[x+2]):
        #print password + " passed straight test"
        end_loop = True
        #print str(ord(password[x])) + " " + str(ord(password[x+1])) + " " + str(ord(password[x+2])) + "  failed test"
      x+=1
    if end_loop:
      break
    password = ""
  return password

def pass_change(filename):
  password = ""
  #return a lowercase 8char string
  input = open(filename, 'rU').read()
  print "Santa's old password is: " + input
  password = input
  password = increment_1(password)
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