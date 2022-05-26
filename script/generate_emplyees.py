import datetime
import random 
import string
from ID_generate import IdNumber

def random_date():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2022, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)


pattern = "INSERT INTO bankmanage_employee (ID_card,fk_bank_id,fk_department_id,name,phone,address,entry_date) VALUES ('%s','%s','%s','%s','%s','%s','%s');\n"
first = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞'
last = ["奕辰","宇轩","浩宇","亦辰","宇辰","子墨","宇航","浩然","梓豪","亦宸","一诺","依诺","欣怡","梓涵","语桐","欣妍","可欣","语汐","雨桐","梦瑶"]
addr = 'USTC'

num = int(input('input num:'))
filename = input('input output filename(default out.txt)')
if filename == '':
    filename = 'out.txt'
file = open(filename,'w',encoding='utf-8')
banks = ['合肥分行','上海分行','北京分行','冈比亚分行']
for bid in range(len(banks)):
    fk_bank_id = banks[bid]
    for did in range(4):
        fk_depart_id = str(bid*4+did+1)
        for i in range(num):
            ID_card = IdNumber.generate_id(random.randint(0,1))
            name = ''.join(random.choices(first, k=1)) + random.choice(last)
            phone = ''.join(random.choices(string.digits, k=11))
            address = ''.join(random.sample(addr,len(addr))) + '{:0>3d}'.format(random.randint(1,100))
            entry_date = random_date()
            file.write(pattern%(ID_card,fk_bank_id,fk_depart_id,name,phone,address,entry_date))
file.close()