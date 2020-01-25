#言語論テスト対策システム
import random
import sys
import tkinter
import pandas as pd
import numpy as np
import os
#import dask as ddf


root = tkinter.Tk()

question_data = pd.read_csv('questions.csv',parse_dates=True)
q_np=np.array(question_data)
def start():
    root.title('プログラミング言語論対策だぁぁぁ')
    root.geometry("500x400")
    start_button.grid(column=1,row=0,padx=60,pady=60)

def question():
    reset()
    global q_num,a_num
    q_num=random.randint(0,len(question_data)-1)
    a_num=q_num
    write_answer.delete(0,tkinter.END)
    q_label["text"]=q_np[q_num][0]
    q_turn.grid(column=0,row=0)
    q_label.grid(column=0,row=1,padx=60,pady=60)
    write_answer.grid(column=0,row=2,padx=60,pady=30)
    q_button.grid(column=0,row=3,padx=60,pady=60)


def answer():
    reset()
    global q_num,a_num
    a_label["text"]=q_np[a_num][1]
    a_turn.grid(column=0,row=0)
    a_label.grid(column=0,row=1,padx=60,pady=60)
    a_button.grid(column=0,row=3,padx=60,pady=60)


def reset():
    start_button.grid_remove()
    q_label.grid_remove()
    q_button.grid_remove()
    a_label.grid_remove()
    a_button.grid_remove()
    q_turn.grid_remove()
    a_turn.grid_remove()

#define
start_button=tkinter.Button(text="Start!",command=question)
q_label=tkinter.Label(text='')
q_button=tkinter.Button(text='Here is Answer!',command=answer)
write_answer=tkinter.Entry(text='',width=60)
q_turn=tkinter.Label(text='Question')
a_turn=tkinter.Label(text='Answer')
a_label=tkinter.Label(text='')
a_button=tkinter.Button(text="Here is next Question!",command=question)



start()
if __name__== "__main__":
    root.mainloop()