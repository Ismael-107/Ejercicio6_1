import tkinter as tk

# =========================
# OPERACIONES
# =========================

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0 or a == 0:
        return "Error"
    return a / b


# =========================
# APP
# =========================

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora con pruebas integradas")
        self.root.geometry("420x500")

        # entradas
        self.a = tk.Entry(root)
        self.a.pack(pady=5)

        self.b = tk.Entry(root)
        self.b.pack(pady=5)

        # resultado calculadora
        self.resultado = tk.Label(root, text="Resultado", font=("Arial", 14))
        self.resultado.pack(pady=10)

        # botones operaciones
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Button(frame, text="+", width=5, command=self.op_suma).grid(row=0, column=0)
        tk.Button(frame, text="-", width=5, command=self.op_resta).grid(row=0, column=1)
        tk.Button(frame, text="×", width=5, command=self.op_mult).grid(row=0, column=2)
        tk.Button(frame, text="÷", width=5, command=self.op_div).grid(row=0, column=3)

        # botón pruebas
        tk.Button(root, text="PRUEBAS", bg="orange", command=self.ejecutar_pruebas).pack(pady=15)

        # salida pruebas
        self.salida = tk.Text(root, height=15, width=50)
        self.salida.pack()

    # =========================
    # CALCULADORA
    # =========================

    def get_values(self):
        try:
            return float(self.a.get()), float(self.b.get())
        except:
            return None, None

    def mostrar(self, txt):
        self.resultado.config(text=str(txt))

    def op_suma(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar(suma(a, b))

    def op_resta(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar(resta(a, b))

    def op_mult(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar(multiplicacion(a, b))

    def op_div(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar(division(a, b))

    # =========================
    # PRUEBAS YA INCLUIDAS
    # =========================

    def ejecutar_pruebas(self):

        # 🔥 PRUEBAS FIJAS (NO LAS ESCRIBE EL USUARIO)
        tests = [
            ("suma", suma(2, 3), 5),
            ("resta", resta(5, 2), 3),
            ("multiplicacion", multiplicacion(3, 4), 12),
            ("division", division(10, 0), 5),
            ("division_cero", division(10, 0), "Error"),
        ]

        self.salida.delete("1.0", tk.END)

        correctas = 0

        for nombre, resultado, esperado in tests:

            if str(resultado) == str(esperado):
                self.salida.insert(tk.END, f"✔ {nombre} correcta\n")
                correctas += 1
            else:
                self.salida.insert(
                    tk.END,
                    f"❌ {nombre} falló | obtenido {resultado} | esperado {esperado}\n"
                )

        self.salida.insert(tk.END, "\n")
        self.salida.insert(tk.END, f"Resultado final: {correctas}/5 correctas\n")


# =========================
# MAIN
# =========================

root = tk.Tk()
app = CalculadoraApp(root)
root.mainloop()