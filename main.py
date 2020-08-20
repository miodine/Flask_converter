from bs4 import BeautifulSoup
from os.path import basename, splitext
import shutil


# elif css['rel'][0] == "stylesheet":
#        css['href'] = '{{url_for(\'static\', filename = \'css/' + \
#            splitext(basename(css['href']))[0] + \
#            splitext(basename(css['href']))[1] + '\')}}'


# TODO: Dodać wszystkie formaty wspierane przez HTML5
formats = ['.jpg', '.png', '.bmp']


# TODO zmienić nazwę na bardziej oddającą to co to robi xd
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


# read file
f = open('index.html', 'r')
html_in = f.read()
f.close()

soup = BeautifulSoup(html_in, 'html.parser')

# re-reference images, obsolete wsm xD
for img in soup.findAll('img'):
    if ("https://" or "http://") in str(img):
        continue
    img['src'] = '{{url_for(\'static\', filename = \'img/' + \
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

                a[attribute_name] = '{{url_for(\'static\', filename = \'img/' + \
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
