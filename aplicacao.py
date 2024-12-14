# # feito com professor aula 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from datetime import datetime
from tkinter import *
import tkinter as tk

def coletador_dados_tempo():

    navegador = webdriver.Edge()

    navegador.get("https://www.google.com")

    navegador.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Temperatura taboão da serra')
    navegador.implicitly_wait(5)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
    navegador.implicitly_wait(5)

    temperatura = navegador.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    umidade = navegador.find_element(By.XPATH, '//*[@id="wob_hm"]').text

    print(f'A temperatura atual de Taboão da Serra é {temperatura}° e a umidade é {umidade}')


    # armazenar no excel

    arquivo = 'ProjetoTempo.xlsx'

    # Abrindo o arquivo existente
    wb = load_workbook(arquivo)
    sheet = wb.active

    # Adicionando os dados na próxima linha
    data_atual = datetime.now().strftime('%d-%m-%Y')
    hora_atual = datetime.now().strftime('%H:%M:%S')

    # Adicionando os dados na próxima linha vazia
    sheet.append([temperatura, umidade, hora_atual, data_atual])

    # Salvando o arquivo
    wb.save(arquivo)

    # Fechar o navegador
    navegador.quit()

    print("Dados armazenados na planilha com sucesso.")


# criando uma gui atraves de gui (unidade 3 - aula 2)

class Aplicacao:
    def __init__(self):
        try:
            self.layout = tk.Tk()
            self.layout.title("Previsão do Tempo de Taboão da Serra")
            self.layout.geometry("300x90")
        
            self.tela = Frame(self.layout)
            self.descricao = Label(self.tela, text= "Atualizar temperatura na planilha:")
            self.salvar = Button(self.tela, text="Buscar previsão", command=coletador_dados_tempo)
            
            self.tela.pack()
            self.descricao.pack()
            self.salvar.pack()


            self.layout.mainloop()

        except Exception as e:
            print(f'Ocorreu um erro: {e}')


executar_app = Aplicacao()

