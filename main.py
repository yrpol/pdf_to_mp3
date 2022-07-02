from unicodedata import name
from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\nEnjoy!'

    else:
        return 'File not foud! Please check the path.'


def main():
    print('Convert your pdf file to mp3!')
    file_path = input('\nEnter a file path: ')
    language = input('\nChoose language (for example "en" of "uk"): ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()
