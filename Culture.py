import tkinter as tk
import random

def Caste0():
    Caste = ['All equal', 'Strong Lead', 'Born Into', 'Employment', 'Skill']
    rand_caste = random.choice(Caste)
    caste_label.config(text=rand_caste)
    top.update()
def Gender0():
    Gender = ['Equal', 'Patriacle', 'Matriachal']
    rand_gender = random.choice(Gender)
    gender_label.config(text=rand_gender)
    top.update()
def Religion0():
    Religion = ['No one major religion', 'Monothieistic', 'Polythieistic', 'Atheistic']
    rand_religion = random.choice(Religion)
    religion_label.config(text=rand_religion)
    top.update()
def Authority0():
    Authority = ['No major authority', 'Single ruler', 'Council', 'Single ruler with council', 'Elected single ruler', 'Elected council', 'Elected single ruler and council']
    rand_authority = random.choice(Authority)
    authority_label.config(text=rand_authority)
    top.update()
def Langague0():
    Language = ['Abundance of language', 'One major language', 'A couple major languages']
    rand_language = random.choice(Language)
    language_label.config(text=rand_language)
    top.update()
def Food0():
    Food = ['Focus on spices', 'Focus on herbs', 'Focus on sweetness', 'Focus on savory', 'Focus on unseasoned', 'Mixed food focus', 'All focuses']
    rand_food = random.choice(Food)
    food_label.config(text=rand_food)
    top.update()
def Art0():
    Art = ['Focus on abstract', 'Focus on realism', 'Focus on realism', 'Focus on impressionism', 'No real focus', 'Sporatic focus']
    rand_art = random.choice(Art)
    art_label.config(text=rand_art)
    top.update()
def Event0():
    Events = ['No major events', 'A few major events', 'Events through the year']
    rand_event = random.choice(Events)
    event_label.config(text=rand_event)
    top.update()
def Music0():
    Music = ['String focus', 'Woodwind focus', 'Percussion focus', 'Brass focus', 'Mixed focus', 'No focus', 'Wide focus']
    rand_music = random.choice(Music)
    music_label.config(text=rand_music)
    top.update()
def Resource0():
    Resource = ['Inland-water', 'Ocean', 'Farmland', 'Lumber', 'Quarry[stone]', 'Mine[ores/gems]', 'Finished Goods', 'Exotics']
    rand_resource = random.choice(Resource)
    res_label.config(text=rand_resource)
    top.update()
def Trade0():
    Trade = ['Abundance', 'Some', 'Very little', 'None']
    rand_trade = random.choice(Trade)
    trade_label.config(text=rand_trade)
    top.update
def Culture0():
    Caste0()
    Gender0()
    Religion0()
    Authority0()
    Langague0()
    Food0()
    Art0()
    Event0()
    Music0()
    Resource0()
    Trade0()

top = tk.Tk()
top.wm_title("Culture")
top.minsize(width=290, height=310)
top.maxsize(width=290, height=310)

b0 = tk.Button(text='Roll All', command=Culture0)
b0.config(width=40, height=1)
b0.grid(row=0, column=0, columnspan=2, sticky='w')

b1 = tk.Button(top, text='Roll Caste', command=Caste0, anchor='w')
b1.config(width=15, height=1)
b1.grid(row=1, column=0)

b2 = tk.Button(top, text='Roll Gender', command=Gender0, anchor='w')
b2.config(width=15, height=1)
b2.grid(row=2, column=0)

b3 = tk.Button(top, text='Roll Religion', command=Religion0, anchor='w')
b3.config(width=15, height=1)
b3.grid(row=3, column=0)

b4 = tk.Button(top, text='Roll Authority', command=Authority0, anchor='w')
b4.config(width=15, height=1)
b4.grid(row=4, column=0)

b5 = tk.Button(top, text='Roll Language', command=Langague0, anchor='w')
b5.config(width=15, height=1)
b5.grid(row=5, column=0)

b6 = tk.Button(top, text='Roll Food', command=Food0, anchor='w')
b6.config(width=15, height=1)
b6.grid(row=6, column=0)

b7 = tk.Button(top, text='Roll Art', command=Art0, anchor='w')
b7.config(width=15, height=1)
b7.grid(row=7, column=0)

b8 = tk.Button(top, text='Roll Event', command=Event0, anchor='w')
b8.config(width=15, height=1)
b8.grid(row=8, column=0)

b9 = tk.Button(top, text='Roll Music', command=Music0, anchor='w')
b9.config(width=15, height=1)
b9.grid(row=9, column=0)

b10 = tk.Button(top, text='Roll Resources', command=Resource0, anchor='w')
b10.config(width=15, height=1)
b10.grid(row=10, column=0)

b11 = tk.Button(top, text='Roll Import', command=Trade0, anchor='w')
b11.config(width=15, height=1)
b11.grid(row=11, column=0)

caste_label = tk.Label(text='Roll Caste', anchor='w', width=30)
caste_label.grid(row=1, column=1)
gender_label = tk.Label(text='Roll Gender', anchor='w', width=30)
gender_label.grid(row=2, column=1)
religion_label = tk.Label(text='Roll Religion', anchor='w', width=30)
religion_label.grid(row=3, column=1)
authority_label = tk.Label(text='Roll Authority', anchor='w', width=30)
authority_label.grid(row=4, column=1)
language_label = tk.Label(text='Roll Language', anchor='w', width=30)
language_label.grid(row=5, column=1)
food_label = tk.Label(text='Roll Food', anchor='w', width=30)
food_label.grid(row=6, column=1)
art_label = tk.Label(text='Roll Art', anchor='w', width=30)
art_label.grid(row=7, column=1)
event_label = tk.Label(text='Roll Event', anchor='w', width=30)
event_label.grid(row=8, column=1)
music_label = tk.Label(text='Roll Music', anchor='w', width=30)
music_label.grid(row=9, column=1)
res_label = tk.Label(text='Roll Resources', anchor='w', width=30)
res_label.grid(row=10, column=1)
trade_label = tk.Label(text='Roll Import', anchor='w', width=30)
trade_label.grid(row=11, column=1)

top.mainloop()