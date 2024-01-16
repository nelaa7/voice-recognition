import speech_recognition as srec
from gtts import gTTS
import os
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan....')
        suara = mendengar.listen(source, phrase_time_limit=5)
        try: 
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except: 
            pass
        return dengar

def ngomong(teks):
    bahasa = 'id'
    namafile = 'ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
    reading()

def jawab_pertanyaan(pertanyaan):
    lemmatizer = WordNetLemmatizer()
    pertanyaan_lemmatized = ' '.join([lemmatizer.lemmatize(word) for word in pertanyaan.split()])
    
    if "nama kamu siapa" in pertanyaan_lemmatized.lower():
        return "Nama saya Michelle"
    # Tambahkan kondisi lain sesuai dengan pertanyaan yang ingin dijawab

    return "Maaf, saya tidak dapat mengenali pertanyaan tersebut."

def run_michelle():
    pertanyaan = perintah()
    ngomong(jawab_pertanyaan(pertanyaan))

run_michelle()
