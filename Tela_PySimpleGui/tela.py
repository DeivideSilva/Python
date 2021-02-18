import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Topanga') # muda o layout da aplicação
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(20,0),key='idade')],
            [sg.Text('Provedores de e-mail disponiveis')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]

        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)
        

    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceitaCartao = self.values['naoAceitaCartao']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'gmail: {aceita_gmail}')
            print(f'outlook: {aceita_outlook}')
            print(f'yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceitaCartao}')

tela = TelaPython()
tela.Iniciar()