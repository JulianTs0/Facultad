from funciones import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os.path


class Main(Tk):
    def __init__(self, title, size):

        #setup

        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.resizable(False, False)
        self.configure(bg="#0F110F")

        #struct

        self.menu = Menu(self)

        #loop

        self.mainloop()

class Extra(Toplevel):
    def __init__(self, title, size, opt):

        #setup

        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.attributes('-topmost', 1)
        self.configure(bg="#0F110F")

        #var

        self.color_letra = "#00A00C"
        self.color_fondo = "#272423"
        self.color_boton_c = "#44A000"
        self.color_boton_s = "#D80000"
        self.color_letra_s = "white"  
        self.archivo_binario = "archivo_binario.dat"

        #struct

        if opt == 2:
            self.status = Form(self)
        elif opt == 3 or opt == 6 or opt == 7 or opt == 8:
            self.status = Display(self, opt)
        elif opt == 4 or opt == 5:
            self.status = Search(self, opt)

        #loop

        self.mainloop()

class Menu(Frame):
    def __init__(self,parent):

        #setup

        super().__init__(parent)
        self.configure(bg="#0F110F", padx=10, pady=10)
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.97, relheight=0.98)

        #var

        self.existe = os.path.exists("archivo_binario.dat")
        self.color_letra = "#00A00C"
        self.color_fondo = "#272423"
        self.color_boton_c = "#44A000"
        self.color_boton_s = "#D80000"
        self.color_letra_s = "white"
        self.archivo_csv = "peajes-tp4.csv"

        #struct

        self.create_widgets()
    
    def create_widgets(self):

        #create

        main_title = Label(self, text="Menu Principal", font=("TkMenuFont",18), bg=self.color_fondo, fg=self.color_letra)
        op1 = Label(self, text="Crear archivo binario con datos de ticket", font=("Calibri",11),  bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w")
        op2 = Label(self, text="Cargar manualmente datos de ticket", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w")
        op3 = Label(self, text="Mostrar todos los datos del archivo binario", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w")
        op4 = Label(self, text="Buscar tickets por patente en el archivo binario", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w")
        op5 = Label(self, text="Buscar tickets por código en el archivo binario", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w")
        op6 = Label(self, text="Determinar y mostrar la combinacion de la cantidad de vehículos por tipo de vehículo y país de cabina", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w", wraplength=300, justify="left")
        op7 = Label(self, text="Mostrar la cantidad de vehiculos por tipo y por cabina", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w", wraplength=300, justify="left")
        op8 = Label(self, text="Calcular y mostrar la distancia promedio de los tickets del archivo binario", font=("Calibri",11), bg=self.color_fondo, fg=self.color_letra, width=37, anchor="w", wraplength=300, justify="left")
        bt1 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.op1_messages())
        bt2 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(2,op2["text"]))
        bt3 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(3,op3["text"]))
        bt4 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(4,op4["text"]))
        bt5 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(5,op5["text"]))
        bt6 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(6,op6["text"]))
        bt7 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(7,op7["text"]))
        bt8 = Button(self, text="Seleccionar", bg=self.color_boton_c, width=10, height=1, command= lambda: self.verif_existe(8,op8["text"]))
        bt_exit = Button(self, text="Salir", bg=self.color_boton_s , fg=self.color_letra_s, width=6, height=1, command= self.quit)
        
        #configure

        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        #tile

        main_title.grid(column=0, row=0, columnspan=3, sticky="nswe")
 
        #lable

        op1.grid(column=0, row=1, sticky="w", pady=5, padx=5)
        op2.grid(column=0, row=2, sticky="w", pady=5, padx=5)
        op3.grid(column=0, row=3, sticky="w", pady=5, padx=5)
        op4.grid(column=0, row=4, sticky="w", pady=5, padx=5)
        op5.grid(column=0, row=5, sticky="w", pady=5, padx=5)
        op6.grid(column=0, row=6, sticky="w", pady=5, padx=5)
        op7.grid(column=0, row=7, sticky="w", pady=5, padx=5)
        op8.grid(column=0, row=8, sticky="w", pady=5, padx=5)

        #button

        bt1.grid(column=1, row=1, sticky="w", padx=20)
        bt2.grid(column=1, row=2, sticky="w", padx=20)
        bt3.grid(column=1, row=3, sticky="w", padx=20)
        bt4.grid(column=1, row=4, sticky="w", padx=20)
        bt5.grid(column=1, row=5, sticky="w", padx=20)
        bt6.grid(column=1, row=6, sticky="w", padx=20)
        bt7.grid(column=1, row=7, sticky="w", padx=20)
        bt8.grid(column=1, row=8, sticky="w", padx=20)
        bt_exit.grid(column=2, row=9, sticky="e", padx=20)
    
    def op1_messages(self):
        if os.path.exists(self.archivo_csv) == True:
            if self.existe == True:
                op = messagebox.askyesno("Crear archivo binario con datos de ticket","Estas apunto de crear un archivo nuevo, quieres eliminar el anterior?")
                if op == True:
                    crear_archivo(self.archivo_csv)
            else:
                crear_archivo(self.archivo_csv)
        else:
            messagebox.showerror("Error","El archivo .csv no existe o no posee el nombre 'peajes-tp4' verifique en tal caso")
        self.existe = os.path.exists("archivo_binario.dat")
    
    def verif_existe(self,op,title):
        if self.existe:
            if op == 2:
                Extra(title, [400,500,800,50], op)
            elif op == 3:
                Extra(title, [700,600,400,50], op)
            elif op == 4 or op == 5:
                Extra(title, [400,400,800,50], op)
            elif op == 6 or op == 7:
                Extra(title, [300,400,400,50], op)
            elif op == 8:
                Extra(title, [700,400,400,50], op) 
        else:
            messagebox.showwarning("No existe el archivo binario","Cargue el archivo binario antes de usar cualquier opción")

