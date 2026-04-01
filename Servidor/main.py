import tkinter as tk
from tkinter import ttk
import socket
import threading

# --- CONFIGURACIÓN ---
IP_ESP32 = "192.168.1.XX" 
PUERTO = 80

# --- CLASE DE DATOS ---
class DatosSensor:
    def __init__(self, valor):
        self.valor = valor

# --- LÓGICA DE RED ---
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar():
    try:
        sock.connect((IP_ESP32, PUERTO))
        print("Conectado al ESP32")
        threading.Thread(target=recibir_datos, daemon=True).start()
    except Exception as e:
        print("Error al conectar:", e)

def recibir_datos():
    # Convertimos el flujo de red en un formato de lectura por líneas
    archivo_red = sock.makefile('r')
    while True:
        try:
            # Lee exactamente hasta el salto de línea (\n)
            linea = archivo_red.readline()
            if not linea: 
                break # Si está vacío, se desconectó
            
            # Limpiamos espacios y procesamos
            valor_limpio = linea.strip()
            if valor_limpio:
                sensor = DatosSensor(int(valor_limpio))
                # Actualizar la interfaz
                progress['value'] = sensor.valor
                lbl_valor.config(text=f"Potenciómetro: {sensor.valor}")
                
        except ValueError:
            # Si llega basura ocasional, la ignoramos y el ciclo continúa
            pass
        except Exception as e:
            print("Desconectado del servidor:", e)
            break

# Agregamos manejo de errores al enviar para evitar que la app colapse si se cae la red
def led_on(): 
    try: sock.send(b'ON')
    except: print("Error enviando ON")

def led_off(): 
    try: sock.send(b'OFF')
    except: print("Error enviando OFF")

# --- INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Control ESP32 - Instituto Cordillera")
root.geometry("500x320")  # Ventana un poco más grande

tk.Label(root, text="CONTROL DE DISPOSITIVO", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

lbl_valor = tk.Label(root, text="Potenciómetro: 0")
lbl_valor.grid(row=1, column=0, columnspan=2)

# Configurar columnas para que el contenido se expanda proporcionalmente
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

progress = ttk.Progressbar(root, maximum=4095)
progress.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

# Botones con bordes redondeados mediante Canvas personalizado
def _create_rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

class RoundedButton(tk.Canvas):
    def __init__(self, master, text, command, bg, activebg, fg="white", radius=20, width=160, height=45, **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, bd=0, bg=master['bg'], **kwargs)
        self.command = command
        self.bg = bg
        self.activebg = activebg
        self.fg = fg
        self.radius = radius
        self.rect = _create_rounded_rect(self, 2, 2, width-2, height-2, radius, fill=bg, outline="")
        self.text_id = self.create_text(width/2, height/2, text=text, fill=fg, font=("Arial", 10, "bold"))
        self.bind('<Button-1>', self._on_press)
        self.bind('<ButtonRelease-1>', self._on_release)
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

    def _on_press(self, event):
        self.itemconfig(self.rect, fill=self.activebg)

    def _on_release(self, event):
        self.itemconfig(self.rect, fill=self.bg)
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.config(cursor="hand2")

    def _on_leave(self, event):
        self.config(cursor="")

btn_on = RoundedButton(root, text="Encender LED", command=led_on,
                       bg="#7B1FA2", activebg="#E040FB")
btn_on.grid(row=3, column=0, padx=10, pady=10)

btn_off = RoundedButton(root, text="Apagar LED", command=led_off,
                        bg="#E040FB", activebg="#7B1FA2")
btn_off.grid(row=3, column=1, padx=10, pady=10)

threading.Thread(target=conectar, daemon=True).start()

root.mainloop()