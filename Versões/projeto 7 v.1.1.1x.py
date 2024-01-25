import tkinter as tk
from tkinter import messagebox

# 1. Importação das bibliotecas tkinter e messagebox:
#  - 'import tkinter as tk': Importa a biblioteca tkinter e a renomeia como `tk`.
# - 'from tkinter import messagebox': Importa apenas o módulo `messagebox` da biblioteca tkinter.

class SistemaInscricaoGUI:
    
# 2. Classe 'SistemaInscricaoGUI':
# - Define uma classe chamada 'SistemaInscricaoGUI'' para a interface gráfica do sistema de inscrição.
  
    def __init__(self):
        
    # 3. Método `__init__(self)`:	# 3. Método '__init__(self)':
      # - É o construtor da classe 'SistemaInscricaoGUI'.
      
        self.janela = tk.Tk()
        
        # - Cria uma nova janela usando a classe 'Tk'' do módulo 'tkinter'.
        
        self.janela.title("Sistema de Inscrição")
        
        # - Define o título da janela como "Sistema de Inscrição".
        
        self.criar_formulario()
        
       # - Chama o método 'criar_formulario()' para criar o formulário na janela.
  
    def criar_formulario(self):
    	
# 4. Método 'criar_formulario(self)':
        
        self.label_nome = tk.Label(self.janela, text="Nome:")
        
# - Cria os elementos do formulário na janela.
# - Cria e posiciona as etiquetas de texto para "Nome:".

        self.label_nome.grid(row=0, column=0)
        
        # atribui uma etiqueta do formulário nome da grade cujos valores para linha=0, coluna=0.
        
        self.entry_nome = tk.Entry(self.janela)
        
        #atribui uma etiqueta de entrada nome que recebe da biblioteca renomeada de Entrada tk cujos valores estão em self.janela.
        
        self.entry_nome.grid(row=0, column=1)
        
        #atribui da entrada nome da grade cujos valores para linha=0, coluna=1.
        
        self.label_idade = tk.Label(self.janela, text="Idade:")
        
        # - Cria e posiciona as etiquetas de texto para "Idade:".
        
        self.label_idade.grid(row=1, column=0)
        
        #atribui uma etiqueta idade de grade linha=1, coluna=0.
        
        self.entry_idade = tk.Entry(self.janela)
        
        #atribui entrada idade que recebe tk de entrada self.janela
        
        self.entry_idade.grid(row=1, column=1)

		#atribui de entrada idade de grade linha=1, coluna=1.
		
        self.label_reside_sp = tk.Label(self.janela, text="Reside em São Paulo?")
        
        # - Cria e posiciona as etiquetas de texto para "Reside em São Paulo?".
        
        self.label_reside_sp.grid(row=2, column=0)
        
        #atribui de etiqueta reside sp de grade linha=2, coluna=0.
        
        self.entry_reside_sp = tk.Entry(self.janela)
        
        #atribui de entrada reside sp recebe tk de entrada self.janela
        
        self.entry_reside_sp.grid(row=2, column=1)
	
		#atribui entrada reside sp de grade linha=2, coluna=1.
		
        self.botao_inscricao = tk.Button(self.janela, text="Inscrever", command=self.inscrever_participante)
        
        # - Cria e posiciona o botão "Inscrever" que chama o método `inscrever_participante()` quando clicado.
        
        self.botao_inscricao.grid(row=3, column=0, columnspan=2)
        
		#atribui botao inscricao de grade linha=3, coluna=0, colun

    def inscrever_participante(self):
        
    # 5. Método 'inscrever_participante(self)':
        
        if self.campos_validos():
            
     # - Verifica se os campos do formulário estão preenchidos corretamente chamando o método 'campos_validos()'.
      #  - Se os campos estiverem corretos, obtém os valores dos campos de nome, idade e residência em São Paulo.
      
            nome = self.entry_nome.get()
            idade = int(self.entry_idade.get())
            reside_sp = self.entry_reside_sp.get()
            
#  - Cria e posiciona as caixas de entrada de texto para o nome, idade e se reside em São Paulo.
  
            if self.idade_valida(idade):
                
           # - Verifica se a idade é válida chamando o método 'idade_valida()'.
           
                if reside_sp.lower() == "sim":
                    
             # - Se a idade for válida, verifica se o participante reside em São Paulo.
             
                    messagebox.showinfo("Sucesso", f"Inscrição para {nome} foi realizado com sucesso!")
                    
                # - Se residir em São Paulo, exibe uma mensagem de sucesso usando o `messagebox.showinfo()`.
                
                else:
                    messagebox.showwarning("Aviso", "A inscrição é válida apenas para residentes de São Paulo!")
                    
                  # - Se não residir em São Paulo, exibe um aviso usando o 'messagebox.showwarning()'.
           
            else:
               	  messagebox.showwarning("Erro", "Idade inválida!")
                
            # - Se a idade não for válida, exibe um erro usando o 'messagebox.showwarning()'.
          
        else:
           				 messagebox.showwarning("Erro", "Preencha todos os campos corretamente!")
            
          # - Se os campos não estiverem preenchidos corretamente, exibe um erro usando o 'messagebox.showwarning()'.

    def campos_validos(self):
        
   # 6. Método 'campos_validos(self)':
        
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        reside_sp = self.entry_reside_sp.get()

       # - Obtém os valores dos campos de nome, idade e residência em São Paulo.
       
        if nome and idade and reside_sp:
            return True
        else:
            return False

        # - Verifica se todos os campos estão preenchidos.
        # - Retorna 'True'' se todos os campos estiverem preenchidos e 'False'' caso contrário.
        
    def idade_valida(self, idade):
        
  # 7. Método 'idade_valida(self, idade)':
        
        if idade >= 18:
            return True
        else:
            return False

       # - Verifica se a idade recebida como argumento é maior ou igual a 18.
       # - Retorna `True` se a idade for válida e `False` caso contrário.
       
    def main(self):
        
   # 8. Método 'main(self)':
        
        self.janela.mainloop()

        # - Inicia o loop principal da janela, permitindo a interação com a interface gráfica.
        
sistema_inscricao = SistemaInscricaoGUI()
sistema_inscricao.main()

# 9. Criação de uma instância da classe 'SistemaInscricaoGUI'' e chamada do método 'main()' para iniciar o programa.

				# Fim das instruções