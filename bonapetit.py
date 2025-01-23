bill = [3,10,2,9] #bills of all items eaten by both of them
k=1 #Anna didn't eat 1 index item
b=12 #Bill Contribuition by Anna

 #Amount which brian give back to Anna

def rem_bal(bill, k, b):
    remaining_balance=0
    actual_anna_bill=0
    for bil in range(len(bill)):
        if bil == k:
            continue
        actual_anna_bill += bill[bil]
    
    actual_anna_bill = actual_anna_bill//2
    remaining_balance = b - actual_anna_bill

    return remaining_balance

rem_bal(bill, k, b)


    