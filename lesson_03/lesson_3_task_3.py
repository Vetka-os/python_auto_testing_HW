from address import Address
from mailing import Mailing

mail = Mailing(
    Address("0987", "Внуково", "ул. Внучкова", "д. 9", "кв. 14"),
    Address("8754", "Дедушково", "ул. Дедкина", "д. 15", "кв. 4"),
    3,
    "DFr_4564-ytr",
)

print(mail)
