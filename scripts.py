#Import libraries
import os
import csv
import re

def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
  pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(pattern,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in
    the received address."""
  pattern = r''+old_domain + '$'
  address = re.sub(pattern,new_domain,address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  direccion_csv_archivo = "C:\\Users\\soria\\OneDrive\\Escritorio\\practice\\user_emails.csv"
  direccion_csv_nuevo ="C:\\Users\\soria\\OneDrive\\Escritorio\\practice\\new_user_emails.csv"

  old_domain_email_list = []
  new_domain_email_list = []

  old_domain='abc.edu'
  new_domain = 'nose.x'
  with open(direccion_csv_archivo) as f:
    user_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_list[1:]]
  
    for email in user_email_list:
      if contains_domain(email,old_domain):
        old_domain_email_list.append(email)
        email = replace_domain(email,old_domain,new_domain)
        new_domain_email_list.append(email)
        
    email_key = ' ' + 'Email Address'
    email_index = user_list[0].index(email_key)

    for user in user_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list,new_domain_email_list):
        if user[email_index] == ' '+old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  #We convert the list above in a .csv file

  with open(direccion_csv_nuevo,"w") as f:
    writer = csv.writer(f)
    writer.writerows(user_list)
      


main()
