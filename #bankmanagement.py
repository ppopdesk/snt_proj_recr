#bankmanagement
import random
from datetime import datetime

class PersonalInfo():
    def __init__(self,name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration, starting_date_of_scheme = datetime.now()):
        #initializing basic identification details of the applicant common to lenders and borrowers
        first,last = name.split(' ')
        self.first_name = first
        self.last_name = last
        self.id_numb = id_numb
        self.total_wealth = total_wealth
        self.scheme_type = scheme_type
        self.amount_deposited_or_loaned = amount_deposited_or_loaned
        self.scheme_duration = scheme_duration
        self.starting_date_of_scheme = starting_date_of_scheme
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    def id_number(self):
        return self.id_numb
    def wealth(self):
        return self.total_wealth
    def bank_id(self):
        #randomlygenerated alphanumeric code unique to an applicant
        return self.first_name+str(random.randint(10000, 99999))
    def print_all_details(self):
        print("Full Name : " + self.full_name())
        print("Wealth : " + str(self.wealth()))
        print("Bank ID : " + self.bank_id())
        print("Scheme Type : " + self.scheme_type)
        print("Term Duration : " + str(self.scheme_duration))
        print("Starting date : " + str(self.starting_date_of_scheme))

#the loaning service can add different schemes for lenders and borrowers
#here l_b_ is whether scheme is for lender or borrower
#the variable l_b_ can only take two values 'Lender Scheme' or 'Borrower Scheme'

class Schemes():
    #basic scheme details common to loan and fd schemes
    def __init__(self,interest_rate,l_b_,scheme_type):
        self.interest_rate = interest_rate
        self.l_b_ = l_b_
        self.scheme_type = scheme_type
    def __repr__(self):
        return "'{}' - '{}'  Interest Rate : {} ".format(self.l_b_,self.scheme_type,self.interest_rate)

class LenderSchemes(Schemes):
    Lender_Schemes = [] #all lender schemes are stored in this list (to be added by user)
    def __init__(self,interest_rate,l_b_,scheme_type_):
        super().__init__(interest_rate,l_b_,scheme_type_)
        LenderSchemes.Lender_Schemes.append(self)
    @staticmethod
    def interest_calc_fixed_deposit(scheme_type_,term_of_fd,principal_amount_):
        #we actually need to calculate interest using some interest calculating algorithm but it is just randomized here
        return random.randint(principal_amount_/100,principal_amount_/50)

class BorrowerSchemes(Schemes):
    Borrower_Schemes = [] #all borrower schemes are stored in this list (to be added by user)
    def __init__(self,interest_rate,l_b_,scheme_type):
        super().__init__(interest_rate,l_b_,scheme_type)
        BorrowerSchemes.Borrower_Schemes.append(self)
    @staticmethod
    def emi_calc_loan(scheme_type_,term_of_loan,principal_amount_):
        #we actually need to calculate emi using some emi calculating algorithm but it is just randomized here
        return random.randint(principal_amount_/100,principal_amount_/50)

class Borrower(PersonalInfo):
    borrowers_list = [] #all Borrower objects stored in this list
    
    def __init__(self,name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration, starting_date_of_scheme = datetime.now()):
        super().__init__(name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration, starting_date_of_scheme = datetime.now())
        for loan in BorrowerSchemes.Borrower_Schemes:
            if loan.scheme_type == self.scheme_type:
                #actually we have to check if loan is approved or not for that particular costumer
                #using credit score but here we are just randomizing
                loan_approval_ = random.randint(0,1)
                break
        self.loan_approval_status = loan_approval_
        if loan_approval_:
            print("Loan Approved")
            Borrower.borrowers_list.append(self)
        else:
            print("Loan not Approved")
    
    def bank_id(self):
        #randomlygenerated alphanumeric code unique to an applicant
        return 'B' + self.first_name+str(random.randint(10000, 99999))
    
    def __repr__(self):
        return "Borrower : '{}', {}, '{}' ".format(self.full_name(),self.id_number(), self.bank_id())
    
    def emi(self):
        return BorrowerSchemes.emi_calc_loan(self.scheme_type,self.scheme_duration,self.amount_deposited_or_loaned)

    def total_amount(self): #total amount of money to be paid (loan + interest)
        if(self.loan_approval_status):
            return BorrowerSchemes.emi_calc_loan(self.scheme_type,self.scheme_duration,self.amount_deposited_or_loaned)*self.scheme_duration*12
        else:
            print("Loan not Approved")
   
    @classmethod
    def search(cls,full_name_):  #used to search for borrower given full name
        for borrower in Borrower.borrowers_list:
            if borrower.full_name() == full_name_:
                return borrower
        return None

