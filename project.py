
import time
import numpy as np
import pandas as pd
import colorama
from colorama import Fore
import bisect
from itertools import permutations
from tkinter import *


'''
GC_Content,
complementSeq,
Reverse,
reverseComplementSeq,
Translation_Table,
Translation

'''
pro = Tk()

pro.geometry('910x500+500+120')

pro.title('GC_Content')
pro.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello\nsection1 ",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)


lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)

lbl1 = Label(fr1, text="please insert subsequence:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=150)
en2 = Entry(fr1, justify='center', bg='wheat', font=10)
en2.place(x=30, y=190)


def FirstFun():
    seq = en1.get()
    sub_seq=en2.get()
    l = len(sub_seq)
    num_G = sub_seq.count("G")
    num_C = sub_seq.count("C")
    total = num_C+num_G
    GC_Content = total/l
    result = Label(fr1, text="The GC_Content :" +
                   str(GC_Content), fg="black", bg="white")
    result.place(x=5, y=280)

    comp = " "
    for i in sub_seq:
        if (i == "A"):
            comp = comp + "T"
        if (i == "T"):
            comp = comp + "A"
        if (i == "C"):
            comp = comp + "G"
        if (i == "G"):
            comp = comp + "C"
        complementSeq = comp
        result = Label(fr1, text="The Complement :" +
                       str(complementSeq), fg="black", bg="white")
    result.place(x=5, y=300)

    Reverse = sub_seq[::-1]
    result = Label(fr1, text="The reverse :" +
                   str(Reverse), fg="black", bg="white")
    result.place(x=5, y=320)

    reverseComplementSeq = complementSeq[::-1]
    result = Label(fr1, text="The reverseComplementSeq :" +
                   str(reverseComplementSeq), fg="black", bg="white")
    result.place(x=5, y=340)

    dic = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
           "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
           "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
           "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
           "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
           "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
           "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
           "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }
    s = ""
    sf = ""
    flag = 0
    for i in range(0, len(seq)-2, 3):
        if dic[seq[i:i+3]] == "M":
            flag = 1
        elif (dic[seq[i:i+3]] == "*"):
            flag = 0
        if flag == 1:
            s += dic[seq[i:i+3]]
        sf += dic[seq[i:i+3]]
    Translation_Table= sf, s
    result = Label(fr1, text="The Translation_Table :" +
                   str(Translation_Table), fg="black", bg="white")
    result.place(x=5, y=360)

    dic = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
           "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
           "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
           "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
           "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
           "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
           "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
           "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
           "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
           "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
           "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }
    x = ''
    for i in range(0, len(seq), 3):
        if dic[seq[i:i+3]] != "*":
            x = x + dic[seq[i:i+3]]
    translations = x
    result = Label(fr1, text="The translation :" +
                   str(translations), fg="black", bg="white")
    result.place(x=5, y=390)




btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=250)
pro.mainloop()





pro1 = Tk()

pro1.geometry('910x500+500+120')
pro1.resizable(False, False)
pro1.title('match')
pro1.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello \n Section2&3",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)

lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)

lbl1 = Label(fr1, text="please insert subsequence:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=150)
en2 = Entry(fr1, justify='center', bg='wheat', font=10)
en2.place(x=30, y=190)


def FirstFun():
    seq = en1.get()
    sub_seq = en2.get()
    x = -1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq == seq[i:i+len(sub_seq)]:
            x = i
    match= x
    result = Label(fr1, text="The match :" +
                   str(match), fg="black", bg="white")
    result.place(x=5, y=280)

    table = np.zeros([4, len(sub_seq)])
    row = ["C", "G", "A", "T"]
    for i in range(4):
        num = -1
        for j in range(len(sub_seq)):
            if row[i] == sub_seq[j]:
                table[i, j] = -1
                num = -1
            else:
                num += 1
                table[i, j] = num
    x = -1
    i = 0
    while (i < len(seq)-len(sub_seq)+1):
        if sub_seq == seq[i:i+len(sub_seq)]:
            x = i
        else:
            for j in range(i+len(sub_seq)-1, i-1, -1):
                if seq[j] != sub_seq[int(j-i)]:
                    k = row.index(seq[j])
                    i += table[k, j-i]
                    break
        i = int(i+1)
    Badchars= x
    result = Label(fr1, text="The Badchars :" +
                   str(Badchars), fg="black", bg="white")
    result.place(x=5, y=300)


btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=250)
pro1.mainloop()


pro2 = Tk()

pro2.geometry('910x500+500+120')
pro2.resizable(False, False)
pro2.title('IndexSorted and query')
pro2.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello \n Section4",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)

lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)

