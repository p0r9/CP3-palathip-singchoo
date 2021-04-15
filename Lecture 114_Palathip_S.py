from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

def leftclick_convented (event) :
    rate_money = CurrencyRates()
    input_money = int(input_entry.get())
    user_currency = rate_money.convert(currency_choosen.get(),currency_converted_choosen.get(),input_money)
    resalt_label.configure(text = user_currency)


def leftclick_clear (event) :
    currency_choosen.set('')
    currency_converted_choosen.set('')
    resalt_label.configure(text = '0')
    input_entry.delete(0,END)

# Creating tkinter window
window = Tk()
window.title('Currency converter')
window.geometry('600x300')

# label text for title
ttk.Label(window, text = "Currency converter", background = 'green', foreground ="white", font = ("arial", 17)).grid(row = 0, column = 1)
  
ttk.Label(window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    

ttk.Label(window, text = "Select the Currency : ",font = ("arial", 11)).grid(column = 0,row = 5)

# Combobox creation
n = StringVar()
# Adding combobox drop down list
currency_choosen = ttk.Combobox(window, width = 27, textvariable = n)

currency_choosen ['values'] = ('THB','GBP', 'HKD','IDR','ILS','DKK','INR','CHF','MXN','CZK','SGD',
                                     'HRK','EUR','MYR','NOK','CNY','BGN','PHP','PLN','ZAR','CAD','ISK',
                                     'BRL','RON','NZD','JPY','RON','KRW','USD','AUD','HUF','SEK')
  
currency_choosen.grid(column = 1, row = 5)
currency_choosen.current()

ttk.Label(window, text = " to ",font = ("arial", 11)).grid(column = 2,row = 5 )

n = StringVar()
currency_converted_choosen = ttk.Combobox(window, width = 27, textvariable = n)
  
currency_converted_choosen['values'] = ('THB','GBP', 'HKD','IDR','ILS','DKK','INR','CHF','MXN','CZK','SGD',
                                      'HRK','EUR','MYR','NOK','CNY','BGN','PHP','PLN','ZAR','CAD','ISK',
                                     'BRL','RON','NZD','JPY','RON','KRW','USD','AUD','HUF','SEK')
  
currency_converted_choosen.grid(column = 3, row = 5)
currency_converted_choosen.current()

ttk.Label(window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 )    

input_label = ttk.Label(window, text = " Input Your Money : ",font = ("arial", 11))
input_label.grid(column = 0,row = 7 )

input_entry = ttk.Entry (window,width='30')
input_entry.grid(column = 1,row = 7 )

to_label  = ttk.Label(window, text = " to ",font = ("arial", 11))
to_label.grid(column = 2,row = 7 )

resalt_label = ttk.Label(window, text = " 0 ",font = ("arial", 11))
resalt_label.grid(column = 3,row = 7 )

ttk.Label(window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )    

enter_button = Button(window, text = " Enter ",font = ("arial", 11),
              background = 'red',foreground ="white")

enter_button.grid(column = 0,row = 9 )
enter_button.bind ('<Button-1>',leftclick_convented)

clear_button = Button(window, text = " Clear ",font = ("arial", 11))
clear_button.grid(column = 1,row = 9 )
clear_button.bind('<Button-1>',leftclick_clear)

window.mainloop()