class Email:
    def __init__(self):
        self.sender_list = []
        self.receiver_list = []
        self.content_list = []


email = Email()
command = input()

while not command == "Stop":
    command = command.split()
    email.sender_list.append(command[0])
    email.receiver_list.append(command[1])
    email.content_list.append(command[2])
    command = input()

is_sent = input().split(", ")

for i in range(len(email.sender_list)):
    is_sent_statement = False
    for sent in is_sent:
        if i == int(sent):
            is_sent_statement = True
    print(f"{email.sender_list[i]} says to {email.receiver_list[i]}: {email.content_list[i]}. Sent: {is_sent_statement}")