# Şüheda Yavuz
# 229911372

import datetime

date_time = datetime.datetime.now()

def login_exit():

    # 3 veri yapısını da burada tanımladım.
    admin = {"name": "İbrahim", "password": "1122"}
    users = [{"name": "Ahmed", "password": "1234"}, {"name": "Zeynep", "password": "4321"}, {"name": "Alberto", "password": "4422"}]
    activity = [{"name": "Ahmed", "balance": 1000, "deposits": [], "withdrawals": [],"transfers": []}, {"name": "Zeynep", "balance": 500, "deposits": [], "withdrawals": [],"transfers": []}, {"name": "Alberto", "balance": 200, "deposits": [], "withdrawals": [],"transfers": []}]

    running = 1
    while running:

        # Bankamızın logosu, güncel tarih ve zaman
        print(  """
------- WELCOME TO İSTİNYE BANK --------
-----------------------------------------
 /             İSTANBUL                   \ 
|       """   , date_time, """       |
 \                                        /
----------------------------------------
        """) 
        # log in ve exit seçenekleri sundum        
        print("""
        1-Log in
        2-Exit
                """)
        # kullanıcıdan bu hizmetlerden birini seçmesini istedim.
        choice = input("Enter your choice: ")
        if choice == "1":
                print("""
                
1-Admin
2-User
3-Go back
                
                """)
                # Eğer 1'i seçerse Admin olarak giriş yapacak
                choice = input("What do you want to login as: ")
                if choice == "1":
                    username = input("Admin Name: ")
                    password = input("Password: ")
                    #Eğer admin ismi ve şifresi eşleşirse giriş yapacak
                    if username == admin["name"] and password == admin["password"]:
                        print("Welcome", username ,"!")
                        logged_in = 1
                        while logged_in:
                            # adminin yapabileceği hizmet menüsü
                            print("""
-------Admin Menu--------
1- Add User
2- Romeve User
3- Display all Users
4- Exit Admin Menu
                            """)
                            choice = input("Please enter a number of the settings operations supported: ")
                            # 1'i seçerse kullanıcı ekleyecek
                            if choice == "1":
                                name = input("Enter the new user's name: ")
                                pwd = input("Enter the new user's password: ")
                                names = [user['name'] for user in users]
                                # Eğer var olan kullanıcıyı eklemeye çalışırsa zaten var deyip uyarı verecek
                                if name in names:
                                    print(name, "does not exist as an user to İSTİNYE BANK")
                                # Eğer var olan bie kullanıcı değilse ekleyecek
                                else:
                                    users.append({"name": name, "password": pwd})
                                    activity.append({"name": name, "balance": 0, "deposits": [], "withdrawals": [],"transfers": []})
                                    print(name, "was added as an user")
                            # Eğer 2'yi seçerse var olan kullanıcıyı hesaptan silecektir   
                            elif choice == "2":
                                name = input("Enter the name of the user to delete: ")
                                found_user = 0
                                for user in users:
                                    if user["name"] == name:
                                        users.remove(user)
                                        found_user = 1
                                        print(name, "was removed as an user to İSTİNYE BANK")
                                        break
                                # var olmayan bir kullanıcıyı silmeye çalışırsa hata mesajı verecek
                                if not found_user:
                                    print("User not found.")
                            # eğer 3'ü seçerse tüm kullanıcıları ve şifrelerini gösterecek
                            elif choice == "3":
                                print("All users:")
                                for user in users:
                                    print(user["name"], user["password"])
                            # Eğer 4'ü seçerse çıkış yapıp menüye geri dönecek
                            elif choice == "4":
                                logged_in = 0
                            # var olan seçeneklerden başka bir seçenek seçerse hata verecek
                            else:
                                print("Invalid choice. Please try again.")
                    # eğer admin ismi ve şifresi eşleşmezse admin ismi ve şifresini yeniden isteyecek
                    else:
                        print("Incorrect username or password. Please try again.")
                # kullanıcı 2'yi seçerse kullanıcı olarak giriş yapacak
                elif choice == "2":
                
                    username = input("User Name: ")
                    password = input("Password: ")
                    found_user = 0
                    # Eğer kullanıcı ismi ve şifre var olan kullanıcı ve şifreyle eşleşirse giriş yapılacak
                    for user in users:
                        if username == user["name"] and password == user["password"]:
                            found_user = 1
                            #kullanıcı ismiyle karşılandı
                            print(username, "Welcome to Sehir Bank")

                            logged_in = 1
                            while logged_in:
                                #kullanıcının sahip olacağı hizmet seçenekleri
                                print("""
Enter 1 to make a withdrawal
Enter 2 to make a deposit
Enter 3 to make a transfer
Enter 4 to view account activity
Enter 5 to log out
                                """)
                                choice = input("Please enter the number of the service: ")
                                for account in activity:
                                    if account["name"] == username:
                                        # eğer 1'i seçerse para çekme işlemini isteyecek
                                        if choice == "1":
                                            amount = int(input("Please enter the amount you want to Withdraw: "))
                                            # girdiği miktar bakiyeden büyükse hata mesajı verip menüye dönecek
                                            if amount > account["balance"]:
                                                print("Insufficient balance.")
                                            #girdiği miktar bakiyeden küçük veya eşitse para çekme işlemi gerçekleştirilecek
                                            else:
                                                account["balance"] -= amount
                                                account["withdrawals"].append({"amount": amount, "timestamp": datetime.datetime.now()})
                                                print("Withdrawal successful.", amount, "TL Withdrawn from your account. New balance:", account["balance"], "Time: ", date_time )
                                                print("Go back to menu..")
                                                break
                                        # 2. seçenek seçilirse para yükleme işlemi seçilecek
                                        elif choice == "2":
                                            amount = int(input("Please enter the amount you want to deposit: "))
                                            account["balance"] += amount
                                            account["deposits"].append({"amount": amount, "timestamp": datetime.datetime.now()})
                                            print("Deposit succesful.",amount, " TL added to your account. New balance: ", account["balance"])
                                            print("Go back to menu..")
                                            break
                                        # 3. seçenek seçilirse transfer işlemi başlatılacak
                                        elif choice == "3":
                                            runni = 2
                                            while runni:
                                                
                                                print("Warning:If you want to abort the transfer please enter abort")
                                                name = input("Please enter the name of the user user you want transfer money to: ")

                                                # eğer transfer yapacağı kendisine transfer yapacaksa hata verip yeniden isim girmesini isteyecek
                                                if name == username:
                                                    print("Transferring to user with the name ", name, "is not possible! \nUser does not exist!")
                                                # eğer kullanıcı transferi iptal etmek isterse "abort" yazarsa
                                                elif name == "abort":
                                                    print("Going back to main menu..")
                                                #kullanıcıdan transfer miktarı istenecek
                                                else:
                                                    
                                                    amount = int(input("Please enter the amountyou want to transfer: "))
                                                    for kullanici in activity:
                                                        if kullanici["name"] == name:
                                                            #girilen miktar bakiyeden küçük veya eşitse işlem başarılı olacak
                                                            if amount <= account["balance"]:
                                                                kullanici["balance"] += amount
                                                                account["balance"] -= amount
                                                                kullanici["deposits"].append({"amount": amount, "timestamp": datetime.datetime.now()})
                                                                account["transfers"].append({"amount": amount, "timestamp": datetime.datetime.now()})
                                                                print("Money transfer successfuly! . New balance:", account["balance"])
                                                                print("Going back to main menu..")
                                                                runni = 0
                                                                break
                                                            # girilecek miktar bakiyeden büyükse hata mesajı verecek ve iki seçenek sunulacak
                                                            else:
                                                                print("Sorry! you don't have the entered amount")
                                                                print("""
1- Going back to main menu
2-transfer again
                                                                """)
                                                                chose = input("Please enter your choice: ")
                                                                # 1'i seçerse menüye dönecek
                                                                if chose == "1":
                                                                    print("Going back to main menu..")
                                                                    runni = 0
                                                                    break
                                                                # 2'yi seçerse yeniden transfer işlemi başlatılacak
                                                                else:
                                                                    print("Transfer againn...") 
                                                                    runni = 2
                                                                    break
                                                    #var olmayan kullanıcıya transfer yapmak isterse hata mesajı verecek
                                                    else:
                                                        print("There is no such user.")
                                        # eğer 4'ü seçerse tüm finansal işlemleri ve kişisel bilgileri gösterecek
                                        elif choice == "4":
                                            print("""
----------İSTİNYE BANK----------
-----""",date_time,"""---
Your Name: """, username,"""
Your Password: """, password,"""
Your Balance Amount: """,account["balance"] ,"""
--------------------------------
User Activities Report:
Your Dopositst:""")
                                            # yapılan para yükleme işlemleri
                                            for transaction in account["deposits"]:
                                                print("Deposit of", transaction["amount"], "TL at", transaction["timestamp"])
                                            
                                            #yapılan para çekme işlemleri
                                            print ("Your Withdrawal: ")
                                            for transaction in account["withdrawals"]:
                                                print("Withdrawal of", transaction["amount"], "TL at", transaction["timestamp"]) 
                                            
                                            #yapılan transfer işlemleri
                                            print("Your Transfers: ")
                                            for transaction in account["transfers"]:
                                                print("Transferred to ",name,transaction["amount"], "TL at", transaction["timestamp"] )
                                                print("""
--------------------------------
Going back to main menu..
                                                """) 
                                        # 5. seçenek seçilirse çıkış yapılacak fakat bilgiler kaydedilecek 
                                        elif choice == "5":
                                            logged_in = 0
                                        # bu seçeneklerden başka bir seçenek seçilirse hata mesajı verilecek
                                        else:
                                            print("Invalid choice. Please try again.")
                                        break
                    # eğer kullanıcı adı veya şifre hatalı girilirse hata mesajı verilecek
                    if not found_user:
                        print("Incorrect username or password. Please try again.")
                #Eğer 3. seçenek seçilirse menüye dönülecek
                elif choice == "3":
                    print("Going back to main menu..")
                # eğer var olan seçenekler dışında başka bir seçenek seçilirse hata mesajı verilecek
                else:
                    print("Please enter a number that is a valid input")
        #eğer 2'yi seçerse uygulamadan çıkış yapılacak
        elif choice == "2":
            running = 0
        # var olan seçeneklerden başka bir seçenek seçilirse hata verecek
        else:
            print("Invalid choice. Please try again.")

# programı çalıştıracak
login_exit()