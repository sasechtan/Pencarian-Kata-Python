from tkinter import *
import pandas as pd

class Custombox:
    def __init__(self, title, text):
        self.title = title
        self.text = text

        def store():
            kataBaku = ['abjad', 'advokat', 'aktif', 'al quran', 'apotek', 'asas',
                        'atlet', 'atmosfer', 'baut', 'berpikir', 'besok', 'bus',
                        'cabai', 'cendekiawan', 'cenderamata', 'daftar', 'definisi', 'Ddepot',
                        'detail', 'diagnosis', 'diesel', 'dipersilakan', 'dolar', 'ekspor',
                        'ekstrem', 'ekulvalen', 'embus', 'februari', 'film', 'fisik',
                        'fondasi', 'formal', 'foto', 'frekuensi', 'gizi', 'gladi',
                        'hafal', 'hak', 'hakikat', 'hierarki', 'hipotesis', 'ijazah',
                        'ikhlas', 'imbau', 'indera', 'insaf', 'istri', 'izin', 
                        'jadwal', 'jenazah', 'jenderal', 'justru', 'kaidah', 'karier',
                        'kategori', 'komplet', 'konferensi', 'kongres', 'konkret', 'kreatif',
                        'kreativitas', 'kualifikasi', 'kuantitatif', 'kualitas', 'kuitansi', 'kiai',
                        'lubang', 'maaf', 'makhluk', 'manajemen', 'manajer', 'mencolok',
                        'menerjemahkan', 'mengesampingkan', 'merek', 'meterai', 'metode', 'mesti',
                        'museum', 'motif', 'motivasi', 'nasihat', 'november', 'napas',
                        'objek', 'paham', 'paspor', 'pikir', 'praktik', 'provinsi',
                        'risiko', 'rezeki', 'saksama', 'sekadar', 'sekretaris', 'silakan',
                        'sistem', 'subjek', 'sutera', 'syukur']
            z = str(input('Masukkan kata : '))
            a = z in kataBaku
            if a == True:
                print(f'kata {z} merupakan kata baku sesuai pada database kami')
            else:
                print(f'kata {z} tidak ada dalam database kami, silahkan periksa di')
                print(f'http://kbbi.kemdikbud.go.ig/entri/{z}')
            
        self.win = Toplevel()
        self.win.title(self.title)
        # self.win.geometry('400x150')
        self.win.wm_attributes('-topmost', True)

        self.label = Label(self.win, text=self.text)
        self.label.grid(row=0, column=0, pady=(20, 10),columnspan=3,sticky='w',padx=10)

        self.l = Label(self.win)

        self.entry = Entry(self.win, width=50)
        self.entry.grid(row=1, column=1,columnspan=2,padx=10)

        self.b1 = Button(self.win, text='Ok', width=10,command=store)
        self.b1.grid(row=3, column=1,pady=10)

        self.b2 = Button(self.win, text='Cancel', width=10,command=self.win.destroy)
        self.b2.grid(row=3, column=2,pady=10)
        
    def __str__(self): 
        return str(self.new)

    def change(self,ran_text):
        self.l.config(text=ran_text,font=(0,8))
        self.l.grid(row=2,column=1,columnspan=3,sticky='nsew',pady=5)


root = Tk()
root.withdraw()

a = Custombox('Mencari Kata Baku', 'Masukkan kata ')

root.mainloop()
