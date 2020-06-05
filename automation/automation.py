import re
from faker import Faker
import shutil
# from assets import potential_contacts
fake = Faker('en_US')
# references 
# https://automatetheboringstuff.com/chapter7/
# credit to TA James for helping me trouble shoot some issues

def fake_file():
    
    content = ''

    for _ in range(100):
        content += fake.paragraph()
        content += fake.email()
        content += fake.paragraph()
        content += fake.phone_number()
        content += fake.paragraph()
        content += fake.phone_number()

        content += '\n'
        # print(content)
        return content


  
for phone_numbers in range(100):
    content_1 = fake_file()
    with open('phone_numbers.txt', 'a+') as f:
        phone_number_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
        # (r'\d{3}-\d{3}-\d{4}')
        # mo variable name is a generic name to use for match objects 
        mo = phone_number_regex.search(content_1)
        # group() returns the actual matched text from the searched string
        try:
            mo.group()
            f.write(mo.group())
            f.write('\n')
        except:
            pass
        # print(mo.group())
        

        # the findall() will not return a match object but a list of strings
        # find_all = phone_number_regex.findall(content_1)
        # print(find_all)
        # f.write(find_all)
        
    shutil.copy('phone_numbers.txt', './assets/phone_numbers.txt')
    
    # print(reg[int(content_1)])

for emails in range(100):
    content_2 = fake_file()
    with open('emails.txt', 'a') as f:
        # source: https://www.regular-expressions.info/email.html
        # email_regex = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b')
        # source: https://www.geeksforgeeks.org/extracting-email-addresses-using-regular-expressions-python/
        email_regex = re.compile(r'\S+@\S+')
        mo = email_regex.search(content_2)
        try:
            mo.group()
            f.write(mo.group())
            f.write('\n')
        except:
            pass
        # print(mo)
        # mo.group()
        # f.write(mo.group())
    shutil.copy('emails.txt', './assets/emails.txt')