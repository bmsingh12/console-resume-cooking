from ResumeCooking.RandomChoiceDemo import uniMain, companyMain, nameMain, jobMain, emailMain, contactNoMain, \
    addressMain, randomTemplate, degreeMain, dateMain, bachelorsphdMain, masterassociateMain, bachelorphddateMain, \
    masterassociatedateMain
from string import Template

import datetime
import os

generatepath = os.path.abspath(os.getcwd())
processedPath = os.path.abspath(os.getcwd() + "/dictionary/processed")
unprocessedPath = os.path.abspath(os.getcwd() + "/dictionary")
templatePath = os.path.abspath(os.getcwd() + "/ResumeTemplates")
repeatedContentPath = os.path.abspath(os.getcwd() + "/dictionary/otherDictionaries/repeatedContentFiles")

date_now = datetime.datetime.now().time()


def generateImpl(numberofresume):
    dirName = generatepath + "/RandomResumeGenerate/temp_{}_{}".format(datetime.datetime.now().date(), date_now)
    os.makedirs(dirName)
    for _ in range(numberofresume):
        # print(_)

        # Name
        dictName = nameMain()
        unprocessedNameLocation = open(unprocessedPath + "/fullname.lst", "r")
        namelines = unprocessedNameLocation.readlines()
        unprocessedNameLocation = open(unprocessedPath + "/fullname.lst", "w")
        processedNameLocation = open(processedPath + "/fullname", "a")

        for line in namelines:
            if line != dictName + "\n":
                unprocessedNameLocation.write(line)
            if line == dictName + "\n":
                processedNameLocation.write(line)
        unprocessedNameLocation.close()
        processedNameLocation.close()

        # email
        dictEmail = emailMain()
        unprocessedEmailLocation = open(unprocessedPath + "/email", "r")
        emaillines = unprocessedEmailLocation.readlines()
        unprocessedEmailLocation = open(unprocessedPath + "/email", "w")
        processedEmailLocation = open(processedPath + "/email", "a")

        for line in emaillines:
            if line != dictEmail + "\n":
                unprocessedEmailLocation.write(line)
            if line == dictEmail + "\n":
                processedEmailLocation.write(line)
        unprocessedEmailLocation.close()
        processedEmailLocation.close()

        # contactNo
        dictContact = contactNoMain()
        unprocessedContactLocation = open(unprocessedPath + "/contactno", "r")
        contactlines = unprocessedContactLocation.readlines()
        unprocessedContactLocation = open(unprocessedPath + "/contactno", "w")
        processedContactLocation = open(processedPath + "/contactno", "a")

        for line in contactlines:
            if line != dictContact + "\n":
                unprocessedContactLocation.write(line)
            if line == dictContact + "\n":
                processedContactLocation.write(line)
        unprocessedContactLocation.close()
        processedContactLocation.close()

        # address
        dictAddress = addressMain()
        unprocessedAddressLocation = open(unprocessedPath + "/address", "r")
        addresslines = unprocessedAddressLocation.readlines()
        unprocessedAddressLocation = open(unprocessedPath + "/address", "w")
        processedAddressLocation = open(processedPath + "/address", "a")

        for line in addresslines:
            if line != dictAddress + "\n":
                unprocessedAddressLocation.write(line)
            if line == dictAddress + "\n":
                processedAddressLocation.write(line)
        unprocessedAddressLocation.close()
        processedAddressLocation.close()

        # JobTitle
        dictJobTitle = jobMain()
        unprocessedJobLocation = open(unprocessedPath + "/jobtitle.txt", "r")
        joblines = unprocessedJobLocation.readlines()
        unprocessedJobLocation = open(unprocessedPath + "/jobtitle.txt", "w")
        processedJobLocation = open(repeatedContentPath + "/jobtitle", "a")

        for line in joblines:
            if line != dictJobTitle + "\n":
                unprocessedJobLocation.write(line)
            if line == dictJobTitle + "\n":
                processedJobLocation.write(line)
                # print("j1:", line)
        unprocessedJobLocation.close()
        processedJobLocation.close()

        # JobTitle2
        dictJobTitle2 = jobMain()
        unprocessedJobLocation2 = open(unprocessedPath + "/jobtitle.txt", "r")
        joblines2 = unprocessedJobLocation2.readlines()
        unprocessedJobLocation2 = open(unprocessedPath + "/jobtitle.txt", "w")
        processedJobLocation2 = open(repeatedContentPath + "/jobtitle", "a")

        for line in joblines2:
            if line != dictJobTitle2 + "\n":
                unprocessedJobLocation2.write(line)
            if line == dictJobTitle2 + "\n":
                processedJobLocation2.write(line)
                # print("j2:", line)
            else:
                processedJobLocation2.write('')
                # print("jt2Null")
        unprocessedJobLocation2.close()
        processedJobLocation2.close()

        # JobTitle3
        dictJobTitle3 = jobMain()
        unprocessedJobLocation3 = open(unprocessedPath + "/jobtitle.txt", "r")
        joblines3 = unprocessedJobLocation3.readlines()
        unprocessedJobLocation3 = open(unprocessedPath + "/jobtitle.txt", "w")
        processedJobLocation3 = open(repeatedContentPath + "/jobtitle", "a")

        for line in joblines3:
            if line != dictJobTitle3 + "\n":
                unprocessedJobLocation3.write(line)
            if line == dictJobTitle3 + "\n":
                processedJobLocation3.write(line)
                # print("j3:", line)
            else:
                processedJobLocation3.write('')
        unprocessedJobLocation3.close()
        processedJobLocation3.close()

        # Organization
        dictCompany = companyMain()
        unprocessedCompanyLocation = open(unprocessedPath + "/company", "r")
        companylines = unprocessedCompanyLocation.readlines()
        unprocessedCompanyLocation = open(unprocessedPath + "/company", "w")
        processedCompanyLocation = open(repeatedContentPath + "/company", "a")

        for line in companylines:
            if line != dictCompany + "\n":
                unprocessedCompanyLocation.write(line)
            if line == dictCompany + "\n":
                processedCompanyLocation.write(line)
        unprocessedCompanyLocation.close()
        processedCompanyLocation.close()

        # Organization2
        dictCompany2 = companyMain()
        unprocessedCompanyLocation2 = open(unprocessedPath + "/company", "r")
        companylines2 = unprocessedCompanyLocation2.readlines()
        unprocessedCompanyLocation2 = open(unprocessedPath + "/company", "w")
        processedCompanyLocation2 = open(repeatedContentPath + "/company", "a")

        for line in companylines2:
            if line != dictCompany2 + "\n":
                unprocessedCompanyLocation2.write(line)
            if line == dictCompany2 + "\n":
                processedCompanyLocation2.write(line)
        unprocessedCompanyLocation2.close()
        processedCompanyLocation2.close()

        # Organization3
        dictCompany3 = companyMain()
        unprocessedCompanyLocation3 = open(unprocessedPath + "/company", "r")
        companylines3 = unprocessedCompanyLocation3.readlines()
        unprocessedCompanyLocation3 = open(unprocessedPath + "/company", "w")
        processedCompanyLocation3 = open(repeatedContentPath + "/company", "a")

        for line in companylines3:
            if line != dictCompany3 + "\n":
                unprocessedCompanyLocation3.write(line)
            if line == dictCompany3 + "\n":
                processedCompanyLocation3.write(line)
        unprocessedCompanyLocation3.close()
        processedCompanyLocation3.close()

        # University
        dictUni = uniMain()
        unprocessedUniLocation = open(unprocessedPath + "/university_world.lst", "r")
        unilines = unprocessedUniLocation.readlines()
        unprocessedUniLocation = open(unprocessedPath + "/university_world.lst", "w")
        processedUniLocation = open(processedPath + "/university", "a")

        for line in unilines:
            if line != dictUni + "\n":
                unprocessedUniLocation.write(line)
            if line == dictUni + "\n":
                processedUniLocation.write(line)
        unprocessedUniLocation.close()
        processedUniLocation.close()

        # degree
        dictDegree = degreeMain()
        dictBachelorPhdDegree = bachelorsphdMain()
        dictMasterAssociate = masterassociateMain()
        # date
        dictDate = dateMain()
        dictDate1 = dateMain()
        dictDate2 = dateMain()
        dictbachelorphdDate = bachelorphddateMain()
        dictmasterassociateDate = masterassociatedateMain()
        randTemplate = randomTemplate()

        f = open(templatePath + "/" + randTemplate, 'r')
        s = Template(f.read())
        result = s.safe_substitute(Name=dictName, Email=dictEmail, Contact=dictContact, Address=dictAddress,
                                   JobTitle=dictJobTitle, JobTitle2=dictJobTitle2, JobTitle3=dictJobTitle3,
                                   Organization=dictCompany, Organization2=dictCompany2, Organization3=dictCompany3,
                                   University=dictUni, Degree=dictDegree, BDegree=dictBachelorPhdDegree,
                                   MDegree=dictMasterAssociate, Date=dictDate, Date1=dictDate1, Date2=dictDate2,
                                   BDate=dictbachelorphdDate, MDate=dictmasterassociateDate)
        f.close()
        filename = "{}_{}_{}".format(datetime.datetime.now().date(),
                                     datetime.datetime.now().time(), dictName)

        f = open(dirName + "/{}.txt".format(filename), "w")
        result = "".join(result)
        # print("##################################################################################\n",result)
        f.write(result)
        f.close()