lbl1 = Label(fr1, text="please insert subsequence:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=150)
en2 = Entry(fr1, justify='center', bg='wheat', font=10)
en2.place(x=30, y=190)

lbl1 = Label(fr1, text="please insert key:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=220)
en3 = Spinbox(fr1, from_=1, to=100)
en3.place(x=30, y=250)


def FirstFun():
    seq = en1.get()
    sub_seq = en2.get()
    ln=int(en3.get())
    def IndexSorted(seq, ln):
        index = []
        for i in range(len(seq)-ln+1):
            index.append((seq[i:i+ln], i))
        index.sort()
        return index
    Sorted=IndexSorted(seq, ln)
    result = Label(fr1, text="The IndexSorted :" +
                    str(Sorted), fg="black", bg="white")
    result.place(x=5, y=310)


    t = seq[1][0:-1]
    def query(t, sub_seq, index):
        keys = [r[0] for r in index]
        st = bisect.bisect_left(keys, sub_seq[:len(keys[0])])

        en = bisect.bisect(keys, sub_seq[:len(keys[0])])
        hits = index[st:en]
        print(hits)
        l = [h[1] for h in hits]
        offsets = []
        for i in l:
            if t[i:i+len(sub_seq)] == sub_seq:
                offsets.append(i)
        return offsets
    index = IndexSorted(seq, ln)
    querys=query(t, sub_seq, index)
        
    result = Label(fr1, text="The query :" +
                str(querys), fg="black", bg="white")
    result.place(x=5, y=340)



btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=280)
pro2.mainloop()


pro3 = Tk()

pro3.geometry('910x500+500+120')
pro3.resizable(False, False)
pro3.title('overlaps')
pro3.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello \n Section5",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)

lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)

lbl1 = Label(fr1, text="please insert subsequence:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=150)
en2 = Entry(fr1, justify='center', bg='wheat', font=10)
en2.place(x=30, y=190)

lbl1 = Label(fr1, text="please insert key:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=220)
en3 = Spinbox(fr1, from_=1, to=100)
en3.place(x=30, y=250)


def FirstFun():
    seq = en1.get()
    sub_seq = en2.get()
    ln = int(en3.get())
    def overlap(seq, sub_seq, ln):
        start = 0
        while True:
            start = seq.find(sub_seq[:ln], start)
            if start == -1:
                return 0
            if sub_seq.startswith(seq[start:]):
                return len(seq[start:])
            start += 1
    overlaps = overlap(seq, sub_seq, ln)
    result = Label(fr1, text="The overlaps :" +
                   str(overlaps), fg="black", bg="white")
    result.place(x=5, y=310)

    
    j = len(seq)-1
    count = 0
    for i in range(len(sub_seq)-1, -1, -1):
        if seq[j] == sub_seq[i]:
            count += 1
            j -= 1
        else:
            count = 0
            j = len(seq)-1
            if seq[j] == sub_seq[i]:
                count += 1
                j -= 1
    if count >= ln:
        print('overlap:', count)
    else:
        print("no overlap")
    
    result = Label(fr1, text="The overlaps :" +
                   str(count), fg="black", bg="white")
    result.place(x=5, y=340)

    


btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=280)
pro3.mainloop()




pro4 = Tk()

pro4.geometry('910x500+500+120')
pro4.resizable(False, False)
pro4.title('suffix')
pro4.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello \n Section6 suffix",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)

lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)



def FirstFun():
    seq = en1.get()
    l = []
    for i in range(len(seq)):
        l.append(seq[i:])
    l2 = l.copy()
    l.sort()
    dec = {}
    for i in range(len(l)):
        dec[l[i]] = i
    table = []
    for i in range(len(l)):
        table.append([l2[i], i, dec[l2[i]]])
    result = Label(fr1, text="The suffix :" +
                   str(table), fg="black", bg="white")
    result.place(x=5, y=310)

    


btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=280)
pro4.mainloop()


pro3 = Tk()

pro3.geometry('910x500+500+120')
pro3.resizable(False, False)
pro3.title('distance')
pro3.config(background='wheat')
fr1 = Frame(width='900', height='500', background='white')
fr1.place(x=10, y=10)
lbl1 = Label(fr1, text="Hello \n Section7 distance",
             fg="black", bg="white", font=5)
lbl1.place(x=215, y=20)

lbl2 = Label(fr1, text="please insert sequence:",
             fg="black", bg="white", font=5)
lbl2.place(x=30, y=90)
en1 = Entry(fr1, justify='center', bg='wheat', font=10)
en1.place(x=30, y=120)

lbl1 = Label(fr1, text="please insert subsequence:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=150)
en2 = Entry(fr1, justify='center', bg='wheat', font=10)
en2.place(x=30, y=190)

lbl1 = Label(fr1, text="please insert key:",
             fg="black", bg="white", font=5)
lbl1.place(x=30, y=220)
en3 = Spinbox(fr1, from_=1, to=100)
en3.place(x=30, y=250)


def FirstFun():
    seq = en1.get()
    sub_seq = en2.get()
    ln = int(en3.get())
    dic = {}
    for i in range(0, len(seq)-ln):
        dic[seq[i:i+ln]] = dic.get(seq[i:i+ln], 0)+1
    
    dic2 = {}
    for i in range(0, len(sub_seq)-ln):
        dic2[sub_seq[i:i+ln]] = dic2.get(sub_seq[i:i+ln], 0)+1
    
    k = list(dic.keys())
    for i in range(len(k)):
        dic2[k[i]] = (dic2.get(k[i], 0)-dic[k[i]])
    d = list(dic2.values())
    Sum = 0
    for i in range(len(d)):
        Sum += d[i]**2
    distance = Sum**(0.5)
    
    result = Label(fr1, text="distance between two dna sequences =" +
                   str(distance), fg="black", bg="white")
    result.place(x=5, y=310)


btn1 = Button(fr1, text="Ok", fg='black', bg='wheat',
              cursor='heart', width=10, command=FirstFun)
btn1.place(x=185, y=280)
pro3.mainloop()
