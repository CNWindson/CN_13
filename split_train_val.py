from shutil import copyfile

txt_path = 'G:\Fundamental\VOCdevkit\VOC2012\ImageSets\Main/'
label_path = 'G:\Fundamental\VOCdevkit\VOC2012\YOLOlabels/'
pic_path = 'G:\Fundamental\VOCdevkit\VOC2012\JPEGImages/'
train_path = 'G:\Fundamental\VOCdevkit\VOC2012/train/'
test_path = 'G:\Fundamental\VOCdevkit\VOC2012/val/'
train_labels_path = 'G:\Fundamental\VOCdevkit\VOC2012/train_labels/'
val_labels_path = 'G:\Fundamental\VOCdevkit\VOC2012/val_labels/'

with open(txt_path + 'train.txt') as f:
    items = f.readlines()
    for item in items:
        item = item.split('\n')[0]
        copyfile(pic_path + item + '.jpg',train_path + item + '.jpg')
        copyfile(label_path + item + '.txt', train_labels_path + item + '.txt')
    f.close()

with open(txt_path + 'val.txt') as f:
    items = f.readlines()
    for item in items:
        item = item.split('\n')[0]
        copyfile(pic_path + item + '.jpg', test_path + item + '.jpg')
        copyfile(label_path + item + '.txt', val_labels_path + item + '.txt')
    f.close()


