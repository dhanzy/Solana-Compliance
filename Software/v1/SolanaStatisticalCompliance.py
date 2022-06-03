# Copyright Fortior Blockchain, LLLP 2022
# Statistical Compliance on Solana
# Apache License

# Widgets:
from tkinter import *
from tkinter.messagebox import *

# Natural Language Ratings
natural_language_compression = {'good':0.75, 'acceptable':0.5, 'outstanding': 1, 'unacceptable': 0, 'marginal': .25}

# Frontend
## The frontend is a simple user interface.
master = Tk()
label0 = Label(master, text = 'Equity', relief = 'groove', width = 12)
label1 = Label(master, text = 'Decentralization', relief = 'groove', width = 12)
label2 = Label(master, text = 'Participation', relief = 'groove', width = 12)
label3 = Label(master, text = 'Investment', relief = 'groove', width = 12)
label4 = Label(master, text = 'Utility', relief = 'groove', width = 12)
label5 = Label(master, text = 'Purpose', relief = 'groove', width = 12)
label6 = Label(master, text = 'Control', relief = 'groove', width = 12)
label7 = Label(master, text = 'Derivatives', relief = 'groove', width = 12)
label8 = Label(master, text = 'Common Enterprise', relief = 'groove', width = 12)
label8 = Label(master, text = 'Compliance Score', relief = 'groove', width = 20)
entry0 = Entry(master, relief = 'groove', width = 12)
entry1 = Entry(master, relief = 'groove', width = 12)
entry2 = Entry(master, relief = 'groove', width = 12)
entry3 = Entry(master, relief = 'groove', width = 12)
entry4 = Entry(master, relief = 'groove', width = 12)
entry5 = Entry(master, relief = 'groove', width = 12)
entry6 = Entry(master, relief = 'groove', width = 12)
entry7 = Entry(master, relief = 'groove', width = 12)
entry8 = Entry(master, relief = 'groove', width = 12)
blank0 = Entry(master, relief = 'groove', width = 20)

# Backend
# The backend is an artificial intelligence (AI) program for automating compliance analysis.
# The AI program uses an embedded knowledge and a geometric mean to capture human intuition and provide intelligent analysis.
def compliance_ai():
    intuitive_ratio = 1/9
    embedded_knowledge = float(mydict[entry0.get()]) * float(mydict[entry1.get()]) * float(mydict[entry2.get()]) *
    float( mydict[entry3.get()]) * float(mydict[entry4.get()]) * float(mydict[entry5.get()]) *
    float(mydict[entry6.get()]) * float(mydict[entry7.get()] * float(mydict[entry8.get()])
    intelligent_analysis = embedded_knowledge ** intuitive_ratio
    blank0.insert(0, intelligent_analysis)
button0 = Button(master, text = 'Calculate SPL Token Compliance', relief = 'groove', width = 20, command =compliance_ai)

# Frontend
## The frontend is a simple user interface.
label0.grid( row = 1, column = 1, padx = 10 )
label1.grid( row = 2, column = 1, padx = 10 )
label2.grid( row = 3, column = 1, padx = 10 )
label3.grid( row = 4, column = 1, padx = 10 )
label4.grid( row = 5, column = 1, padx = 10 )
label5.grid( row = 6, column = 1, padx = 10 )
label6.grid( row = 7, column = 1, padx = 10 )
label7.grid( row = 8, column = 1, padx = 10 )
label8.grid( row = 9, column = 1, padx = 10 )
entry0.grid( row = 1, column = 2, padx = 10 )
entry1.grid( row = 2, column = 2, padx = 10 )
entry2.grid( row = 3, column = 2, padx = 10 )
entry3.grid( row = 4, column = 2, padx = 10 )
entry4.grid( row = 5, column = 2, padx = 10 )
entry5.grid( row = 6, column = 2, padx = 10 )
entry6.grid( row = 7, column = 2, padx = 10 )
entry7.grid( row = 8, column = 2, padx = 10 )
entry8.grid( row = 9, column = 2, padx = 10 )
blank0.grid( row = 3, column = 3, padx = 10 )
button0.grid( row = 4, column = 3, columnspan = 2)

# Software Title
master.title('Statistical Compliance on Solana')
