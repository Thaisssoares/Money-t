from moneyAdvicer import pegarcotacoes
import PySimpleGUI as psg
psg.theme('Dark Blue ')
psg.popup('Deseja continuar,aperte OK')
layout = [
    [psg.Text("Pegar Cotação de Moeda:",)],
    [psg.InputText(key="nomeCotacao")],
    [psg.Button("Pegar Cotação"), psg.Button("Cancelar")],
    [psg.Text("", key="texto_cotacao")],
]
janela = psg.Window("Cotação da Moeda", layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED or evento == 'Cancelar':
        break
    else:
        cod_cotacao = valores["nomeCotacao"]
        cotacao = pegarcotacoes(cod_cotacao)
        janela["texto_cotacao"].update(f"A cotação do {cod_cotacao} é R$ {cotacao} ")

janela.close()