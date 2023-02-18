#!/usr/bin/python
import pdf2image
import os

def input_filename():
    print('Insert path of pdf input file')
    filename = input()
    #path_file = os.getcwd() + "/" + str(filename) + ".pdf"
    path_file = str(filename)
    return path_file

def main():
    answer = 'n'
    # Store Pdf with convert_from_path function
    print('Welcome in CLI_PDFtoImg_version_0.1\n')
    #print('+---------------------------------- REMEMBER ------------------------------+')
    #print('|                                                                          |')
    #print('| Remember to put inside program directory the files that you want convert |')
    #print('|                                                                          |')
    #print('+--------------------------------------------------------------------------+')
    
    while answer != 'y': 
        path_file = input_filename()
        print('The path \"' + path_file + '\" is correct? (y or n)')
        answer = str(input()).lower()
    try:
        print('Insert path output file')
        output = str(input())
        images = pdf2image.convert_from_path(path_file)
        
        for i in range(len(images)):
        # Save pages as images in the pdf
            images[i].save(output + str(i) +'.jpg', 'JPEG')
        
        print('Convertion completed\nGoodbye.')
    except:
        print('Something goes wrong with file or file path.\nGoodbye.')
    
if __name__=="__main__":
    main()
