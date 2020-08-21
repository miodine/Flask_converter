from bs4 import BeautifulSoup
import os
import shutil


# elif css['rel'][0] == "stylesheet":
#        css['href'] = '{{url_for(\'static\', filename = \'css/' + \
#            splitext(basename(css['href']))[0] + \
#            splitext(basename(css['href']))[1] + '\')}}'


formats = ['.png', '.bmp', '.jpg', '.jpeg',
           '.jfif', '.pjpeg', '.pjp', '.svg',
           '.apng', '.ico,', '.cur', '.tif', '.tiff',
           '.webp', '.webm', '.mp4', '.mp3']


def list_skim(list_of_strings, target_string):
    # If target string is present in the list of strings, return its index
    # if not, return -1
    present = False
    for i in range(len(list_of_strings)):
        if list_of_strings[i] in target_string:
            present = True
            return i
    if not present:
        return -1


# GET path and directories:
path = os.path.dirname(__file__)
print(path)
list_dir = os.listdir(path)
target_dir = path + '\Flask_converter_output'

try:
    os.mkdir(target_dir)
except OSError:
    print("Creation of the directory %s failed" % path)
    print("Directory already exist!")
    exit()
else:
    print("Successfully created the directory %s " % path)

try:
    os.mkdir(target_dir + "\\templates")
except OSError:
    print("Creation of the directory %s failed" % path)
    print("Directory already exist!")
    exit()
else:
    print("Successfully created the directory %s " % path)

try:
    os.mkdir(target_dir + '\\static')
except OSError:
    print("Creation of the directory %s failed" % path)
    print("Directory already exist!")
    exit()
else:
    print("Successfully created the directory %s " % path)


htmls = {}


for i in list_dir:
    if '.html' in str(i):
        f = open(path + "\\" + i, 'r')
        htmls.update({i: f.read()})
        f.close()
        shutil.copy(path + '\\' + i, target_dir + "\\templates")
        continue

    elif '.txt' in i:
        shutil.copy(path + '\\' + i, target_dir + "\\")
        continue
    elif ('.py' or '\Flask_converter') in i:
        continue
    else:
        shutil.copytree(path + "\\" + i, target_dir + '\\static\\' + i)


f = open('index.html', 'r')
html_in = f.read()
f.close()

soup = BeautifulSoup(html_in, 'html.parser')

# re-reference images, obsolete wsm xD
for img in soup.findAll('img'):
    if ("https://" or "http://") in str(img):
        continue
    img['src'] = '{{url_for(\'static\', filename = ' + \
        img['src'] + '\')}}'


# re-reference stylesheets
for css in soup.findAll('link'):
    if ("https://" or "http://") in str(css):
        continue

    elif css['rel'][0] == "stylesheet":
        css['href'] = '{{url_for(\'static\', filename = \'css/' + \
            css['href'] + '\')}}'


# re-reference hyperlinks // wsm można zastąpić tym to pierwsze co powyżej xD
for a in soup.findAll('a'):
    if ("https://" or "http://") in str(a):
        continue
    else:

        attribute_name = ''
        i = list_skim(formats, str(a))
        if i == -1:
            continue

        for j in range(len(list(a.attrs.values()))):
            if formats[i] in list(a.attrs.values())[j]:
                attribute_name = list(a.attrs.keys())[j]
                a[attribute_name] = '{{url_for(\'static\', filename = ' + \
                    a[attribute_name] + '\')}}'

                print(a[attribute_name])

# re-reference local javascripts
for js in soup.findAll('script'):

    i = list_skim(list(js.attrs.keys()), 'src')

    if i == -1:
        continue

    js['src'] = '{{url_for(\'static\', filename = \'js/' + \
        js['src'] + '\')}}'


# TODO re-reference of other assets
# TODO copying default files to proper directories(imgs and htmls)


# TODO add Flask file generator
# TODO popraw ścieżki plików; zamiast np.zmieniać assets/css/xd.css na static/css/xd.css, zmieniać na
#      static/assets/css/xd.css

# TODO encapsulate

#             |||
# return this VVV jak już będzie klasa xddD


html_out = str(soup)
