from django.db import models

# Create your models here.

class Bank(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    city = models.CharField(max_length=50)
    assset = models.FloatField(default=0)

class Client(models.Model):
    ID_card = models.CharField(max_length=18,primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=11)
    c_email = models.CharField(max_length=100)
    c_relation = models.CharField(max_length=20)

class Department(models.Model):
    id = models.AutoField(primary_key=True)

    Depart_ID = models.CharField(max_length=20)
    fk_bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    dtype = models.CharField(max_length=20)

    class Meta:
        unique_together=("Depart_ID","fk_bank")

class Employee(models.Model):
    ID_card = models.CharField(max_length=18,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    entry_date = models.DateField()

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    employee = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    stype = models.CharField(max_length=20)

    class Meta:
        unique_together=("client","employee")

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    
    Account_ID = models.CharField(max_length=50)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    balance = models.FloatField(default=0)
    open_date = models.DateField()

    class Meta:
        unique_together=("Account_ID","fk_bank")

class StoreAccount(models.Model):
    id = models.AutoField(primary_key=True)
    
    Account_ID = models.CharField(max_length=50,null=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    balance = models.FloatField(default=0)
    open_date = models.DateField()
    rate = models.FloatField()
    currency_type = models.CharField(max_length=20)
    class Meta:
        unique_together=("Account_ID","fk_bank")

class CheckAccount(models.Model):
    id = models.AutoField(primary_key=True)
    
    Account_ID = models.CharField(max_length=50,null=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    balance = models.FloatField(default=0)
    open_date = models.DateField()
    overdraft =  models.FloatField(default=0)
    class Meta:
        unique_together=("Account_ID","fk_bank")

class OpenCheck(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)
    fk_account = models.ForeignKey(CheckAccount,models.CASCADE,null=True)
    last_access = models.DateField(auto_now=True)

    class Meta:
        unique_together=("fk_bank","fk_client")

class OpenStore(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)
    fk_account = models.ForeignKey(StoreAccount,on_delete=models.CASCADE,null=True)
    last_access = models.DateField(auto_now=True)

    class Meta:
        unique_together=("fk_bank","fk_client")

class Loan(models.Model):
    Loan_ID = models.CharField(max_length=50,primary_key=True)
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    money = models.FloatField(default=0)

class Payment(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    pay_date = models.DateField()
    pay_money = models.FloatField()

class ClientLoan(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)

    class Meta:
        unique_together=("fk_loan","fk_client")

"""
要求中写道，“每笔贷款用唯一的贷款号标识”，因此贷款不应该与某一个支行关联
class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    Loan_ID = models.CharField(max_length=50)
    money = models.FloatField(default=0)

    class Meta:
        unique_together=("fk_bank","Loan_ID")

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    Payment_ID = models.CharField(max_length=50)
    pay_date = models.DateField()
    pay_money = models.FloatField()

    class Meta:
        unique_together=("fk_bank","fk_loan","Payment_ID")

class ClientLoan(models.Model):
    id = models.AutoField(primary_key=True)
    
    fk_bank = models.ForeignKey(Bank,on_delete=models.SET_NULL,null=True)
    fk_loan = models.ForeignKey(Loan,on_delete=models.SET_NULL,null=True)
    fk_client = models.ForeignKey(Client,on_delete=models.PROTECT,null=True)

    class Meta:
        unique_together=("fk_bank","fk_loan","fk_client")
"""