import os

#TODO any static varable use capital letter.eg PATH=...
path = "/Users/mingyugai/Downloads/files/"
#read all files in the directory
#TODO any internal function (which not be used outside of the package), start with "_".
#TODO eg. _readAllFiles()
def readAllFiles():
    for root, dirs, files in os.walk(path):
        file_list = files
    return file_list

#select the line start with "en" and also has no suffix
def selectEnstart(line):
#TODO, you do not use if. You can directly return this condition
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
        #TODO, you do split for multiple times which equals the length of temp. You can just do once
        #TODO, before for loop.
        if line.split(' ')[1].startswith(str):
            return False
    return True

#select line that page title not start with lower case
def selectFirstTitle(line):
    #TODO do not need if condition
    if line.split(' ')[1][0].islower() is True:
        return False
    return True

#select line that page title not end with such format
def selectFormat(line):
    temp = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
    #TODO split out of for, just do once.
    for str in temp:
        if line.split(' ')[1][-4:-1] in temp:
            return False
    return True

#select line that page title not have such string
def selectBoilerplate(line):
    temp = ['404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search']
    #TODO same thing
    for str in temp:
        if line.split(' ')[1].find(str) is True:
            return False
    return True
# TODO, normally, if __name__, we do not do such business logic. In __main__, we only part the
# TODO, parameter of application input. For your script, there is no parameter. So just call one
# TODO, main(). And in that function, you can do some business logic. 
if __name__ == '__main__':
    file_list = readAllFiles()
    newfile = []
    for file in file_list:
        #TODO, put such condition when call readAllFiles()
        if file.startswith('page'):
            with open(path + file) as f:
                doc =f.readlines()
                for line in doc:
                    if selectEnstart(line) and selectTitle(line) and selectFirstTitle(line) \
                            and selectFormat(line) and selectBoilerplate(line):
                        newline = "{}\t{}".format(line.split(' ')[1], line.split(' ')[2])
                        #TODO, change the newfile name, which is confusing. eg. newFileList
                        newfile.append(newline)
    #TODO, delete unnecessary print
    print newfile
    #TODO, why keep the try part, delete those debug info. 
    for x in newfile:
        try:
            int(x.split('\t')[1])
        except Exception:
            print x
    newfile.sort(key = lambda x: int(x.split('\t')[1]))
    #TODO, you can write one sub fuction for this logic.
    with open('/Users/mingyugai/Downloads/' + 'testfile.txt', 'w') as f:
        for s in newfile:
            print s
            f.write(s + '\n')
#TODO: Name convention in python may be different from java. So you need to keep in mind what
#TODO: should be like in python
#TODO: class: class ThisIsAClass
#TODO: function: def this_is_a_function
#TODO: variable in fucntion: this_is_a_var
#TODO: variable with a static value: THIS_IS_THIS_YEAR=2017, THIS_IS_MONTH=['Jan', 'Feb',....]
#TODO: private/internal function: _this_is_a_private_function()









