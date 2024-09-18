import random

domains = [
	"@gmail.com",
	"@yahoo.com",
	"@hotmail.com",
	"@outlook.com",
	"@icloud.com",
	"@aol.com",
	"@protonmail.com",
	"@zoho.com",
	"@gmx.com",
	"@mail.com",
	"@yandex.com",
	"@live.com",
	"@me.com",
	"@msn.com",
	"@comcast.net",
	"@verizon.net",
	"@att.net",
	"@tutanota.com",
	"@fastmail.com"
]

def create_emails():
	with open("names.txt") as file:
		names = ["".join(line.strip().split('.')) for line in file.readlines()]

	with open("emails.txt", "a") as file:
		for name in names:
			email = f"{name}{random.choice(domains)}\n"
			file.write(email)

