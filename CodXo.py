import currency as converter
from forex_python.converter import currencyRates
common_currencies=['USD','EUR','GBJ','JPY','CAD','AUD','CHF','NZD']
class currentconverter:
    def __int__(self):
        self.root=converter.CC()
        self.root.title("current converter")
        self.root.geometry("200*180")
        self.from_var=converter.stringvar(self.root)
        self.from_var.set('USD')
        self.from_menu=converter.optionmenu(self.root,self.from_var,"values*common_currencies")
        self.from_menu.pack(pady=1)
        self.from_var=converter.stringvar(self.root)
        self.from_var.set('EUR')
        self.from_menu=converter.optionmenu(self.root,self.from_var,"values*common_currencies")
        self.from_menu.pack(pady=1)
        self.amount_label=converter.label(self.root,text="amount:")
        self.amount_label.pack(pady=1)
        self.amount_entry=converter.entry(self.root)
        self.amount_entry.pack(pady=1)
        self.convert_button=converter.button(self.root,text="convert",command=self.convert_current)
        self.convert_button.pack(pady=1)
        self.result_label=converter.label(self.root,text="")
        self.result_label.pack(pady=1)
        self.root.mainloop()
        def conver_currency(self):
            try:
                from_currency=self.from_var.get()
                to_currency=self.to_var.get()
                amount=float(self.amount_entry.get())
                c_rates=currencyRates()
                rate=c_rates.get_rate(from_currency,to_currency)
                converter_amount=amount*rate
                self.result_label.config(text=f'{amount}{from_currency}={converter_amount:2f}{to_currency}')
            except ValueError:
                self.result_label.config(text="please enter a valid number")
            except Exception:
                self.result_label.config(text="Error occurred")
