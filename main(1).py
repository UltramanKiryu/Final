
# Online Python - IDE, Editor, Compiler, Interpreter
cart=[]
Items = ["Pepsi","Ramen", "Steak", "Fries","Avengers","Twlight","Halloween","Godzilla","Ruby","Emerald","Quartz","Sapphire"]
Price = [2.00, 1.25, 100.00, 10.00, 12.20,20.00,20.00,10.00,12.20,514.00,120.00,538.00]
quanity = [50, 12, 15, 22, 6, 10, 15, 2, 12,15,0,22]
qrCode=["FO-5544","FO-1212","FO-2211","FO-1414","MV-4546","MV-7574","MV-8585","MV-3332","JW-0001","JW-5001","JW-0002","JW-8080"]
def display(a):
    i=0
    for i in range(len(Items)):
        ## to ensure that the  
        if a in qrCode[i]:
            print(f'Item: {Items[i]}')
            print(f'Amount in Stock: {quanity[i]}')
            print(f'Price: {Price[i]}')
    tt=str(input('Please enter in the name of the item you want or type exit to return to the main screen: '))
    while tt !="exit":
        if tt in Items:
            w =0;
            qq= int(input('Please enter in the amount of the item you want: '))
            for w in range(len(Items)):
                if tt == Items[w]:
                    if qq <= quanity[w]: 
                        st = str(qq)+ qrCode[w]
                        cart.append(st)
                    else:
                        print("Please enter an amount that is less than the amount in Stock")
        else:
            print("Please enter an item from the list")
        tt=str(input('Please enter in the name of the item you want or type exit to exit: '))
    return None

def checkout():
    total=0
    for i in range(len(cart)):
        st = cart[i]
        x = st.find("FO")# see if the item has the FO or Food tag
        if x==-1:
            x = st.find("MV")# see if the item has the MV or movies tag
            if x==-1:
                x = st.find("JW")# see if the item has the JW/ Jewels tag
        w=0
        for w in range(len(qrCode)):
            if (st[x:]) in qrCode[w]:
                print(Items[w])
                if x<1:
                    t =int (st[0]) * Price[w]
                    total=t+total
                    print(f'Price: {t}')
                elif x<2:
                    t=int (st[:1]) * Price[w]
                    total=t+total
                    print(f'Price: {t}')
                elif x<3:
                    t=int (st[:2]) * Price[w]
                    total=t+total
                    print(f'Price: {t}')
    print(f'Total: {total}')
    em =str(input('Please enter in your email address: '))
    sh =str(input('Please enter in a shipping address for the items: '))
    print(f'The items will be ship to this address: {sh}')
    print(f'Confromation email has been sent to this email address: {em}')


print("Welcome to the website program")
a = str(input('Please enter in your name: '))

print(f'Welcome {a}, to the Website program')
print("Please select form the following catagories or type checkout to proceed to checkout")
print("Jewels, Movies, Food")
w =str(input('Enter which the name of the catagories you want to look through: '))
while w != "exit":
    if w=="Jewels":
        ##display the Jewels
        display("JW")
    elif w=="Movies":
        ## go to Movies
        display("MV")
    elif w =="Food":
        ## go to Food
        display("FO")
    else:
       print("Please enter one of the catagories")
    w =str(input('Enter which the name of the catagories you want to look through: '))
    
checkout()

