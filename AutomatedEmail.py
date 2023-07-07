import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "20510837.dypit@dypvp.edu.in"
receiver_email = "adityamsahane07@gmail.com"
password = input("Type your password and press enter:")
message ="""Hello mail  sent through python automation"""
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)