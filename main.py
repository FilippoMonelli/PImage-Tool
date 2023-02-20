#!/usr/bin/python

import os
import sys
from pdfconverter import PDFConverter


def input_filename():
    print('Insert path of pdf input file')
    filename = input()
    #path_file = os.getcwd() + "/" + str(filename) + ".pdf"
    path_file = str(filename)
    return path_file

def syntax():
    error("Syntax: main.py <pdf_input_file> <img_output_file>",1)

def error(msg,error_code):
    print(msg)
    print(f"Error code {error_code}")
    exit(error_code)

def main():

    # Input control
    if len(sys.argv) != 3:
        syntax()
    
    input = sys.argv[1]
    output = sys.argv[2]
    converter = PDFConverter(input,output) 

    #print(converter.__repr__)
    ret = converter.check_input_file()
    if (ret != 0):
        if ret == 2:
            error("Error: <pdf_input_file> extention is incorrect",ret)
        elif ret == 3:
            error("Error: <pdf_input_file> does not exists")
    ret = converter.check_output_file()
    if (ret != 0):
        error("Error: <img_output_file> extention is incorrect(supported: JPEG,PNG,TIFF,PPM)",ret)
    
    ret = converter.convert()
    if (ret != 0):
        error("Error: something goes wrong")
    print("Convertion completed")
    return 0

    """
    answer = 'n'
    # Store Pdf with convert_from_path function
    print('PImage Tool')
    print('You can convert a PDF file in images (supported: JPEG, PNG, TIFF, PPM)\n')

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
    """
    
if __name__=="__main__":
    main()
