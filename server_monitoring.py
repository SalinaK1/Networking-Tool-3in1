# def color_print(msg, color=None):
#     """
#     Print colored console output.

#     Color choices are:
#         'gray'
#         'green'
#         'red'
#         'yellow'
#         'purple'
#         'magenta'
#         'cyan'

#     Example::
#         color_print("Here is a message...", 'red')
#     """
#     if not msg:
#         print("You must pass a message to the color_print function!")
#         return

#     # Declare closing.
#     end = "\033[0m"

#     # Declare print colors.
#     colors = {
#         "gray": "\033[90m",
#         "green": "\033[92m",
#         "red": "\033[91m",
#         "yellow": "\033[93m",
#         "purple": "\033[94m",
#         "magenta": "\033[95m",
#         "cyan": "\033[96m",
#     }

#     if color in list(colors.keys()):
#         print((colors[color] + str(msg) + end))
#     else:
#         print(msg)


def send_mail(gmail_user, gmail_password, to, subject="(No Subject)", text="", html=None, attach=None):       #send email if the server is down via gmail.

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email import encoders

    if html:
        message = MIMEMultipart("alternative")
    else:
        message = MIMEMultipart()

    if not gmail_user:
        print("User needs to be specified.\n")
        return
    if not gmail_password:
        print("Password is missing.\n")
        return

    message["From"] = gmail_user
    message["To"] = to
    message["Subject"] = subject

    if html:        # If there is an HTML message (e.g. text/html), attach that to the email.
        message.attach(MIMEText(html, "html"))

    message.attach(MIMEText(text, "plain"))     # Attach the text/plain message to the email.

    if attach:      # Attach the file, if given.
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(attach, "rb").read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            'attachment; filename="%s"' % os.path.basename(attach),
        )
        message.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_password)
    mailServer.sendmail(gmail_user, to, message.as_string())
    mailServer.close()
    print("Message sent!")
    print("    To: %s\n    Subject: %s" % (message["To"], message["Subject"]))


def monitor_uptime(url, recipients=None, gmail_user=None, gmail_password=None):     # Monitor a url to see if it is online.
    from datetime import datetime, timedelta
    import http.client
    from urllib.parse import urlparse

    print("\nChecking if %s is online" % url)
    site = urlparse(url)        # parse urls to components.
    conn = http.client.HTTPConnection(site[1])      
    conn.request("HEAD", site[2])       
    status = conn.getresponse()
    status_code = status.status

    full_url = site.geturl()
    clean_url = site.netloc + site.path     # Get the clean URL (without protocol)

    if status_code != 200 and status_code != 302:
        print("\nSite is down with a %s error code\n" % status_code)

        if recipients and gmail_user and gmail_password:
            subject = "Server is down!"
            message_text = "%(site)s is down with status code %(code)s!" % {"site": full_url, "code": status_code,}

            # Send the message to all the recipients.
            recipients = recipients if not isinstance(recipients, str) else [recipients]
            for to_address in recipients:
                send_mail(gmail_user, gmail_password, to_address, subject, message_text)
            print("\nNotification sent!\n")
        return False

    print("\nSite is online (status 200)!\n")
    return True