class Form(Frame):
    def __init__(self,parent):

        #setup

        super().__init__(parent)
        self.configure(bg="#0F110F", padx=10, pady=10)
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.97, relheight=0.98)

        #struct

        self.form_op2(parent)
    
    def form_op2(self,root):

        #var
        id_var = IntVar()
        patente_var = StringVar()
        km_var = IntVar()

        #create

        main_title = Label(self, text="Formulario", font=("TkMenuFont",18), bg=root.color_fondo, fg=root.color_letra)

        bt_exit = Button(self, text="Volver", bg=root.color_boton_s, fg=root.color_letra_s, width=8, height=1, command= lambda: root.destroy())
        bt_confirmar = Button(self, text="Confirmar", bg=root.color_boton_c, width=8, height=1, command= lambda: self.get_values(id_var, patente_var, tipo_cb.current(), pago_cb.current(), pais_cb.current(), km_var, error_lb))

        id_entry = Entry(self, textvariable= id_var)
        patente_entry = Entry(self, textvariable= patente_var)
        tipo_cb = ttk.Combobox(self)
        pago_cb = ttk.Combobox(self)
        pais_cb = ttk.Combobox(self)
        km_entry = Entry(self, textvariable= km_var)

        id_lb = Label(self, text="Identificador del ticket", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=23, wraplength=130, anchor="w")
        patente_lb = Label(self, text="Patente", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=23, wraplength=130, anchor="w")
        tipo_lb = Label(self, text="Tipo de vehículo", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=23, wraplength=130, anchor="w")
        pago_lb = Label(self, text="Tipo de pago", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=23, wraplength=130, anchor="w")
        pais_lb = Label(self, text="Pais de la cabina ", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=23, wraplength=130, anchor="w")
        km_lb = Label(self, text="Kilometraje desde la última cabina de peaje", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, width=24, wraplength=140, anchor="w")
        error_lb = Label(self, text="", font=("Calibri",9), bg="#0F110F", fg="red", anchor="center", wraplength=140)

        #configure

        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1)

        #tile

        main_title.grid(column=0, row=0, columnspan=3, sticky="nswe")
 
        #label

        id_lb.grid(column=0, row=1, sticky="w", padx="5", pady="3")
        patente_lb.grid(column=0, row=2, sticky="w", padx="5", pady="3")
        tipo_lb.grid(column=0, row=3, sticky="w", padx="5", pady="3")
        pago_lb.grid(column=0, row=4, sticky="w", padx="5", pady="3")
        pais_lb.grid(column=0, row=5, sticky="w", padx="5", pady="3")
        km_lb.grid(column=0, row=6, sticky="w", padx="5", pady="3")
        error_lb.grid(column=1, row=7, padx="5", pady="3", sticky="we")

        #entry

        id_entry.grid(column=1, row=1, sticky="we", padx=8)
        patente_entry.grid(column=1, row=2, sticky="we", padx=8)
        km_entry.grid(column=1, row=6, sticky="we", padx=8)
     
        #combobox

        tipo_cb["values"] = ["Motocicleta","Automovil","Camion"]
        tipo_cb["state"] = "readonly"
        pago_cb["values"] = ["Manual","Telepeaje"]
        pago_cb["state"] = "readonly"
        pais_cb["values"] = ["Argentina","Bolivia","Brasil","Paraguay","Uruguay"]
        pais_cb["state"] = "readonly"

        tipo_cb.grid(column=1, row=3, sticky="we", padx=8)
        pago_cb.grid(column=1, row=4, sticky="we", padx=8)
        pais_cb.grid(column=1, row=5, sticky="we", padx=8)
        
        #button

        bt_exit.grid(column=2, row=7, sticky="e", padx=20)
        bt_confirmar.grid(column=0, row=7, sticky="w", padx=20)

    def get_values(self, id_var, patente_var, tipo_var, pago_var, pais_var, km_var, error_lb):
        error = False
        msg_error = "ERROR"

        try:
            id = int(id_var.get())
            patente = patente_var.get()
            tipo = int(tipo_var)
            pago = int(pago_var)
            pais = int(pais_var)
            km = int(km_var.get())
        except:
            error = True
        
        if km < 0:
            error = True
            msg_error = "Ingrese un kilometraje valido"
        if pais == -1:
            error = True
            msg_error = "Seleccione un pais"
        if pago == -1:
            error = True
            msg_error = "Seleccione un tipo de pago"
        if tipo == -1:
            error = True
            msg_error = "Seleccione un tipo de vehiculo"
        if es_minuscula(patente) or patente == "":
            error = True
            msg_error = "Ingrese la Patente (con letras en mayúscula)"
        if id <= 0:
            error = True
            msg_error = "Identificador del ticket mayor a 0"
        

        if not error:
            cargar_datos("archivo_binario.dat",id, patente, tipo, pago, pais, km)
            messagebox.showinfo("Datos cargados",f"Los datos de la patente {patente} fueron cargados")
        else:
            error_lb["text"] = msg_error

