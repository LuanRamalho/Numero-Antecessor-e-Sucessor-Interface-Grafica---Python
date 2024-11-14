# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num = int(entry_numero.get())
        antecessor = num - 1
        sucessor = num + 1

        resultado = (
            f"Número antecessor: {antecessor}\n"
            f"Número digitado: {num}\n"
            f"Número sucessor: {sucessor}"
        )
        
        messagebox.showinfo("Resultados", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número inteiro válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Antecessor e Sucessor")
root.geometry("400x300")
root.configure(bg="#4CAF50")  # Cor de fundo verde

# Título
titulo = tk.Label(root, text="Calculadora de Antecessor e Sucessor", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white")
titulo.pack(pady=20)

# Entrada de número
frame = tk.Frame(root, bg="#4CAF50")
frame.pack(pady=10)

label_numero = tk.Label(frame, text="Digite um número inteiro:", font=("Arial", 12), bg="#4CAF50", fg="white")
label_numero.pack(side=tk.LEFT)

entry_numero = tk.Entry(frame, font=("Arial", 12), width=10)
entry_numero.pack(side=tk.LEFT)

# Botão para calcular
botao_calcular = tk.Button(root, text="Calcular", command=calcular, font=("Arial", 12, "bold"), bg="#FF9800", fg="white")
botao_calcular.pack(pady=20)

# Executar o loop principal
root.mainloop()
