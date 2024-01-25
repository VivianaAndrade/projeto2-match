import tkinter as tk
from tkinter import messagebox
import csv
import os

class SistemaInscricaoEvento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inscrição para Evento")
        self.root.geometry("400x300")

    # condicionando o código de atribuição 
        
        self.visualizar_button = tk.Button(root, text="Visualizar Cadastro", command=self.visualizar_cadastro)
        self.visualizar_button.pack()

    # aplicando os métodos 

    def visualizar_cadastro(self):
        # Create an instance of VisualizarCadastro
        visualizar_cadastro_window = VisualizarCadastro(self.root)

class VisualizarCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizar Cadastro")
        self.root.geometry("400x300")

        self.lista_participantes = tk.Listbox(root)
        self.lista_participantes.pack()

        self.carregar_participantes()

    def carregar_participantes(self):
        arquivo_csv = "participantes.csv"

        if not os.path.exists(arquivo_csv):
            messagebox.showinfo("Sem Cadastros", "Não há cadastros para visualizar.")
            return

        with open(arquivo_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                self.lista_participantes.insert(tk.END, f"Nome: {row[0]}, Idade: {row[1]}, Endereço: {row[2]}, SP: {row[3]}, Noturno: {row[4]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaInscricaoEvento(root)
    root.mainloop()
