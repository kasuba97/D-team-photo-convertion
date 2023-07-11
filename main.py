import cv2


print('hey artisee fam please follow these steps:\n1.. copy the extracted folders of Female and Male in the input folder\n2.. overwrite the already existing folders\n3.. rename all images to image (...) by pressing ctl + A, then F2 then type in image')

start = input('4.. input y to start the convention: ')

if start=='y' or start == 'Y':
    print('5.. convention started please wait\n6.. working...')
    try:
        for i in range(20):
            og_img = cv2.imread(f'./input/Female/image ({i+1}).png',1)
            output =  cv2.resize(og_img,(0,0),fx=1024/416,fy=1024/416)
            cv2.imwrite(f'./output/Female/img({i+1}).jpeg',output)
            og_img = cv2.imread(f'./input/Male/image ({i+1}).png',1)
            output =  cv2.resize(og_img,(0,0),fx=1024/416,fy=1024/416)
            cv2.imwrite(f'./output/Male/img({i+1}).jpeg',output)
            
    except:
        ValueError
        KeyError
        print('hey artisee fam please follow these steps:\n1.. copy the extracted folders of Female and Male in the input folder\n2.. overwrite the already existing folders\n3.. rename all images to image (...) by pressing ctl + A, then F2 then type in image')

    print('7.. convention ended successfully :)\n.... find the images in the output folder')
else:
    print('input y after following the steps fam')