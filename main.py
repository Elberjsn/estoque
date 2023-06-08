import base64
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
from modal import *


class main:

    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Inicio')
        self.root.geometry('500x250')
        
        self.ultimo_opc = None
        self.frm_entrada = Frame(self.root)
        self.frm_prod = Frame(self.root)
        self.frm_consulta = Frame(self.root)
        self.frm_saida = Frame(self.root)
        self.frm_relatorio = Frame(self.root)
        self.imagens_envio = None
        self.codigos = []
        self.nfs = []
        self.sku = []
        self.nome_produtos = []
        self.fornecedor = []
        self.qtd = []
        self.imagens = []

        self.lista_produtos = busca_prod()
        self.menu()

    def tabela_produtos(self):
        for lista in self.lista_produtos:
            self.codigos.append(lista[0])
            self.nfs.append(lista[1])
            self.sku.append(lista[2])
            self.nome_produtos.append(lista[3])
            self.fornecedor.append(lista[4])
            self.qtd.append(lista[5])
            self.imagens.append(lista[10])

    def telas(self, opc):

        if self.ultimo_opc:
            self.ultimo_opc.forget()
                
        if opc == '1':
            self.ultimo_opc = self.frm_entrada
            return self.entrada()
        elif opc == '2':
            self.ultimo_opc = self.frm_prod
            return self.cad_prod()
        elif opc == '3':
            self.ultimo_opc = self.frm_consulta
            return self.cons_prod()
        elif opc == '4':
            self.ultimo_opc = self.frm_saida
            return self.saida_produto()
        elif opc == '5':
            self.ultimo_opc = self.frm_relatorio
            return self.relatorio()
        else:
            self.ultimo_opc = None

    def menu(self):
        self.btn_menu= Menu(self.root)
        self.root.config(menu = self.btn_menu)
        
        submenu = Menu(self.btn_menu)
        submenu.add_command(label='Recebimento', command=lambda:self.telas('1'))
        submenu.add_command(label='Cadastrar Produtos', command=lambda:self.telas('2'))
        submenu.add_command(label='Consultar Produtos', command=lambda:self.telas('3'))
        submenu.add_command(label='Saida', command=lambda:self.telas('4'))
        submenu.add_command(label='Relatorios', command=lambda:self.telas('5'))
        submenu.add_separator()
        submenu.add_command(label="Sair", command=self.root.destroy)
        
        self.btn_menu.add_cascade(label='Opçoes', menu=submenu, underline=0)


    def adicionar_img(self):

        dirname = tkinter.filedialog.askopenfilename()
        if dirname:
            imagem_selecionada = Image.open(dirname)
            img = imagem_selecionada.resize((125,150))
            img = ImageTk.PhotoImage(img)
            #dupla adição de imagem verificação
            self.painel['image'] = img
            self.painel.image = img

            with open(dirname, 'rb') as encode_imgs:
                encode_img = base64.b64encode(encode_imgs.read())
                print(encode_img)
                self.imagens_envio =  encode_img

    def entrada(self):
        self.frm_entrada.pack()
        lista_cbx=[]
        for lista in self.lista_produtos:
            lista_cbx.append(f'{lista[2]} - {lista[3]}')

        cbx = StringVar()
        Label(self.frm_entrada, text='Codigo Produto: ', font=('Arial','12')).grid(column=0, row=0, padx=5)
        cbx_codigo = ttk.Combobox(self.frm_entrada, textvariable=cbx)
        cbx_codigo['values'] = lista_cbx
        cbx_codigo['state'] = 'readonly'
        cbx_codigo.grid(row=0, column=1)
        cbx_codigo.current()

        Label(self.frm_entrada, text='Nota Fiscal: ', font=('Arial','12')).grid(column=0, row=1, padx=5)
        txt_nfe= Entry(self.frm_entrada, width=15)
        txt_nfe.focus()
        txt_nfe.grid(row=1, column=1)

        Label(self.frm_entrada, text='Fornecedor: ', font=('Arial','12')).grid(column=0, row=2, padx=5)
        txt_fornecedor= Entry(self.frm_entrada, width=15)
        txt_fornecedor.grid(row=2, column=1)

        Label(self.frm_entrada, text='Quantidade: ', font=('Arial','12')).grid(column=0, row=3, padx=5)
        txt_qtd= Entry(self.frm_entrada, width=15)
        txt_qtd.grid(row=3, column=1)

        btn_nova = Button(self.frm_entrada, text='Receber', command=lambda: recebimento())
        btn_nova.grid(row=4, column=1)


        def recebimento():
            lista = [lista_cbx.get(),txt_nfe.get(),txt_fornecedor.get(), txt_qtd.get()]
            add_entrada(lista)

    def cad_prod(self):
        self.frm_prod.pack()
        self.root.geometry('700x250')

        Label(self.frm_prod, text='Codigo: ', font=('Arial','12')).grid(row=0, column=0)

        txt_codigo= Entry(self.frm_prod, width=15)
        txt_codigo.grid(row=0, column=2)

        Label(self.frm_prod, text='Nota Fiscal: ', font=('Arial','12')).grid(row=1,column=0)
        txt_nfe= Entry(self.frm_prod, width=15)
        txt_nfe.grid(row=1, column=2)
        
        Label(self.frm_prod, text='Fornecedor: ', font=('Arial','12')).grid(row=2, column=0)
        txt_fornecedor= Entry(self.frm_prod, width=15)
        txt_fornecedor.grid(row=2, column=2)
        
        Label(self.frm_prod, text='Produto: ', font=('Arial','12')).grid(row=3, column=0)
        txt_produto= Entry(self.frm_prod, width=15)
        txt_produto.grid(row=3, column=2)
        
        Label(self.frm_prod, text='Quantidade: ', font=('Arial','12')).grid(row=4, column=0)
        txt_qtd= Entry(self.frm_prod, width=15)
        txt_qtd.grid(row=4, column=2)
        
        Label(self.frm_prod, text='Cubagem (cm)', font=('Arial','12')).grid(row=5, column=0)
        txt_codigo= Entry(self.frm_prod, width=15, state= DISABLED)
        txt_codigo.grid(row=5, column=2)
        
        Label(self.frm_prod, text='Largura: ', font=('Arial','12')).grid(row=6, column=0)
        txt_l= Entry(self.frm_prod, width=15)
        txt_l.grid(row=6, column=2)
        
        Label(self.frm_prod, text='Altura: ', font=('Arial','12')).grid(row=7, column=0)
        txt_a= Entry(self.frm_prod, width=15)
        txt_a.grid(row=7, column=2)
        
        Label(self.frm_prod, text='Profundidade: ', font=('Arial','12')).grid(row=8, column=0)
        txt_p= Entry(self.frm_prod, width=15)
        txt_p.grid(row=8, column=2) 

        btn_nova = Button(self.frm_prod, text='Adicionar Produto')
        btn_nova.grid(row=9, column=1)

        self.painel = Label(self.frm_prod, text="Imagem do Produto")
        self.painel.grid(row=0, column=4, columnspan=4, rowspan=9)

        btn_image = Button(self.frm_prod, text='Adicionar Imagem', command=self.adicionar_img)
        btn_image.grid(row=9, column=0)
        
        def cadastrar():
            cubagem = txt_a*txt_p*txt_l
            lista=[txt_nfe.get(),txt_fornecedor.get(),txt_produto.get(),txt_qtd.get(),cubagem]
            cadastrar_novo(lista)
        
        def busca_cod():


    def cons_prod(self):
        self.frm_consulta.pack()
        self.root.geometry('500x250')

        list_test= ['elber','jose','silva','nascimento']
        
        n = StringVar()
        Label(self.frm_consulta, text='Codigo Produto: ', font=('Arial','12')).grid(column=0, row=0, padx=5)
        cbx_codigo = ttk.Combobox(self.frm_consulta, textvariable=n)
        cbx_codigo['values'] = list_test
        cbx_codigo.grid(row=0, column=1)
        cbx_codigo.current()

        Label(self.frm_consulta, text='Produto: ', font=('Arial','12')).grid(row=1, column=0)
        txt_prod = Entry(self.frm_consulta, width=15)
        txt_prod.grid(row=1, column=1)

        Label(self.frm_consulta, text='Quantidade: ', font=('Arial','12')).grid(row=2, column=0)
        txt_qtd = Entry(self.frm_consulta, width=15)
        txt_qtd.grid(row=2, column=1)

        Label(self.frm_consulta, text='Posição: ', font=('Arial','12')).grid(row=3, column=0)
        txt_posi = Entry(self.frm_consulta, width=15)
        txt_posi.grid(row=3, column=1)

        Label(self.frm_consulta, text='Estoque: ', font=('Arial','12')).grid(row=4, column=0)
        txt_estoque = Entry(self.frm_consulta, width=15)
        txt_estoque.grid(row=4, column=1)       

    def saida_produto(self):
        self.frm_saida.pack()
        self.root.geometry('500x150')

        Label(self.frm_saida, text="Saida: ", font=('Arial', '12')).grid(row=0, column=0)
        Label(self.frm_saida, text="-----", font=('Arial', '12')).grid(row=0, column=1)
        
        Label(self.frm_saida, text="Codigo: ", font=('Arial', '12')).grid(row=2, column=0)
        txt_cod = Entry(self.frm_saida, width=20)
        txt_cod.grid(row=2, column=1)

        Label(self.frm_saida, text="Produto: ", font=('Arial', '12')).grid(row=3, column=0)
        Label(self.frm_saida, text="-----", font=('Arial', '12')).grid(row=3, column=1)
        
        Label(self.frm_saida, text="Quantidade: ", font=('Arial', '12')).grid(row=4, column=0)
        Label(self.frm_saida, text="-----", font=('Arial', '12')).grid(row=4, column=1)
        
        self.painel = Label(self.frm_saida, text="Imagem do Produto")
        self.painel.grid(row=0, column=4, columnspan=4, rowspan=3, pady=15, padx=15)

        btn_sucesso = Button(self.frm_saida, text='Nova Saida')
        btn_sucesso.grid(row=5, column=1)

    def relatorio(self):
        self.frm_relatorio.pack()
        scrollbar = Scrollbar(self.frm_relatorio)

        Label(self.frm_relatorio, text='Relatorio').grid(row=0, column=2)

        lista_table= ttk.Treeview(self.frm_relatorio, yscrollcommand=scrollbar.set)
        lista_table['columns'] = ('NF','Produtos','Qtd','Data','Hora')

        lista_table .column("#0", width=0, stretch=NO)
        lista_table .column("NF", width=80, anchor=CENTER)
        lista_table .column("Produtos", width=80, anchor=CENTER)
        lista_table .column("Qtd", width=80, anchor=CENTER)
        lista_table .column("Data", width=80, anchor=CENTER)
        lista_table .column("Hora", width=80, anchor=CENTER)
        
        lista_table.heading('#0', text="")
        lista_table.heading('NF', text="Nota", anchor=CENTER)
        lista_table.heading('Produtos', text="Produtos", anchor=CENTER)
        lista_table.heading('Qtd', text="Quantidade", anchor=CENTER)
        lista_table.heading('Data', text="Data", anchor=CENTER)
        lista_table.heading('Hora', text="Hora", anchor=CENTER)

        lista_table.insert(parent='',index='end',iid=0,text='',
        values=('1','Ninja','101','Okla', 'Moore'))

        lista_table.grid(row=2, rowspan=5, column=2, columnspan=10)
        scrollbar.grid(row=2, rowspan=5, column=12)
        scrollbar.config(command=lista_table.yview)

root = Tk()
main(root)
root.mainloop()