from os.path import exists
import os
import pdf2image

class PDFConverter:

    # Constructor
    def __init__(self,ifile,ofile):
        #self.input_dir_path = os.getcwd()
        #self.output_dir_path = os.getcwd()
        self.input_file = ifile
        self.output_file = ofile

    # Destructor
    def __del__(self):
        pass

    # Methods
    def check_input_file(self):
        if not self.input_file.endswith('.pdf'):
            return 2
        if not exists(self.input_file):
            return 3
        return 0

    def check_output_file(self):
        filename, file_extension = os.path.splitext(self.output_file)
        list_extension = ['.jpg','.jpeg','.tif','.ppm','.png']
        if file_extension in list_extension:
            return 0
        return 4

    def convert(self):
        filename, file_extension = os.path.splitext(self.output_file)
        try:
            images = pdf2image.convert_from_path(self.input_file)
            for i in range(len(images)):
            # Save pages as images in the pdf
                images[i].save(f'{filename}{i}{file_extension}')
            return 0
        except:
            return 5

    # Representation
    def __repr__(self):
        return str(self.__dict__)
