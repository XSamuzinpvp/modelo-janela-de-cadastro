import io
import customtkinter as ctk

# Configuração inicial da janela
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Login")
app.geometry("400x500")

# Itens da interface
textLabel = ctk.CTkLabel(app, text="LOGIN", font=("Arial", 30))
textLabel.place(x=158, y=10)

usern = ctk.CTkEntry(app, placeholder_text="username", font=("Arial", 14))
usern.place(x=135, y=125)

userpass = ctk.CTkEntry(app, placeholder_text="password", font=("Arial", 14), show="*")
userpass.place(x=135, y=185)

resultado_label1 = ctk.CTkLabel(app, text=" ", font=("Arial", 8))
resultado_label1.place(x=135, y=155)

resultado_label2 = ctk.CTkLabel(app, text=" ", font=("Arial", 8))
resultado_label2.place(x=135, y=215)

# Função para fechar o aplicativo
def quebrar():
    app.destroy()

# Função para ocultar os elementos
def ocultar():
    textLabel.place_forget()
    usern.place_forget()
    userpass.place_forget()
    resultado_label1.place_forget()
    resultado_label2.place_forget()
    button.place_forget()
    fechar.place_forget()

    # Mensagem de sucesso
    final = ctk.CTkLabel(app, text="Cadastro Efetuado com Sucesso", font=("Arial", 20))
    final.place(x=50, y=100)
    fechar2 = ctk.CTkButton(app, text="Fechar", command=quebrar, width=100, height=40)
    fechar2.place(x=150, y=200)

# Função de login
def login():
    username = usern.get().strip()
    password = userpass.get().strip()
    contagemPASS = len(password)

    # Validações básicas
    if username == "":
        resultado_label1.configure(text="O campo não pode estar vazio.", text_color="red")
        return
    else:
        resultado_label1.configure(text="")

    if password == "" or contagemPASS < 8:
        resultado_label2.configure(text="A senha deve ter no mínimo 8 caracteres.", text_color="red")
        return
    else:
        resultado_label2.configure(text="")

    # Verificar se o username já existe no banco de dados
    try:
        with io.open("bancodedados.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha_username = linha.strip().split(",")[0]  # Obtém o username
                if username == linha_username:
                    resultado_label1.configure(text="Esse nome de usuário já está sendo usado.", text_color="red")
                    return
    except FileNotFoundError:
        # O arquivo será criado caso não exista
        pass

    # Salvar o username e a senha no banco de dados
    try:
        with io.open("bancodedados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{username},{password}\n")
    except Exception as e:
        resultado_label1.configure(text=f"Erro ao salvar: {e}", text_color="red")
        return

    # Ocultar a interface e mostrar a mensagem de sucesso
    ocultar()

# Botões
button = ctk.CTkButton(app, text="Entrar", font=("Arial", 14), command=login)
button.place(x=135, y=245)

fechar = ctk.CTkButton(app, text="X", command=quebrar, height=5, width=5)
fechar.place(x=10, y=10)

app.mainloop()
