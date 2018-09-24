import os
import smtplib
import getpass
from email import encoders
from string import Template
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def initialize_server(from_address, password, email_smtp):
    server = smtplib.SMTP(email_smtp, 587)
    server.starttls()
    server.login(from_address, password)
    return server


def kill_server(server):
    server.quit()


def iterate_over_files(root_path, extension, server, from_address, email_subject, email_body, assignment_count):
    email_extension = extension
    to_address = ""
    student_list = []
    assignment_number = assignment_count

    for name in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, name)):
            student_list.append(name)

    for student in student_list:
        to_address = student + extension
        assignment_path = root_path + "/" + student + \
            "/" + "hw" + str(assignment_number) + "/"
        for assignment in os.listdir(assignment_path):
            if assignment != ".DS_Store":
                assignment_path = assignment_path + assignment
                send_mail(server, from_address, to_address,
                          assignment_path, email_subject, email_body, assignment)
                console_message = Template("Mail sent to ${to_address}").substitute(
                    to_address=to_address).strip(extension)
                print(console_message)


def send_mail(server, from_address, to_address, assignment_path, email_subject, email_body, assignment):
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = email_subject

    body = email_body
    msg.attach(MIMEText(body, "plain"))

    attachment = open(assignment_path, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",
                    "attachment; filename= %s" % assignment)
    msg.attach(part)

    text = msg.as_string()
    server.sendmail(from_address, to_address, text)


def main():
    root_path = input("Enter root folder path: ")
    extension = input("Enter email extension, e.g. @something.com: ")
    from_address = input("Enter your Email: ")
    password = getpass.getpass("Password:")
    email_smtp = input("Enter email smtp adddress: ")
    email_subject = input("Enter email subject: ")
    email_body = input("Enter email body: ")
    assignment_number = input("What number is the assignment? e.g. 1 or 2 or n: ")
    server = initialize_server(from_address, password, email_smtp)
    iterate_over_files(root_path, extension, server,
                       from_address, email_subject, email_body, assignment_number)
    kill_server(server)


if __name__ == "__main__":
    main()
