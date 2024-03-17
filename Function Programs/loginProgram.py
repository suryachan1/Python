#login fn which accepts the user only when the user name and password are same and displays a mess login successfull
#otherwise it keeps asking the user to enter the crentitials untill the correct
'''def login():
    a=(username=='sai')
    b=(password==1234)
    if(username==password):
        print('login successfull')
    else:
        login()
username=input('enter username')
password=input('enter password')
login()'''


def login():
    while True: #infinite
        username=input('enter username')
        password=input('enter password')
        if username==password:
            print('login successfull')
            break
        else:
            print('invalid crendiantles')
login()
            
    
