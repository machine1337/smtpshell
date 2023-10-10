# smtpshell
A simple Reverse Shell that can communicate through Gmail SMTP or any other SMTP to evade network restrictions

![gmail](https://user-images.githubusercontent.com/82051128/235435093-0b482435-88b3-405c-98f9-fa218b2ed95f.PNG)

# Note:
     This reverse shell communicates Via Gmail SMTP (or u can use any other smtps as well)
     but Gmail SMTP is valid because most of the companies block unknown traffic
     so gmail traffic is valid and allowed everywhere.
  
# Warning:
     1. Don't Upload Any Payloads To VirusTotal.com Bcz This tool will not work
        with Time.
     2. Virustotal Share Signatures With AV Comapnies.
     3. Again Don't be an Idiot!

# How To Setup
     1. Create Two seperate Gmail Accounts.
     2. Now enable SMTP On Both Accounts (check youtube if u don't know)
     3. Suppose you have already created Two Seperate Gmail Accounts With SMTP enabled
        A -> first account represents  Your_1st_gmail@gmail.com
        B -> 2nd account   represents  your_2nd_gmail@gmail.com
     4. Now go to server.py and then go to line (66 to 75):-
        smtp_username="Your_1st_gmail@gmail.com"
        smtp_password="Your_1st_gmail_app_password"
        imap_username="your_1st_gmail@gmail.com"
        imap_password="Your_1st_gmail_app_password"
        imap_username_from_client="your_2nd_gmail@gmail.com"
     5. Now go to client.py and then go to line (7 to 12):-
          imap_username_from_client="your_2nd_gmail@gmail.com"
          imap_password= "your_2nd_gmail@app_password"
          smtp_username="Your_1st_gmail@gmail.com"
          smtp_password="Your_1st_gmail_app_password"
    6. Enjoy
  
# How To Run:-
    1. Run the client.py
    2. Run the server.py and then enter command
    
# Features:-

    1) FUD Ratio 0/40
    2) Bypass Any EDR's Solutions
    3) Bypass Any Network Restrictions
    5) No More Tcp Shits

# Contact:-
    Telegram Group:- https://t.me/machine1337
