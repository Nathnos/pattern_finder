# pattern_finder
A script that tries to find a specific pattern in all files of a folder (and optionally its subfolders). Capital or lowercase are not taken into acount.

Examples of use :
--------
- You want to search in your current directory (and its subfolders) if a file contains the word "Flowy" :  
<code>python3 pattern_finder.py -sf -p "Flowy"</code>

- You want to find screenshots you made of a python code, in the "Picture" folder :  
<code>python3 pattern_finder.py -sf --path "/home/username/Pictures" --image -p "import"</code>

- You want to find a piece of code, but you can't remember where it is stored
<code>python3 pattern_finder.py -sf --path "path_to_project_folder" --ignore ".git/my_virtalenv/requirements.txt" --pattern "def prime_numbers("</code>

- If you copied the script folder in your Document folder, which also contain "my_pdf" directory, and you want to find out which pdf are about cats
<code>python3 pattern_finder.py -sf --pdf --path "my_pdf" --pattern "cat"</code>

Arguments :
--------
__-p, --pattern :__
Pattern to find - spaces not allowed. Required, but if you don't  
__--path :__
Search in a specific folder  
__-sf, --subfolders :__
Search also in subfolders. Can be long.  
__-pdf, --pdf :__
Search also in PDF documents. Can be long.   
__-i, --ignore :__
Ignore all folders and files with a specific name. To define multiples forbidden folder and file names, put a slash between each : fold1/fold2/readme.md  
__--image :__
Also search the pattern in images. You'll need tesseract to use this option. Don't work very well, anyways. Can be quite long. Extensions allowed : png, jpg, jpeg, bmp and webp  
