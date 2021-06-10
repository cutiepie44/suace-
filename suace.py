import time
import webbrowser
print("""                                                              
 @@@@@@   @@@  @@@   @@@@@@    @@@@@@@  @@@@@@@@             
@@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@             
!@@       @@!  @@@  @@!  @@@  !@@       @@!          @@!     
!@!       !@!  @!@  !@!  @!@  !@!       !@!          !@!     
!!@@!!    @!@  !@!  @!@!@!@!  !@!       @!!!:!    @!@!@!@!@  
 !!@!!!   !@!  !!!  !!!@!!!!  !!!       !!!!!:    !!!@!@!!!  
     !:!  !!:  !!!  !!:  !!!  :!!       !!:          !!:     
    !:!   :!:  !:!  :!:  !:!  :!:       :!:          :!:     
:::: ::   ::::: ::  ::   :::   ::: :::   :: ::::             
:: : :     : :  :    :   : :   :: :: :  : :: ::              
                                                             """)
print("1 NHENTIA")
print("2 R34")
print("3 E621")
websitec = input("What website? ")
if websitec == "1":
    websitec = 1
    while True:
        code0 = input("whats the code ")
        website0 = "https://nhentai.net/g/"
        print(website0 + code0)
        webbrowser.open(f"{website0}{code0}")
        print('\033c')
        print('\x1bc')
        time.sleep (5)
if websitec == "2":
                websitec = 2
                while True:
                    code1 = input("whats the code ")
                    website1 = "https://rule34.xxx/index.php?page=post&s=view&id="
                    print(website1 + code1)
                    webbrowser.open(f"{website1}{code1}")
                    print('\033c')
                    print('\x1bc')
                    time.sleep (5)
if websitec == "3":
    websitec = 3
    while True:
        code2 = input("whats the code ")
        website2 = "https://e621.net/posts/"
        print(website2 + code2)
        webbrowser.open(f"{website2}{code2}")
        print('\033c')
        print('\x1bc')
time.sleep (5)
