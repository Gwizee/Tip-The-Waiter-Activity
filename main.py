def total_tip(bill_amount,tip_perc) :
    total = bill_amount * (tip_perc/100)
    total = total + bill_amount
    return total
total_amount = total_tip(1000,20)
print("Total bill:", total_amount)