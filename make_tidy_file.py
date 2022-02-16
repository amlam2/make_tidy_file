# Aleh Labovich
# Date: 02/16/2022
# Python version: 3.8.12
# Description: Test exercise PSA


import sys
import os
import re


raw_pattern = r"cast\(\s*(\"?\w*\(*\[*\w*\,*\s*[a-zA-Z0-9…]*\s*\)*\]*\\*\,?\"{0,2})\s*,\s*(\[*\w*\,*\s*\w*\,*\s*\{*\"*\w*\"*\(*\w*\,*\s*\w*\)*\s*=*:*\s*\"*\w*\)*\"*\}*\]*)\s*\)"
pattern = re.compile(raw_pattern)


def to_clean_up(file_name):
    if isinstance(file_name, str):
        temp_file_name = f'{file_name}.temp'
        with open(temp_file_name, 'w') as output_file:
            with open(file_name, 'r') as input_file:
                for line in input_file:
                    line = re.split(r'\s=\s', line.strip())
                    if len(line) > 1:
                        start_of_line = line.pop(0)
                        match_list = pattern.findall(*line)
                        line_for_write = ' = '.join((start_of_line, ', '.join(item[1].strip() for item in match_list)))
                    else:
                        line_for_write = line[0]
                    output_file.write(f'{line_for_write}{chr(10)}')
        os.remove(file_name)
        os.rename(temp_file_name, file_name)
        return True
        # print('Ready!')
    else:
        return False


if __name__ == "__main__":
    os.chdir(os.getcwd())
    if os.path.exists(sys.argv[1]):
        if to_clean_up(sys.argv[1]):
            print('Ready!')
        else:
            print('Something went wrong(')
    else:
        print(f'No such file: "{sys.argv[1]}"')
