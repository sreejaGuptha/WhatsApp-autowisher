# packages used are pywhatkit  for sending auto message in whatsapp
import pywhatkit as w
number = input("Enter whatsapp number :")
message = input("Enter the message you want to send:")
hours = int(input("enter which hour to send:"))
mins = int(input("enter minutes: "))
try:
    w.sendwhatmsg(number, message, hours, mins)
    print("msg sent successfully")
except:
    print("error occured!")