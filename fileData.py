import csv
import re

data = []

def normalize(num):
  if (sum(c.isdigit() for c in num) < 10):
    return None
  elif re.match('(\+?){1}([0-9]+)(-)([0-9]+)-([0-9]+)-([0-9]+)', num):
    if ('+1' in num):
      phone_num = num.strip('+1-')
    elif ('+' not in num):
      phone_num = "+" + num
  elif re.match('([0-9]{10})', num): 
    phone_num = num[0:3] + '-' + num[3:6] + '-' + num[6:] 
  else: 
    phone_num = num.strip('(').replace(')','-').replace('.', '-')
  
  phone_num = phone_num.replace('x', ' ext. ')

  return phone_num
  
with open('A.csv','r') as f_obj: 
    reader = csv.reader(f_obj)
    header = next(reader)

    for line in reader:
      key, first_name, last_name, _  = line
      first_name = None if first_name == "" else first_name
      last_name = None if last_name == "" else last_name
      phone_num = normalize(line[3])
      contact = {"id": key, "firstName": first_name, "lastName": last_name, "phoneNum": phone_num}
      data.append(contact)

