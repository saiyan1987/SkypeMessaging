import skpy
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username",dest="username")
    parser.add_argument("--password", dest="password")
    parser.add_argument("--message",dest="message")
    args=parser.parse_args()
    skype=skpy.Skype()
    skype.conn.liveLogin(args.username,args.password)
    white_list=["uk-faheem"]
    for contact in skype.contacts:
        if(contact.id in white_list):
            print(f"sending message to {contact.id}")
            contact.chat.sendMsg(args.message)

main()
