from ResumeCooking.RandomChoiceDemo import uniMain, companyMain, nameMain, jobMain, emailMain, randomTemplate

from faker import Faker

from ResumeCooking.generateImpl import templatePath

fake = Faker()
# uniMain()

from string import Template, Formatter

uniTemplate = Template("I completed my Master's Degree from $University.\n")
uniResult = uniTemplate.substitute(University=uniMain())
print(uniResult)

companyTemplate = Template("I worked at $CompanyName.\n")
companyResult = companyTemplate.substitute(CompanyName=companyMain())
print(companyResult)

nameTemplate = Template("Meine Name ist ' $Name '. My friend's name is ' $Name '\n")
nameStore = nameMain()
print(nameStore)
# for _ in range(2):

nameResult = nameTemplate.substitute(Name=fake.name())
print(nameResult)
# name = nameMain()
# name1 = nameMain()
# x = str.format(f'My name is {name}. Again, my name is {name1}')
# print(x)
# nameStore.replace(nameStore,"")

# unprocessed to processed
# alpha1 = alpha()
# file = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/f1", "r")
# lines = file.readlines()
# # file.close()
# file = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/f1", "w")
# file2 = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/processed/f1", "a")
#
# for line in lines:
#     if line != alpha1 + "\n":
#         file.write(line)
#     if line == alpha1 + "\n":
#         file2.write(line)
# file.close()
# file2.close()

# nameTemplate = Template("Meine Name ist ' $Name '. My friend's name is ' $Name '\n")
# nameResult = nameTemplate.substitute(Name=alpha1)
# getKeys = Template.pattern.findall("Meine Name ist ' $Name '. My friend's name is ' $Name1 ")
# print(getKeys)

# print(nameResult)
# jt = jobMain()
# jt2 = jobMain()
# print(jt, ",", jt2)
# d1Template = Template("substitute: $j1 ### $j1")
# d1result = d1Template.substitute(j1=jobMain())
# print(d1result)
#
# print("JT:", jt)

import datetime

dt = datetime.datetime.now().date()
hour = datetime.datetime.now().hour
min = datetime.datetime.now().minute

# print(dt)
# print(hour,":",min)


# inp = int(input("Enter # of resumes you want to generate: "))
# dictEmail = emailMain()
#
# for _ in range(inp):
#     file = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/email", "r")
#     lines = file.readlines()
#     # file.close()
#     # file.close()
#     file = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/email", "w")
#     file2 = open("/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/processed/email", "a")
#     print(dictEmail)
#     for line in lines:
#         if line != dictEmail + "\n":
#             file.write(line)
#         if line == dictEmail + "\n":
#             file2.write(line)
#         # print(dictEmail)
#     file.close()
#     file2.close()

# for i in range(inp):
#     dictEmail = emailMain()
#     print(dictEmail)
#     # print(emailMain())
#     emailTemplate = Template("Email: $Email.\n")
#     emailResult = emailTemplate.substitute(Email=emailMain())
#     print("Dictemail: ",dictEmail)

# processedPath = "/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/processed/"
# unprocessedPath = "/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/"
# templatePath = "/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/ResumeTemplates/"
# generatepath = "/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/"


# dictJobTitle = jobMain()
# unprocessedJobLocation = open(unprocessedPath + "jobtitle.txt", "r")
# joblines = unprocessedJobLocation.readlines()
# unprocessedJobLocation = open(unprocessedPath + "jobtitle.txt", "w")
# processedJobLocation = open(processedPath + "jobtitle", "a")
#
# for line in joblines:
#     if line != dictJobTitle + "\n":
#         unprocessedJobLocation.write(line)
#     if line == dictJobTitle + "\n":
#         processedJobLocation.write(line)
#         print("j1:", line)
# unprocessedJobLocation.close()
# processedJobLocation.close()


