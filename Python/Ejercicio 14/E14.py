import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "Pruebaspc101@gmail.com"
Reciever_Email = "ggamezserna@gmail.com"
Password = input('Ingresa tu contraseña: ')

newMessage = EmailMessage()                         
newMessage['Subject'] = "Imagen chistocita" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Somos Gerardo Gámez Serna y Francisco Javier Valero Lara')

files = ['chistocito.jpg']

for file in files:
    with open(file, 'rb') as meme:
        image_data = meme.read()
        image_type = imghdr.what(meme.name)
        image_name = meme.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage) 
