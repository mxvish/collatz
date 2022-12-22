from matplotlib import pyplot as plt
import tkinter as tk      
from functools import partial

def call_result(label_result, arg):
    try:
        number = int(arg.get())
        if number <= 1:
            label_result.config(text="0より大きい整数を入力してください") 
        else:
            startNum = number
            yaxis = []
            
            while number != 1:
                yaxis.append(number)
            
                if number % 2 == 0:
                    number /= 2
                else:
                    number = number * 3 + 1
            
            yaxis.append(number)
            print("解析終了!")            
            print(yaxis)
            
            plt.plot(yaxis)
            plt.title(str(startNum) + "から始まるコラッツ数列", fontname="MS Gothic")  
            plt.show()
            return

    except ValueError:
        label_result.config(text="整数を入力してください") 

root = tk.Tk()                                                                  
root.geometry('480x270+100+100')  
root.title('pythonコラッツ配列シミュレーター')  
   
inputStr = tk.StringVar()  
  
labelNum = tk.Label(root, text="数字を入力").grid(row=1, column=0)  
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)  

entry = tk.Entry(root, textvariable=inputStr).grid(row=1, column=1)  
  
call_result = partial(call_result, labelResult, inputStr)  
buttonPlot = tk.Button(root, text="プロット", command=call_result).grid(row=3, column=1)
  
root.mainloop()  
