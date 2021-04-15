def read_from_database():
  

    try :
        products = []
        f = open("e:/kelass mohandes aemi/6/zahra_store/database.csv","r")
        big_text = f.read()
        products_list = big_text.split('\n')

        for i in range(len(products_list)):
            info = products_list[i].split(',')
            products.append( {'id':info[0],'name':info[1],'price':info[2],'count':info[3]})

    except Exception as e:
        print(e)
        products = []

    return products

def add():
   id = input('enter id:')
   name = input('enter name:')
   price = input('enter price:')
   count = input('enter count:')
   products.append( {'id': id,'name':name ,'price':price,'count': count})
   print('ezafe shodan kala be database ba movaffaghiyat')
 
def serch():
    user_input = input ('enter a text to search... ')
    for product in products:
        if product['id'] ==user_input  or product['name'] == user_input:
            print(product)
            break
    else:
        print('not found')
def edit():

    show_all()
    use_input = input('vared kon yek id ya name baraye edit= ')
    for product in products:
        if product['id'] == use_input or product['name'] == use_input:
            print(product)
            break
    else:
        print('kala peyda nashod')


    products.remove(product)
    id = input('vared kon edited id:')
    name = input('vared kon edited name:')
    price = input('vared kon edited price:')
    count = input('vared kon edited count:')
    products.append({'id':id , 'name':name ,'price':price ,'count':count})
    print('edited kala ton ba movaffaghiyat anjam shod')


def remove():
   show_all()
   use_input = input('vared kon yek id ya name baraye edite=')
   for product in products:
       if product['id'] == use_input or product['name'] == use_input:
           print(product)
           break
       else:
        print('kala peyda nashod')

   products.remove(product)
   print('kala ton ba movaffaaghiyat hazf shod')

def buy():
    factor = []
    price = int() 
    while True:
        user_list = input('ayay shoma ghasd kharid darid?(y or n):')
        if user_list == 'y':
            print('az list zir kalaiy ke mikhay bekhari ro entekhab kon')
            for product in products:
                print(product)
            use_input = input('kalaei ke mikhahid ra vared konid=')
            for product in products:
                if product['id'] ==use_input or product['name']==use_input:
                    print(product)
                    break

            else:       
                print('in kala mojod nist') 
                exit()       

        elif  user_list == 'n':
            print(factor)
            print('hazineh kamel shoma:',price)  
            break

def show_all():
    for product in products:
        print(product)

def my_exit():
   khorog = input('aya shoma mayel hasti taghyirat ro zakhireh koni dar database? (y or n): ')
   if khorog  == 'y':
        f = open("database.csv", "w")
        for product in products:
            f.write(str(product['id']+','+product['name']+','+product['price']+','+product['count']))
        exit()



def show_menu():
    print('well come to zahra store') 
    print('1-add new product')
    print('2-serch')
    print('3-edit')
    print('4-remove')
    print('5-buy')
    print('6-show all')
    print('7-exit')

#products=read_from_database()
#print(products)

products = read_from_database()

while True:
    show_menu()
    choice = input('enter your choice:')

    if choice == '1':
        add()
    elif choice == '2':
        serch()
    elif  choice =='3':
        edit()
    elif  choice =='4':
        remove()
    elif  choice =='5':
        buy()
    elif  choice =='6':
        show_all()
    elif  choice =='7':
        my_exit()