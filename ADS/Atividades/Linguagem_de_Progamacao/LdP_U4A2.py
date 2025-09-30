# instalacoes nescessarias
pip install kivymd

# importacoes
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

# Definicao da string KV que contem a descricao da interface
KV = '''
<CalculatorApp>:
    orientation: 'vertical'
    MDTextField:
        id: input_field
        hint_text: "Insira um numero:"
        helper_text_mode: "on_focus"
        input_filter: "float"
    GridLayout:
        cols: 4
        spacing: dp(10)
        MDRaisedButton:
            Text: '1'
            on_press: app.on_number_press(1)
        MDRaisedButton:
            Text: '2'
            on_press: app.on_number_press(2)
        MDRaisedButton:
            Text: '3'
            on_press: app.on_number_press(3)
        MDRaisedButton:
            Text: '+'
            on_press: app.on_operator_press("+")
        MDRaisedButton:
            Text: '4'
            on_press: app.on_number_press(4)
        MDRaisedButton:
            Text: '5'
            on_press: app.on_number_press(5)
        MDRaisedButton:
            Text: '6'
            on_press: app.on_number_press(6)
        MDRaisedButton:
            Text: '-'
            on_press: app.on_operator_press("-")
        MDRaisedButton:
            Text: '7'
            on_press: app.on_number_press(7)
        MDRaisedButton:
            Text: '8'
            on_press: app.on_number_press(8)
        MDRaisedButton:
            Text: '9'
            on_press: app.on_number_press(9)
        MDRaisedButton:
            Text: '*'
            on_press: app.on_operator_press("*")
        MDRaisedButton:
            Text: 'C'
            on_press: app.clear_input()
        MDRaisedButton:
            Text: '0'
            on_press: app.on_number_press(0)
        MDRaisedButton:
            Text: '='
            on_press: app.calculate_result()
        MDRaisedButton:
            Text: '/'
            on_press: app.on_operator_press("/")

'''

# Definindo a classe CalculatorApp que herda BoxLayout
class CalculatorApp(BoxLayout):
    # metodo para numero pressionado
    def on_number_press(self, n):
        current_text = self.ids.input_field.text
        new_text = f"{current_text}{n}"
        self.ids.input_field.text = new_text
        
    # metodo para operador chamado
    def on_operator_press(self, op):
        current_text = self.ids.input_field.text 
        new_text = f"{current_text} {op}"
        self.ids.input_field.text = new_text 
        
    # metodo para limpar entrada
    def clear_input(self):
        self.ids.input_field.text = ""
        
    # metodo para calcular resultado da expressao
    def calculate_result(self):
        try:
            result = eval(self.ids.input_field.text)
            self.ids.input_field.text = str(result)
        except Exception as e:
            self.ids.input_field.text = "Erro"
            
# Definindo classe CalculatorMDApp que herda de MDApp 
class CalculatorMDApp(MDApp):
    # metodo chamado para construir o App
    def build(self):
        return CalculatorApp()
        
    # metodos para interagir com a instancia de CalculatorApp
    def on_number_press(self, n):
        self.root.on_number_press(n)
        
    def on_operator_press(self, op):
        self.root.on_operator_press(op)
        
    def clear_input(self):
        self.root.clear_input()
        
    def calculate_result(self):
        self.root.calculate_result()
        
# verificando se o script esta sendo executado diretamente
if __name__ == '__main__':
    # carregando a string KV usando builder
    Builder.load_string(KV)
    
    # iniciando app MD
    CalculatorMDApp().run()