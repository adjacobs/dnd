import random
import smtplib
from email.mime.text import MIMEText


class People:
    def __init__(self, first, last, number, email, date, last_elf):
        self.name = f'{first} {last}'
        self.number = number
        self.email = email
        self.date = date
        self.last_elf = last_elf

    def __str__(self):
        return f'{self.name}, Email is {self.email}'

    def __repr__(self):
        return f'{self.name}'


def sort_santas_list(lop=None):
    """

    @return:
    """
    lop = [People('Alex', 'Jacobs', '1', 'alexdjacobs@gmail.com', '12/25/2021', 'Brook'),
           People('Alex', 'Gilbert', '2', 'angilbert.film@gmail.com', '12/25/2021', "Eve"),
           People('Craig', 'Tynes', '3', 'CraigTynes@gmail.com', '12/25/2021', 'Alex Gilber'),
           People('Dom', 'Martin', '4', 'dom.wm.martin@gmail.com', '12/25/2021', 'Craig'),
           People('Eve', 'Cole', '5', 'coeeverett@gmail.com ', '12/25/2021', 'Alex Jacobs'),
           People('Brook', 'Johnston', '6', 'react746@gmail.com ', '12/25/2021', 'Dom Martin')]

    lop2 = list(lop)
    random.shuffle(lop)
    random.shuffle(lop2)
    santas_list = zip(lop, lop2)

    while not test_santas_list(santas_list):
        random.shuffle(lop)
        random.shuffle(lop2)
        santas_list = list(zip(lop, lop2))

    return santas_list


def test_santas_list(santas_list):
    for p1, p2 in santas_list:
        if p1 == p2:
            return False
        if p1.last_elf == p2.name:
            return False
    return True


def send_santas_list(santa, person, budget=None):
    """
    Sends email to santa on behalf of the person. Giving santa their name and information
    @param santa: Person Class
    @param person: Person Class
    @param budget: Int
    @return:
    """
    if budget:
        msg = f'Your secret Santa for {person.name} with a budget of {budget}'
    else:
        msg = f'Your secret Santa for {person.name}'

    subject = 'Your Foggy Secret Santa'

    santas_helper = 'punnyfoggersanta@gmail.com'
    password = 'doubledragon1986'
    message = f"""From: {santas_helper}\nTo: {santa.name}\nSubject: {subject}\n\n{msg}"""

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(santas_helper, password)
        server.sendmail(santas_helper, santa.email, message)
        server.close()
        print(f'successfully sent the mail email to {santa.name}')

    except:
        print("failed to send mail")


if __name__ == "__main__":
    l = sort_santas_list()
    if l:
        for k, v in l:
            print(f'Santa is {k.name}')
            #send_santas_list(k, v)
