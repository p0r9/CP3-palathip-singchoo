from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

def convented (event) :
    user_money = CurrencyRates()
    output_money = user_money.get_rate(currency_choosen.get(),currency_converted_choosen.get())
    print (output_money)

# Creating tkinter window
window = Tk()
window.title('Convert money')
window.geometry('600x250')
  
# label text for title
ttk.Label(window, text = "Convert money", background = 'green', foreground ="white", font = ("arial", 17)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Select the Currency : ",font = ("arial", 11)).grid(column = 0,row = 5, padx = 5, pady = 20)
  
# Combobox creation
n = StringVar()
# Adding combobox drop down list
currency_choosen = ttk.Combobox(window, width = 27, textvariable = n)

currency_choosen ['values'] = (' GBP', ' HKD',' IDR',' ILS',' DKK',' INR',' CHF',' MXN',' CZK',' SGD',' THB',' HRK',
                            ' EUR',' MYR',' NOK',' CNY',' BGN',' PHP',' PLN',' ZAR',' CAD',' ISK',' BRL',' RON',
                            ' NZD',' JPY',' RON',' KRW',' USD',' AUD',' HUF',' SEK',)
  
currency_choosen.grid(column = 1, row = 5)
currency_choosen.current()

ttk.Label(window, text = " to ",font = ("arial", 11)).grid(column = 2,row = 5 )

n = StringVar()
currency_converted_choosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
currency_converted_choosen['values'] = (' GBP', ' HKD',' IDR',' ILS',' DKK',' INR',' CHF',' MXN',' CZK',' SGD',' THB',
                                     ' HRK',' EUR',' MYR',' NOK',' CNY',' BGN',' PHP',' PLN',' ZAR',' CAD',' ISK',
                                     ' BRL',' RON',' NZD',' JPY',' RON',' KRW',' USD',' AUD',' HUF',' SEK','All')
  
currency_converted_choosen.grid(column = 3, row = 5)
currency_converted_choosen.current()

input_label = ttk.Label(window, text = " Input Your Money : ",font = ("arial", 11)).grid(column = 0,row = 6 )

input_entry = ttk.Entry (window,width='30').grid(column = 1,row = 6 )

to_label  = ttk.Label(window, text = " to ",font = ("arial", 11)).grid(column = 2,row = 6 )

resalt_label = ttk.Label(window, text = " 0 ",font = ("arial", 11)).grid(column = 3,row = 6 )

ttk.Label(window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 7 )    

enter_button = Button(window, text = " Enter ",font = ("arial", 11),
              background = 'red',foreground ="white")
enter_button.grid(column = 0,row = 8 )
enter_button.bind ('<Button-1>',convented)

clear_button = Button(window, text = " Clear ",font = ("arial", 11)).grid(column = 1,row = 8 )

window.mainloop()'''