class Display(Frame):
    def __init__(self, parent, op):

        #setup
        super().__init__(parent)
        self.configure(bg="#0F110F", padx=10, pady=10)
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.96, relheight=0.96)
        
        #struct

        self.multi_display(parent, op)
    
    def multi_display(self,root,op):

        #var
        if op == 3:
            txt_height = 15
        else:
            txt_height = 10

        #create

        main_title = Label(self, text="Muestra", font=("TkMenuFont",18), bg=root.color_fondo, fg=root.color_letra)

        main_txt = ScrolledText(self, wrap="word", spacing3="10", height=txt_height, font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra, relief="solid")

        bt_exit = Button(self, text="Volver", bg=root.color_boton_s, fg=root.color_letra_s, width=6, height=1, command= lambda: root.destroy())

        #configure

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        #title

        main_title.grid(column=0, row=0, columnspan=3, sticky="nswe")

        #text

        main_txt.grid(column=0, row=1, columnspan=2, sticky="nswe", pady=15)
        if op == 3:
            mostrar_datos(root.archivo_binario, main_txt)
        elif op == 6:
            mostrar_vehiculo_cabina(root.archivo_binario, main_txt)
        elif op == 7:
            mostrar_filas_columnas_matriz(root.archivo_binario, main_txt)
        elif op == 8:
            promedio_distancia(root.archivo_binario, main_txt)
        main_txt["state"] = "disabled"

        #button

        bt_exit.grid(column=1, row=2, sticky="e")

class Search(Frame):
    def __init__(self, parent, sop):

        #setup 

        super().__init__(parent)
        self.configure(bg="#0F110F", padx=10, pady=10)
        self.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.97, relheight=0.98)

        #var

        self.opcion = sop

        #struct

        self.sear(parent)   
    
    def sear(self, root):

        #var

        self.search_var = StringVar()
        
        #create

        main_title = Label(self, text=f"Busqueda", font=("TkMenuFont",18), bg=root.color_fondo, fg=root.color_letra)

        self.main_txt = ScrolledText(self, wrap="word", spacing3="10", height="10", font=("Calibri",9), bg=root.color_fondo, fg=root.color_letra)

        search_entry = Entry(self, textvariable= self.search_var, bg=root.color_fondo, fg=root.color_letra)

        search_btt = Button(self, text="Buscar", bg=root.color_boton_c, width=8, height=1, command= lambda: self.get_entry())
        exit_btt = Button(self, text="Volver", bg=root.color_boton_s, fg=root.color_letra_s, width=6, height=1, command= lambda: root.destroy())

        #configure

        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2,3), weight=1)

        #title

        main_title.grid(column=0, row=0, columnspan=4, sticky="we")

        #text

        self.main_txt.grid(column=0, row=2, columnspan=4, sticky="nswe")
        self.main_txt["state"] = "disabled"

        #button

        search_btt.grid(column=1, row=1, sticky="w")
        exit_btt.grid(column=3, row=3, sticky="se")

        #entry

        search_entry.grid(column=0, row=1, sticky="we", padx=10)
    
    def get_entry(self):
        if self.opcion == 4:
            if es_minuscula(self.search_var.get()):
                messagebox.showerror("Error","La patente no debe poseer minusculas")
            else:
                buscar_patente("archivo_binario.dat", self.search_var.get(), self.main_txt)
        elif self.opcion == 5:
            if self.search_var.get() <= "0":
                messagebox.showerror("Error","El codigo debe ser mayor a 0")
            elif es_letra(self.search_var.get()):
                messagebox.showerror("Error","El codigo debe ser un numero")
            else:
                buscar_codigo("archivo_binario.dat", self.search_var.get(), self.main_txt)


if __name__ == "__main__":
    Main("Gestor de Tickets", [800,600,200,50])
    
    
    