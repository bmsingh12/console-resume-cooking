import random, os


def get_items(filename):
    with open(filename) as text_file:
        return list(set(word.strip() for word in text_file))


def random_words(n, words):
    return " ".join(random.choice(words) for _ in range(n))


def nameMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/fullname.lst")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def emailMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/email")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def contactNoMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/contactno")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def addressMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/address")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def uniMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/university_world.lst")
    words = get_items(filename)
    # while True:
    # n = int(input("Number of words:"))
    n = 1
    return random_words(n, words)


# degrees
def degreeMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/degree")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def bachelorsphdMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/bachelordegree")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def masterassociateMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/masterassociatedegree")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


####

def companyMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/company")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


def jobMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/jobtitle.txt")
    words = get_items(filename)
    n = 1
    return random_words(n, words)


# dates
def dateMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/date")
    dates = get_items(filename)
    n = 1
    # for _ in dates:
    return random_words(n, dates)


def bachelorphddateMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/bachelorsdate")
    dates = get_items(filename)
    n = 1
    # for _ in dates:
    return random_words(n, dates)


def masterassociatedateMain():
    filename = os.path.abspath(os.getcwd() + "/dictionary/mastersdate")
    dates = get_items(filename)
    n = 1
    # for _ in dates:
    return random_words(n, dates)


# # # #

# testing
# def alpha():
#     filename = "/home/infotmt-user/PycharmProjects/ResumeCooking/ResumeCooking/dictionary/f1"
#     words = get_items(filename)
#     n = 1
#     return random_words(n, words)


def randomTemplate():
    return random.choice(os.listdir(os.path.abspath(os.getcwd() + "/ResumeTemplates/")))

def randomResume():
    return random.choice(os.listdir(os.path.abspath(os.getcwd() + "/RandomResumeGenerate/")))