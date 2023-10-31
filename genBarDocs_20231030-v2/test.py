from docx2pdf import convert

inputfile1='./barcode_1.docx'
inputfile2='./barcode_2.docx'
inputfile3='./barcode_3.docx'

convert(input_path=inputfile1,output_path='.\input_pdf1.pdf')
convert(input_path=inputfile2,output_path='.\input_pdf2.pdf')
convert(input_path=inputfile3,output_path='.\input_pdf3.pdf')
