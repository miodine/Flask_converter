from bs4 import BeautifulSoup
from os.path import basename, splitext
import shutil


class Flask_format(BeautifulSoup):
    # BEGIN: CLASS VARIABLES
    formats = ['.jpg', '.png', '.bmp']
# END: CLASS VARIABLES

# BEGIN: HELPER FUNCTIONS
    def list_skim(self, list_of_strings, target_string):
        # If target string is present in the list of strings, return its index
        # if not, return -1
        present = False
        for i in range(len(list_of_strings)):
            if list_of_strings[i] in target_string:
                present = True
                return i
        if not present:
            return -1
# END: HELPER FUNCTIONS

# BEGIN: CORE FUNCTIONS
    def format_contents(self, tag, soup):
        # search through all 'tag's and modify local sources in a Flask compatible way
        # TODO: add copy pasterinio del contento por formato flasko mamma mia
        for tag_ in soup.findAll(str(tag)):
            if ("https://" or "http://") in str(tag_):
                continue
            else:

                attribute_name = ''
                i = self.list_skim(self.formats, str(tag_))
                if i == -1:
                    continue

                for j in range(len(list(tag_.attrs.values()))):
                    if self.formats[i] in list(tag_.attrs.values())[j]:
                        attribute_name = list(tag_.attrs.keys())[j]

                        tag_[attribute_name] = '{{url_for(\'static\', filename = \'img/' + \
                            tag_[attribute_name] + '\')}}'
# END: CORE FUNCTIONS
