import random
import smtplib
import sys

chores = ["dishes", "bathroom", "vacuum", "walk dog"]
email = [
    "alice@example.com",
    "bob@example.com",
    "carol@example.com",
    "david@example.com",
]

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login("bokyeong3659@gmail.com", sys.argv[1])

for num in range(len(chores)):
    random_chore = random.choice(chores)
    print(random_chore)
    chores.remove(random_chore)

    body = f"""subject: Distribute chores({num+1}) \n
    You have to do chores like {random_chore}! We distribute chores at random.
    Thank you :)."""
    print(f"Sending email to {email[num]}...")
    send_email = smtp_obj.sendmail("bokyeong3659@naver.com", email[num], body)

smtp_obj.quit()
