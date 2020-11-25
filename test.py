import os, docx2txt

def get_doc_text(filepath, file):
 try:
    if file.endswith('.docx'):
       text = docx2txt.process(file)
       return text
    elif file.endswith('.doc'):
       doc_file = filepath + file
       docx_file = filepath + file + 'x'
       os.system('C:\\antiword\\antiword ' + doc_file + ' > ' + docx_file)
       with open(docx_file) as f:
             text = f.read()
       return text
 except :
     pass

