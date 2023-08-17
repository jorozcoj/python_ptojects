import matplotlib.pyplot as plt
import numpy as np

def generate_bar_char(labels, values):
    fig, ax = plt.subplots() #fig es la figura, ax son las coordenadas 
    ax.bar(labels, values)
    plt.show()  

def generate_pie_char(labels, values):
    fig, ax = plt.subplots() #fig es la figura, ax son las coordenadas 
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show() 

if __name__ == '__main__':    
    labels = ['value_a' ,'value_b' ,'value_c']
    values = [20 , 30, 15]
    #generate_bar_char(labels, values)
    generate_pie_char()