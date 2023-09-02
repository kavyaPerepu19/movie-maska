
import webbrowser
import json
try:
    with open ("movies.json",'r') as fp:
        s=json.load(fp)
except FileNotFoundError:
    print("File not found")
try:
    with open("links.json",'r') as ff:
        a=json.load(ff)
except FileNotFoundError:
    print("File not found")
fav=[]
history=[]
def view_fav(fav):
    print("Showing your favourites:")
    for ele in fav:
        print(ele)
def view_hisory(history):
    print("Showing your history: ")
    for ele in history:
        print(ele)
def addtofav(m_name):
    fav.append(m_name)
def pt():
    print("-----------------------------------------------------------------------------")
def web(link):
    webbrowser.open_new(link)
def inp():
    sno=int(input("Enter a number corresponding to the movie which you would like to view:"))
    return sno
def options():
    print("Enter 1 for trailer ")
    print("Enter 2 to watch the movie")
    print("Enter 3 to go back to main menu")
    vid=int(input())
    return vid
    
def display(name,lno):
    fp=open(name,"r")
    det=fp.readlines()
    print(det[lno])
    
def romcom():
    sno=inp()
    display("romcom.txt",sno-1)
    m_name=s["Rom-com"][sno-1]
    return m_name    
def horror():
    sno=inp()
    display("Horror.txt",sno-1) 
    m_name=s["Horror"][sno-1]
    return m_name
def poldrama():
    sno=inp()
    display("poldrama.txt",sno-1)
    m_name=s["Political Drama"][sno-1]
    return m_name
        
def susthriller():
    sno=inp()
    display("SuspenseThrillers.txt",sno-1)
    m_name=s["Suspense Thriller"][sno-1]
    return m_name
        
def documentry():
    sno=inp()
    display("documentry.txt",sno-1)
    m_name=s["Documentry"][sno-1]
    return m_name
def patriotic():
    sno=inp()
    display("patriotic.txt",sno-1)
    m_name=s["Patriotic Movies"][sno-1]
    return m_name
pt()
choice=1
flag="y"
while choice<=8 and flag=="y":
    genre={1:"Horror",2:"Rom-com",3:"Political Drama",4:"Suspense Thriller",5:"Documentry",6:"Patriotic Movies",7:"view your favourites",8:"view your history",9:"exit"}
    for ele in genre:
        print(ele,genre[ele])
    print()
    print("Please select a number referring to a genre or command:")
    choice=int(input())
    pt()
    if choice>=1 and choice<=6:
        i=0
        x=s[genre[choice]]
        for ele in x:
            print(i+1,ele)
            i+=1
        pt()
        if choice==1:
            m_name=horror()
        elif choice==2:
            m_name=romcom()
        elif choice==3:
            m_name=poldrama()
        elif choice==4:
            m_name=susthriller()
        elif choice==5:
            m_name=documentry()
        elif choice==6:
            m_name=patriotic()
        pt()
        history.append(m_name)
        vid=options()
        if vid==3:
            pt()
            continue
        link=a[m_name][vid-1]
        web(link)
        pt()
        favour=input("Do you want to add to favourites? ""y"" for yes: ")
        if favour=="y":
            addtofav(m_name)
    elif choice==7:
        view_fav(fav)
    elif choice==8:
        view_hisory(history)
    elif choice==9:
        pt()
        break
    flag=input("Do you wish to continue? ""y"" for yes: ")
    pt()
print("The connection has been closed. Thank you.")

 
