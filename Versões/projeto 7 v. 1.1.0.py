import tkinter as tk
from tkinter import messagebox

class SistemaInscricaoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inscrição")

        # Formulário para inscrição
        self.label_nome = tk.Label(root, text="Nome:")
        self.input_nome = tk.Entry(root)

        self.label_idade = tk.Label(root, text="Idade:")
        self.input_idade = tk.Entry(root)

        self.label_endereco = tk.Label(root, text="Endereço:")
        self.input_endereco = tk.Entry(root)

        self.label_residencia_sp = tk.Label(root, text="Reside em São Paulo?")
        self.radio_var = tk.StringVar()
        self.radio_var.set("sim")

        self.radio_sim = tk.Radiobutton(root, text="Sim", variable=self.radio_var, value="sim")
        self.radio_nao = tk.Radiobutton(root, text="Não", variable=self.radio_var, value="não")

        self.btn_inscricao = tk.Button(root, text="Inscrever", command=self.inscrever_participante)

        # Layout do formulário
        self.label_nome.grid(row=0, column=0, sticky=tk.W)
        self.input_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_idade.grid(row=1, column=0, sticky=tk.W)
        self.input_idade.grid(row=1, column=1, padx=5, pady=5)

        self.label_endereco.grid(row=2, column=0, sticky=tk.W)
        self.input_endereco.grid(row=2, column=1, padx=5, pady=5)

        self.label_residencia_sp.grid(row=3, column=0, sticky=tk.W)
        self.radio_sim.grid(row=3, column=1, padx=5, pady=5)
        self.radio_nao.grid(row=3, column=2, padx=5, pady=5)

        self.btn_inscricao.grid(row=4, column=1, padx=5, pady=5)

    def inscrever_participante(self):
        nome = self.input_nome.get()
        idade = self.input_idade.get()
        endereco = self.input_endereco.get()
        reside_sp = self.radio_var.get()

        if nome and idade and endereco:
            if idade.isnumeric() and int(idade) >= 18:
                if reside_sp == "sim":
                    messagebox.showinfo("Inscrição", "Inscrição validada!")
                else:
                    messagebox.showwarning("Inscrição", "A participação é restrita a moradores de São Paulo.")
            else:
                messagebox.showwarning("Inscrição","Apenas maiores de idade podem se inscrever.")
        else:
            messagebox.showwarning("Inscrição", "Por favor, preencha todos os campos.")

def main():
    root = tk.Tk()
    app = SistemaInscricaoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
