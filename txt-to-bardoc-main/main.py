# %%
import PySimpleGUI as sg
import qrcode
import os
from create_doc import create_doc_with_bar
from barcode import Code128
import barcode.writer
import cairosvg
import shutil

def create_txt_selection_gui() -> str:
    """Create a PySimpleGUI window for user to select file to import."""
    file_path = ""
    layout = [[sg.Text('Select .txt file')],
              [sg.InputText(disabled=True, do_not_clear=False),
               sg.FileBrowse()],
              [sg.Text('Sequence Code')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Input your text', layout)

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED:
                break
            case 'Submit':
                file_path = values[0]  # Extract file path in string
                bar_valid_date = values[1]
                if not file_path.endswith('.txt'):
                    sg.popup('Please select file with .txt extension!')
                else:
                    break

    window.close()

    return file_path, bar_valid_date


if __name__ == '__main__':
    # file_path, bar_valid_date = create_txt_selection_gui()
    # file_path = './testing_code.txt'
    # bar_valid_date = ' '

    print(file_path)
    print(bar_valid_date)



    bar_folder_path = './OUT_BAR'
    doc_folder_path = './OUT_DOCX'
    pdf_folder_path = './OUT_PDF'

    if not file_path:
        print("no file selected.")
        exit()

    with open(file_path) as f:
        lines = f.readlines()

        if os.path.exists(bar_folder_path):
            shutil.rmtree(bar_folder_path)
        if os.path.exists(doc_folder_path):
            shutil.rmtree(doc_folder_path)
        if os.path.exists(pdf_folder_path):
            shutil.rmtree(pdf_folder_path)

        os.makedirs(bar_folder_path)
        os.makedirs(doc_folder_path)
        os.makedirs(pdf_folder_path)

        svgCNT = 0
        for line in lines:
            print(line)
            # Check if empty line
            if line == "\n":
                continue
            line = line.replace('\n', '')

            # 产生SVG文件
            svgFile_list = [svgfile for svgfile in os.listdir(bar_folder_path) if svgfile.endswith('.svg')]
            outitem = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}'
            img = barcode.generate('code128',
                                   line,
                                   output=outitem)
            # 将SVG转换成PNG
            inputSVG = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}.svg'
            img_file_path = f'{bar_folder_path}/barcode_{len(svgFile_list) + 1}.png'
            cairosvg.svg2png(url=inputSVG, write_to=img_file_path, dpi=200)
            # 将PNG插入word模板
            print('pdf_pathXXX: ' + f"{pdf_folder_path}/barcode_{(len(os.listdir(pdf_folder_path)) + 1)} ")
            create_doc_with_bar(bar_path=img_file_path,
                                save_path=f"{doc_folder_path}/barcode_{(len(os.listdir(doc_folder_path)) + 1)}.docx",
                                pdf_path=f"{pdf_folder_path}/barcode_{(len(os.listdir(pdf_folder_path)) + 1)}.pdf",
                                bar_valid_date=bar_valid_date)

        print(f"BAR codes created: {len(os.listdir(doc_folder_path))}")