class Lender(PersonalInfo):
    lenders_list = [] #all Lender objects stored in this list
    
    def __init__(self,name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration, starting_date_of_scheme = datetime.now()):
        super().__init__(name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration, starting_date_of_scheme = datetime.now())
        Lender.lenders_list.append(self)
    
    def bank_id(self):
        #randomlygenerated alphanumeric code unique to an applicant
        return 'L' + self.first_name+str(random.randint(10000, 99999))
    
    def __repr__(self):
        return "Lender : '{}', {}, '{}' ".format(self.full_name(),self.id_number(), self.bank_id())
    
    def monthly_interest(self): #monthly interest to be given to the lender
        return LenderSchemes.interest_calc_fixed_deposit(self.scheme_type,self.scheme_duration,self.amount_deposited_or_loaned)
    
    @classmethod #used to search for lender given full name
    def search(cls,full_name_):
        for lender in Lender.lenders_list:
            if lender.full_name() == full_name_:
                return lender
        return None


def print_all_details(list): #prints scheme details given a list of schemes
    for object in list:
        print("'{}' - '{}'  interest rate : {} ".format(object.l_b_,object.scheme_type,object.interest_rate))

#initializing 6 basic schemes
ls1 = LenderSchemes(6,'Lender Scheme','Term Deposit')
ls2 = LenderSchemes(3.5,'Lender Scheme','Saving Deposit')
ls3 = LenderSchemes(7,'Lender Scheme','Recurring Deposit')
bs1 = BorrowerSchemes(12,'Borrower Scheme','Personal Loan')
bs2 = BorrowerSchemes(8,'Borrower Scheme','Housing Loan')
bs3 = BorrowerSchemes(10,'Borrower Scheme','Consumer Loan')

print("Schemes provided by Bank: ")
print_all_details(LenderSchemes.Lender_Schemes)
print_all_details(BorrowerSchemes.Borrower_Schemes)

bs1 = Borrower("Vijaya Anand",123123,13143134,"Consumer Loan",341241,3)

action = input("Search or Add costumer? ")

if action == 'Add':
    name = input("Enter full name : ")
    id_numb = int(input("Enter ID number : "))
    total_wealth = int(input("Enter wealth amount : "))
    l_or_b = input("Lender or Borrower? : ")
    if l_or_b == 'Lender':
        scheme_type = input("Enter scheme type : ")
        amount_deposited_or_loaned = int(input("Enter pricipal amount : "))
        scheme_duration = int(input("Enter term duration : "))
        Lender(name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration)
    else:
        scheme_type = input("Enter scheme type : ")
        amount_deposited_or_loaned = int(input("Enter loan amount : "))
        scheme_duration = int(input("Enter term duration : "))
        Borrower(name,id_numb,total_wealth,scheme_type,amount_deposited_or_loaned,scheme_duration)
else:
    full_name_ = input("Enter full name of person you want records of : ")
    l_or_b = input("Lender or Borrower : ")
    if l_or_b == 'Lender':
        obj = Lender.search(full_name_)
        if obj:
            obj.print_all_details()
        else:
            print("Costumer not found")
    else:
        obj = Borrower.search(full_name_)
        if obj:
            obj.print_all_details()
        else:
            print("Costumer not found")
