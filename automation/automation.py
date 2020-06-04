import re
from faker import Faker
import shutil
fake = Faker('en_US')
# references 
# https://automatetheboringstuff.com/chapter7/

def fake_file():
    
    content = ''

    for _ in range(200):
        content += fake.paragraph()
        content += fake.email()
        content += fake.paragraph()
        content += fake.phone_number()
        content += fake.paragraph()

        content += '\n'

        return content
content_1 = fake_file()
    
# breakpoint()
for phone_numbers in content_1:
    
    with open('phone_numbers.txt', 'w+') as f:
        phone_number_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
        # (r'\d{3}-\d{3}-\d{4}')
        # mo variable name is a generic name to use for match objects
        # the findall() will not return a match object but a list of strings
        mo = phone_number_regex.search(content_1)
        
        mo.group()
        # find_all = phone_number_regex.findall(content_1)
        # print(find_all)
        # f.write(find_all)
        # print(mo.group())
        f.write(mo.group())
    shutil.copy('phone_numbers.txt', './assets/phone_numbers.txt')
    
    # print(reg[int(content_1)])

content_2 = fake_file()
with open('emails.txt', 'w+') as f:
    f.write(content_2)
shutil.copy('emails.txt', './assets/emails.txt')