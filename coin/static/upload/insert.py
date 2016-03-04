import pyodbc
import random
import string

from faker import Faker
from faker.providers import company, date_time, misc

faker = Faker()

faker.add_provider(company)
faker.add_provider(date_time)
faker.add_provider(misc)

def gen_randnum():

    return random.randint(1, 255)

def gen_randcls():

    return random.randint(100, 999)

def gen_randflg():

    return random.randint(0, 1)

def gen_randmrk():

    return gen_randflg()

def gen_randusr():

    candidates = string.letters + string.digits

    return ''.join((random.choice(candidates) for x in xrange(gen_randnum())))

def gen_randeml():

    pass    

cnxn = pyodbc.connect("DRIVER={SQL SERVER}; SERVER=localhost; DATABASE=#db_file_common; UID=sa; PWD=123456")

cursor = cnxn.cursor()

# sql = 'INSERT INTO table_maildata VALUES (%d, "%s", "%s", "%s", %d, "%s", %d, "%s", "%s", "%s", %d, "%s")'

sql = 'INSERT INTO table_maildata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

for i in xrange(8143414, 10000000):

    cursor.execute(sql, (i + 10, faker.name(),
                                 faker.email(),
                                 faker.company(),
                                 gen_randcls(),
                                 faker.language_code(),
                                 int(faker.year()),
                                 faker.country_code(),
                                 gen_randmrk(),
                                 faker.date_time(),
                                 gen_randflg(),
                                 faker.name()))
    
    cnxn.commit()

    print i



