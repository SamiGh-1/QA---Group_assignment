import re
def get_function_name(string):
    try:
        found = re.search('def (.+?) ?\(', string).group(1)
        return found
    except AttributeError:
        pass

def get_args(string):
    try:
        found = re.search('\((.+?)\)', string).group(1)
        return found
    except AttributeError:
        pass

# in python the function parameters dont have types so I just matched the No. of params to match the attributes sent to the function
def check_attribs(filepath):
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            if line.startswith("def"):
                func_name = get_function_name(line)
                args = get_args(line)
                args_no = args.count(',')
                with open(filepath) as fp1:
                    line1 = fp1.readline()
                    cnt1 = 1
                    while line1:
                        if func_name in line1:
                            if 'def' not in line1:
                                #print("Line {}: {}".format(cnt1, line1.strip()))
                                args1 = get_args(line1)
                                args1_no = args1.count(',')
                                if args_no != args1_no:
                                    print('No. of attributes doesnt match in ',line1)
                        line1 = fp1.readline()
                        cnt1 += 1
            line = fp.readline()
            cnt += 1

def main():
    path = 'python.txt'
    check_attribs(path)
# the file is attached and has one wrong function call

if __name__ == "__main__":
    main()