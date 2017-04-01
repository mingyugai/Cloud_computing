import os

path = "/Users/mingyugai/Downloads/files/"
#read all files in the directory
def readAllFiles():
    for root, dirs, files in os.walk(path):
        file_list = files
    return file_list

#select the line start with "en" and also has no suffix
def selectEnstart(line):
    if line.startswith('en') and len(line.split(' ')[0]) == 2:
        return True
    return False

#select line that the page title not start with such string
def selectTitle(line):
    temp = ['Media:', 'Special:', 'Talk:', 'User:', 'User_talk:','Project:',
            'Project_talk:','File:','File_talk:','MediaWiki:','MediaWiki_talk:',
            'Template:','Template_talk:','Help:','Help_talk:','Category:',
            'Category_talk:','Portal:','Wikipedia:','Wikipedia_talk:']
    for str in temp:
        if line.split(' ')[1].startswith(str):
            return False
    return True

#select line that page title not start with lower case
def selectFirstTitle(line):
    if line.split(' ')[1][0].islower() is True:
        return False
    return True

#select line that page title not end with such format
def selectFormat(line):
    temp = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
    for str in temp:
        if line.split(' ')[1][-4:-1] in temp:
            return False
    return True

#select line that page title not have such string
def selectBoilerplate(line):
    temp = ['404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search']
    for str in temp:
        if line.split(' ')[1].find(str) is True:
            return False
    return True

if __name__ == '__main__':
    file_list = readAllFiles()
    newfile = []
    for file in file_list:
        if file.startswith('page'):
            with open(path + file) as f:
                doc =f.readlines()
                for line in doc:
                    if selectEnstart(line) and selectTitle(line) and selectFirstTitle(line) \
                            and selectFormat(line) and selectBoilerplate(line):
                        newline = "{}\t{}".format(line.split(' ')[1], line.split(' ')[2])
                        newfile.append(newline)
    print newfile
    for x in newfile:
        try:
            int(x.split('\t')[1])
        except Exception:
            print x
    newfile.sort(key = lambda x: int(x.split('\t')[1]))

    with open('/Users/mingyugai/Downloads/' + 'testfile.txt', 'w') as f:
        for s in newfile:
            print s
            f.write(s + '\n')










