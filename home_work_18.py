ticket_quantity = int(input('Введите количество билетов'))
def get_ticket_price(price):
 age = int(input("How old are you?"))
 if 18 <= age <= 18:
    print('бесплатно')
 elif  18 <= age <= 25:
    print('990 рублей')
 elif 25<= age:
    print('1390 рублей')
if ticket_quantity > 3:
     price = price - ((price / 100)* 10)
     print('сумма к оплате - {price} рублей (со скидкой в 10% ')
else:
     print('сумма к оплате {price}')


