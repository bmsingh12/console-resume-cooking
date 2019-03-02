from faker import Faker

fake = Faker()

numberofnames = int(input("Enter # of names you want to generate: "))

for _ in range(numberofnames):
    f = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/dictionary/fakerdictionary/fullname","a")
    result = "".join(fake.name())
    f.write(result+"\n")

    f.close()


# checking for repeated names

# with open('/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/fakerdictionary/fullname') as file:
#     seen = set()
#     for line in file:
#         line_lower = line.lower()
#         if line_lower in seen:
#             print(line)
#         else:
#             seen.add(line_lower)