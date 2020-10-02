### flask_converter.py

*The code is incomplete and the works on it have been suspended. Sometimes it works, sometimes it does not, see below if it will be of any use to you :)*

### 0.Prerequisites

You need Python3 (xD), BeautifulSoup4 (for modifying the source html files), and the Flask micro-framework (for running the website). The latter 
two can be obtained through pip. 

### 1. What is this? 

It is a very simple flask background generator for ~~thieves~~ beginner web developers who are working with template webpages. The flask_converter.py is a code 
snippet that re-organises website resource files to a flask-compatible directory convention, replaces all references to said resources in the .html codes with 
appropirate flask nested methods, and generates flask script for running the website on the server (actual deployment requires proper configuration of course, this is just a
preparation)


### 2. How does it work?

It kind of does not. It works 90% of 50% of times. But, it should work rather nicely, provided that your soruce website is structured like this:
MAIN_DIRECTORY:

-->html_src_1.html
-->html_src_2.html
-->html_src_3.html
...
-->html_src_n.html

-->some_assets:
---->pictures_n_stuff:
------>something.jpg

-->some_other_assets:
etc. 
**The thing is, to have only .htmls and asset folders in your website directory.**

To have such site converted into flask compatible mess, you must place the flask_converter.py inside the main directory of the webpage (the same directory where you 
have all your .htmls, see above - there it would be inside the MAIN_DIRECTORY catalogue). 

Run the file (click on it, or execute it through console with python3 flask_converter.py), and in the same directory, the flask_converter_output folder should appear, where you'll have your website converted
into "flask compatibility mode". **HOWEVER** it does not work with some custom .css references in source files, so there will be some artifacts that would have 
to be changed manually (state for the first relase version, this might change :)). 

Now you can execute main.py within said generated folder, and your website should now be set up on your local host, with all the .jss and .csss and pictures and other good stuff.

### 3. Where to steal the templates from?

I tested the code on some of those presented here:
https://www.free-css.com/free-css-templates?start=36
but the file organisation was "not the way the snipped would like it to be" so sometimes it worked, sometimes it did not.

Most of the websites on html5up seem to be compatible though: 
https://html5up.net


### 4. About the project
This is merely an idea I had a month ago while I was sitting on a toilet. Someday I will finish it and then it might be truly useful. For now, follow the guidelines and check 
for yourself if it does work for you :3 cheers


