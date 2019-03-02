from ResumeCooking.generateImpl import processedPath,unprocessedPath, repeatedContentPath

def uniqueJobTitle():
    uniqueLines = set()
    outfile = open(processedPath + "/jobtitle", "w")
    for line in open(repeatedContentPath + "/jobtitle", "r"):
        if line not in uniqueLines:  # not a duplicate
            outfile.write(line)
            uniqueLines.add(line)
    outfile.close()

def uniqueCompany():
    uniqueLines = set()
    outfile = open(processedPath + "/company", "w")
    for line in open(repeatedContentPath + "/company", "r"):
        if line not in uniqueLines:
            outfile.write(line)
            uniqueLines.add(line)
    outfile.close()
