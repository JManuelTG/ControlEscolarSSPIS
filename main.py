from App import ControlEscolar
import ttkbootstrap as ttk

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = ControlEscolar(root)
    root.mainloop()
