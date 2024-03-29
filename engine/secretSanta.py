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


def sort_santas_list(santas_list=None):
    """

    @return:
    """
    checking_it_twice = list(santas_list)
    random.shuffle(santas_list)
    random.shuffle(checking_it_twice)
    nice_list = list(zip(santas_list, checking_it_twice))

    while not test_santas_list(nice_list):
        random.shuffle(santas_list)
        random.shuffle(checking_it_twice)
        nice_list = list(zip(santas_list, checking_it_twice))

    return nice_list


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
        print (1)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        print(2)
        server.starttls()
        print(server)
        server.login(santas_helper, password)
        print(3)
        server.sendmail(santas_helper, santa.email, message)
        server.close()
        print(f'successfully sent the mail email to {santa.name}')

    except:
        print("failed to send mail")


if __name__ == "__main__":
    santas_list = [People('Alex', 'Jacobs', '1', 'alexdjacobs@gmail.com', '12/25/2021', 'Brook'),
                   People('Alex', 'Gilbert', '2', 'angilbert.film@gmail.com', '12/25/2021', "Eve"),
                   People('Craig', 'Tynes', '3', 'CraigTynes@gmail.com', '12/25/2021', 'Alex Gilber'),
                   People('Dom', 'Martin', '4', 'dom.wm.martin@gmail.com', '12/25/2021', 'Craig'),
                   People('Eve', 'Cole', '5', 'coeeverett@gmail.com ', '12/25/2021', 'Alex Jacobs'),
                   People('Brook', 'Johnston', '6', 'react746@gmail.com ', '12/25/2021', 'Dom Martin')]

l = sort_santas_list(santas_list)
print(l)
if l:
    print (l)
    for santa, person in l:
        print(f'{santa.name} is giving a gift to {person.name}')
        if santa.name == 'Alex Jacobs':
            print ('testing')
            send_santas_list(santa, person)

