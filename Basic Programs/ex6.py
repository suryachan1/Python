#to check the on road price of a bike under the conditions
#if the price is greater then 72000 then income tax is 10% of usual price and insurance will bw 15% of the actual price
#if the price is greater than 150000 and less than 200000 rupees the tax should be 25% and insurance 20%
#if the price is above 200000 rs then tax will be 35% and insurance will be 28%
#otherwise min price with as starts from 72000
#actual price+tax+insurance=onroadprice
price=int(input('enter the bike price'))
if price>72000 and price<150000:
    tax=(10/100)*price
    insu=(15/100)*price
    print('onroadprice',price+tax+insu)
elif price>150000 and price<200000:
    tax=(25/100)*price
    insu=(20/100)*price
    print('onroadprice',price+tax+insu)
elif price>200000:
    tax=(35/100)*price
    insu=(28/100)*price
    print('onroadprice',price+tax+insu)
else:
    print('min price as start as 72000')
    
total=price+tax+insu
print('total price is',total)
