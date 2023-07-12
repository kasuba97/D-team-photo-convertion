import cv2
import termcolor as tc
import os

print('hey fam, please follow these steps:\n[1] copy the extracted folders of Female and Male in the input folder')
todo = input(
    '[?] type b: for both folders|| f: for only female|| m: for only male: ')
start = input('[?] input y to start the convertion: ')


def img_conv(command):
    print('[✓] convention started please wait')

    def lady_work():
        try:
            tc.cprint('[✓] working on female folder...','yellow')
            input_female = os.fspath('./input/Female/')
            files = os.listdir(input_female)
            for file in files:
                og_img = cv2.imread(f'./input/Female/{file}', 1)
                output = cv2.resize(og_img, (0, 0), fx=1024/416, fy=1024/416)
                cv2.imwrite(f'./output/Female/{file}).jpeg', output)
            return tc.cprint('[✓] convertion for female folder ended successfuly\n[-] find images in the output/Female','green')
        except:
            tc.cprint('[X] something went wrong please follow step 1','red')
            ValueError
            KeyError
            TypeError


    def man_work():
        try:
            tc.cprint('[✓] working on male folder...','yellow')
            input_male = os.fspath('./input/Male/')
            files = os.listdir(input_male)
            for file in files:
                og_img = cv2.imread(f'./input/Male/{file}', 1)
                output = cv2.resize(og_img, (0, 0), fx=1024/416, fy=1024/416)
                cv2.imwrite(f'./output/Male/{file}', output)
            return tc.cprint('[✓] convertion for male folder ended successfuly\n[-] find images in output/Male','green')
        except:
            tc.cprint('[X] something went wrong please follow step 1','red')
            ValueError
            KeyError
            TypeError

    if command == 'b' or command == 'B':
        lady_work()
        man_work()
    elif command == 'f' or command == 'F':
        lady_work()
    elif command == 'm' or command == 'M':
        man_work()
    else:
        return print('invalid command was passed')


if start == 'y' or start == 'Y':
    img_conv(todo)
