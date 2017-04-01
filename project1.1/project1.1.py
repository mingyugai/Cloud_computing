import os
import argparse

#read all files in the directory
def _read_all_files(input_path):
    file_list = []
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.startswith('pagecount'):
                file_list.append(file)
    return file_list

#select the line start with "en" and also has no suffix
def _select_enstart(line):
    return line.startswith('en') and len(line.split(' ')[0]) == 2

#select line that the page title not start with such string
def _select_title(line):
    temp = ['Media:', 'Special:', 'Talk:', 'User:', 'User_talk:','Project:',
            'Project_talk:','File:','File_talk:','MediaWiki:','MediaWiki_talk:',
            'Template:','Template_talk:','Help:','Help_talk:','Category:',
            'Category_talk:','Portal:','Wikipedia:','Wikipedia_talk:']
    split = line.split(' ')
    for str in temp:
        if split[1].startswith(str):
            return False
    return True

#select line that page title not start with lower case
def _select_first_title(line):
    return line.split(' ')[1][0].islower()

#select line that page title not end with such format
def _select_format(line):
    temp = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
    split = line.split(' ')
    for str in temp:
        if split[1][-4:-1] in temp:
            return False
    return True

#select line that page title not have such string
def _select_boilerplate(line):
    temp = ['404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search']
    split = line.split(' ')
    for str in temp:
        if split[1].find(str) is True:
            return False
    return True

#output the file
def _write_files(out_path, out_file_list, name):
    with open(out_path + name, 'w') as f:
        for s in out_file_list:
            f.write(s + '\n')

def main(args):
    file_list = _read_all_files(args.input_path)
    newfile_list = []
    for file in file_list:
        # TODO, put such condition when call readAllFiles()
        with open(args.input_path + file) as f:
            doc = f.readlines()
            for line in doc:
                if _select_enstart(line) and _select_title(line) and _select_first_title(line) \
                        and _select_format(line) and _select_boilerplate(line):
                    newline = "{}\t{}".format(line.split(' ')[1], line.split(' ')[2])
                    newfile_list.append(newline)
    newfile_list.sort(key=lambda x: int(x.split('\t')[1]))
    _write_files(args.out_path, newfile_list, args.name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-path",  help="input file path")
    parser.add_argument("-o", "--out-path", help="output file path")
    parser.add_argument("-n", "--name",help="file name of output")
    args = parser.parse_args()
    main(args)









