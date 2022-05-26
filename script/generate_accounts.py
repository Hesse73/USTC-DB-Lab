import datetime
import json
import random 
import string

def random_date():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)
clients =json.load(open('ID_cards.json','r'))
spat = "INSERT INTO bankmanage_storeaccount (Account_ID,fk_bank_id,balance,open_date,rate,currency_type) values ('%s','%s','%.2f','%s','%.2f','%s');\n"
cpat = "INSERT INTO bankmanage_checkaccount (Account_ID,fk_bank_id,balance,open_date,overdraft) values ('%s','%s','%.2f','%s','%.2f');\n"
open_store = "INSERT INTO bankmanage_openstore (fk_account_id,fk_bank_id,fk_client_id,last_access) VALUES ((select id from bankmanage_storeaccount where Account_ID='%s' AND fk_bank_id='%s'),'%s','%s','%s');\n"
open_check = "INSERT INTO bankmanage_opencheck (fk_account_id,fk_bank_id,fk_client_id,last_access) VALUES ((select id from bankmanage_checkaccount where Account_ID='%s' AND fk_bank_id='%s'),'%s','%s','%s');\n"
num = int(input('input num:'))
filename = input('input output filename(default out.sql)')
if filename == '':
    filename = 'out.sql'
file = open(filename,'w',encoding='utf-8')
banks = ['合肥分行','上海分行','北京分行','冈比亚分行']
for bid in range(len(banks)):
    fk_bank_id = banks[bid]
    for i in range(num):
        client = clients.pop()
        account_ID = ''.join(random.choices(string.digits, k=20))
        balance = random.random()*100000
        open_date = random_date()
        rate = random.random()*10
        currency_type = ''.join(random.choices(string.ascii_uppercase,k=3))+'D'
        file.write(spat%(account_ID,fk_bank_id,balance,open_date,rate,currency_type))
        #还要选取对应的客户添加到openstore
        file.write(open_store%(account_ID,fk_bank_id,fk_bank_id,client,random_date()))
        account_ID = ''.join(random.choices(string.digits, k=20))
        balance = random.random()*100000
        open_date = random_date()
        overdraft = random.random()*10000
        file.write(cpat%(account_ID,fk_bank_id,balance,open_date,overdraft))
        #还要选取对应的客户添加到opencheck
        file.write(open_check%(account_ID,fk_bank_id,fk_bank_id,client,random_date()))

file.close()