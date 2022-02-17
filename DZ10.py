    #actions = ['add', 'change', 'del', 'phone', 'show all', 'name']
    #def add(self, Record):
        #Dict[Record.name.value]=Record.phone.value

from collections import UserDict

class Field():
    pass

class AddressBook(UserDict):
    address_book = {
        'ff': '88',
        'hhh': '9979999'
    }
    actions = ['add', 'change', 'del', 'phone', 'show all', 'name']
    #def add(self, Record):
        #Dict[Record.Name]=Record.phone    
    
class Name(Field):
    value='User'
    
class Phone(Field):
    phone=tuple()        

class Record(Name, Phone):    
    def name (self):       
        value = Name.value
    def phone (self):        
        phone = Phone.phone
    

contact_book = AddressBook()

# old code start
def input_error (get_handler):
    def inner(command1):
        try:
            get_handler(command1)
            return  get_handler(command1) 
        except ValueError as e:
            print(e)
            command1 ='help'
        except IndexError as e:
            print(e)  
            command1 ='help' 
        except TypeError as e:
            print(e) 
            command1 ='help'
        except KeyError as e:
            print("hhhhhh")
            command1 ='help'             
        return command1 , print(command1)         
    return inner 

def input_():
    while True:
        user_command1= input('Please, give me a command:')
        
        if "hello" in user_command1 or "exit" in user_command1 or "close" in user_command1 or "good bye"  in user_command1 or "show all" in user_command1 or "phone" in user_command1  or "add" in user_command1 or "change" in user_command1:
            return user_command1
        continue

def normalization (user_command1):
    user_command1.casefold()   
    user_command1_norm=user_command1
    return user_command1_norm 
    
    
def input_error_2 (parser):
    def inner(user_command1_norm):
        a=0  
        while a<10:
            try:         
                name, phone, command1 = parser(user_command1_norm)
                a+=1
                return name, phone, command1
            except TypeError:         
                print("Give me name and phone please")                             

            except  IndexError:
                print("Give me true name or phone please")
                
                while True:
                    
                    user_command1= input_()
                    user_command1_norm=normalization (user_command1)                 
                    try:           
                        name, phone, command1 = parser(user_command1_norm)
                        a+=1
                        return name, phone, command1
                    except:
                        print(f'"{phone}" is not a number. Try again')                                    
               
            except  ValueError:
                print("Give me true name or phone please")
                                

            except  KeyError:
                print("Give me true name or phone please")
                
    return inner 

def help_func():
    user_command1= input('Please, give me a new command1:')
    user_command1_norm=normalization (user_command1)        
    name, phone, command1 = parser(user_command1_norm)    
    return name, phone, command1     

@input_error_2
def parser(user_command1_norm):
    if user_command1_norm in ["hello", "exit", "close", "good bye", "show all"]:
        command1=user_command1_norm
        return "", "", command1
    
    elif 'phone' in user_command1_norm:
        b=user_command1_norm.split('phone ')
        name=b[-1]
        command1='phone'    
        return name,"", command1
    
    elif 'add' in user_command1_norm or 'change' in user_command1_norm:
        c=user_command1_norm.split(' ')
        name=c[1]
        phone=c[2]
        command1=c[0]
        return name, phone, command1
    
    else:         
        name=''
        phone=""
        command1="help"
        return name, phone, command1

def main ():

    def close_func(): 
        print('Good bye!')    

    def show_func():
        print(contact_book)
    
    def phone_func():
        print(f'{name} phone is')
        
        print(contact_book.get(name))

    def change_func():        
        
        contact_book[Record.name.value] =Record.name.phone
        
      
        
         

    def hello_func():    
        print('How can I help you?')

    command1S = {
    'good bye': close_func,
    'close': close_func,
    'exit': close_func,
    'show all': show_func,
    'phone': phone_func,
    'change': change_func,
    'add': change_func,
    'hello': hello_func,
    'help': help_func,
}

@input_error   
def get_handler(command1):
    return command1S[command1]


    
while True:    
    user_command1= input_()

    if user_command1 in ['close', 'good bye', 'exit']:       
        close_func()
        break
    user_command1_norm=normalization (user_command1)
        
    name, phone, command1 = parser(user_command1_norm)

     
        
    if command1 is not None:
        Record=Record()
        Record.name.value = name
        Record.phone.phone= phone
        a= get_handler(command1)           
        a()
        
      
          
if __name__ =="__main__":
    main ()







