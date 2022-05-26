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
lpat = "INSERT INTO bankmanage_Loan (Loan_ID,fk_bank_id,money) values ('%s','%s','%.2f');\n"
ppat = "INSERT INTO bankmanage_payment (fk_loan_id,pay_date,pay_money) values ('%s','%s','%.2f');\n"
clpat = "INSERT INTO bankmanage_clientloan (fk_loan_id,fk_client_id) VALUES ('%s','%s');\n"

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
        #loan
        Loan_ID = ''.join(random.choices(string.ascii_uppercase,k=5)+random.choices(string.digits, k=20))
        money = random.randint(10000,1000000)
        file.write(lpat%(Loan_ID,fk_bank_id,money))
        #loan+client
        file.write(clpat%(Loan_ID,client))
        #支付
        pay_flag = random.randint(1,3)
        if pay_flag == 1:
            #不支付
            continue
        elif pay_flag == 2:
            #支付一半
            total_money = money/2
            mon = money/20
        else:
            #付清
            total_money = money
            mon = money/10
        already_mon = 0
        for tim in range(9):
            #10次支付
            file.write(ppat%(Loan_ID,random_date(),mon))
            already_mon += mon
        file.write(ppat%(Loan_ID,random_date(),total_money-already_mon))

file.close()