# print(fake.date())
# print(fake.date(pattern="%Y-%m-%d", end_datetime=None))
# print(fake.date(pattern="%Y-%d-%m", end_datetime=None))
# print(fake.date(pattern="%m-%Y-%d", end_datetime=None))
# print(fake.date(pattern="%m-%d-%Y", end_datetime=None))
# print(fake.date(pattern="%d-%m-%Y", end_datetime=None))
# print(fake.date(pattern="%m-%Y", end_datetime=None))
# print(fake.date.between('1995-02-05',fake.date(pattern="%m-%Y")))
# print(fake.month_name(), fake.year(), "to", fake.month_name(), fake.year())
# print(fake.date_between(start_date="-15y", end_date="-10y"), "to",
#       fake.date_between(start_date="-10y", end_date="-6y"))
# print(fake.date_between(start_date="-10y", end_date="-5y"), "to",
#       fake.date_between(start_date="-5y", end_date="-3y"))
# print(fake.date_between(start_date="-5y", end_date="-4y"), "to",
#       fake.date_between(start_date="-3y", end_date="-3y"))
# print(fake.date_between(start_date="-5y", end_date="-3y"), "to",
#       fake.date_between(start_date="-3y", end_date="today"))
# import os
#
# dict_dir = os.path.abspath(os.getcwd())
# print(dict_dir)


# inp = int(input("Enter # : "))

# for _ in range(inp):
#     print(fake.ascii_free_email())

# namee = set(nameMain())
# print(namee)
# t = Template("My name is $Name, Again: $Name")
# print(t.safe_substitute(Name=namee))
# print(name)

# def effify(non_f_str: str):
#     return eval(f'f"""{non_f_str}"""')
#
#
# name = 'Fred'
# age = 42

# randTemplate = randomTemplate()
# f = open(templatePath + "/" + randTemplate, 'r')
#
# dictName = nameMain()
# files = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/ResumeTemplates/testsample3","r")

# naame = nameMain()
# s = "My name is {name} and I am {age} years old" \
#     "asdasd {naame}"
# print(effify(s))
# files.close()


# print(nameStore)
# if naame in s:
#     files = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/ResumeTemplates/testsample4", "a")
#     files.write("\n" + "".join(naame))
#     files.close()
# else:
#     files = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/ResumeTemplates/testsample4", "a")
#     files.write('')
#     files.close()
# import glob
#
# x = glob.glob(os.path.abspath(os.getcwd() + "/RandomResumeGenerate/*"))
# print(x)
# for z in x:
#     print(z)


# for _ in x:
#     with open(_) as myfile:
#         if 'Name' in myfile.read():
#             print('Blahblah')
#             files = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/ResumeTemplates/testsample3", "a")
#             files.write("".join("Name\n"))
#             files.close()
#         else:
#             files = open("/home/infotmt-user/PycharmProjects/ResumeCook/ResumeCooking/ResumeTemplates/testsample3", "a")
#             files.write("")
#             files.close()
#             print("Not Present")

# numberofresume = int(input("Enter ## of resumes you want to generate: "))
# new = []
# for _ in range(numberofresume):
#     filename = "{}_{}_{}".format(datetime.datetime.now().date(),
#                                  datetime.datetime.now().time(), nameMain())
#     new.append(filename)
# print(new)
#
# for _ in new:
#     print(_)
# os.makedirs("sample_s", exist_ok=True)
#
# import pathlib
#
# pathlib.Path('RandomResumeGenerate/{}'.format(datetime.datetime.now().date())).mkdir(exist_ok=True)


# sentence = "Blair Antoine\nLake Jackson, TX - Email me on Indeed: indeed.com\/r\/Blair-Antoine\/c3db396f7ba020f1\n\nWORK EXPERIENCE\n\nInformation Technology Specialist\n\nEDUCATION\n\nHigh school or equivalent\n\nMILITARY SERVICE\n\nService Country: US\n\nBranch: Navy\n\nRank: E5\n\nOctober 2001 to May 2009\n\nhttps:\/\/www.indeed.com\/r\/Blair-Antoine\/c3db396f7ba020f1?isid=rex-download&ikw=download-top&co=US"
#
#
# word = "c3db396f7ba020f1\n\nWORK EXPERIENCE"
# startIndex= sentence.index(word)
# print("Start Index: ",startIndex)
# wordEndIndex = sentence.index(word) + len(word) - 1
# print("End Index:",wordEndIndex)


# text = "fed up of seeing perfect fashion photographs"
# word = "fed"
