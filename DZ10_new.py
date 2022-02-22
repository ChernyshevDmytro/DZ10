from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[obj.name.value] = obj         
    
class Field():
    pass   
    
class Name(Field):
    value='User'
    
class Phone(Field):
    phone=[]        

class Record(Name, Phone):    
    #self.phone = phone 
    def __init__(self, name) -> None:
        self.name = name
        
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
        command1=c[0]
        if len(c) <=2: 
            phone="no" 
        else: phone=c[2]
        
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
        #print(c_b.data.values)
        for k,v in  c_b.data.items():
            for i in v.phone:
                a=len(i)
                b=1
                if i !="" or i =="no":
                    b+=1
                    print(f"{k} {i}")
                elif a==b:
                    print({k})  
        
    
    def phone_func():
        if name in c_b.data.keys():
            print(f'{name} phone is')
            for i in c_b.data.get(name).phone:
                if i !='':
                    print(i)
        else: print(f'{name} is not in contact book')    

    def change_func():        
        c_b.add_record(record) 

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


    c_b = AddressBook()

    while True:   
    
        user_command1= input_()

        if user_command1 in ['close', 'good bye', 'exit']:       
            close_func()
            break
    
        user_command1_norm=normalization (user_command1)
        
        name, phone, command1 = parser(user_command1_norm)

        record=Record(Name())
        record.name.value = name
        record.phone.append(phone)
        
        if command1 is not None:     
               
            a= get_handler(command1)           
            a()
  
            
if __name__ =="__main__":
    
    main () 



    
       

    






