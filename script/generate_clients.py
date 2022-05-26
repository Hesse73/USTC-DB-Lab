import random 
import string
import json
from ID_generate import IdNumber

pattern = "INSERT INTO bankmanage_client (ID_card,name,phone,address,c_name,c_phone,c_email,c_relation) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');\n"
relations = ['亲属','朋友','同学','师生','雇佣','战友','同事']
first = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞'
last = ["奕辰","宇轩","浩宇","亦辰","宇辰","子墨","宇航","浩然","梓豪","亦宸","一诺","依诺","欣怡","梓涵","语桐","欣妍","可欣","语汐","雨桐","梦瑶"]
addr = 'USTC'
ids = []
num = int(input('input num:'))
filename = input('input output filename(default out.sql)')
if filename == '':
    filename = 'out.sql'
file = open(filename,'w',encoding='utf-8')
for i in range(num):
    ID_card = IdNumber.generate_id(random.randint(0,1))
    ids.append(ID_card)
    name = ''.join(random.choices(first, k=1)) + random.choice(last)
    phone = ''.join(random.choices(string.digits, k=11))
    address = ''.join(random.sample(addr,len(addr)))
    c_name = ''.join(random.choices(first, k=1)) + random.choice(last)
    c_phone = ''.join(random.choices(string.digits, k=11))
    c_email = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3,10)))+'@banksys.com'
    c_relation = relations[random.randint(0,len(relations)-1)]
    file.write(pattern%(ID_card,name,phone,address,c_name,c_phone,c_email,c_relation))
file.close()
json.dump(ids,open('ID_cards.json','w'))