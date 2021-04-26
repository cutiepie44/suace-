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
x = 1
while True:
    code = input("whats the code ")
    website = "https://nhentai.net/g/"
    print(website + code)
    webbrowser.open(f"{website}{code}")
    print('\033c')
    print('\x1bc')
    time.sleep (5)
time.sleep (5)
