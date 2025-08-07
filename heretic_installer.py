import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Candidatos a diretório onde pode estar o Heretic.wad original
POSSIBLE_PATHS = [
    r"C:\XboxGames\Heretic + Hexen\Content",
    r"C:\Program Files (x86)\Steam\steamapps\common\Heretic",  # tentativa padrão Steam
    r"C:\SteamLibrary\steamapps\common\Heretic",               # tentativa alternativa Steam
]

HERETIC_WAD_NAME = "Heretic.wad"

def localizar_heretic():
    for path in POSSIBLE_PATHS:
        wad_path = os.path.join(path, HERETIC_WAD_NAME)
        if os.path.exists(wad_path):
            return wad_path
    return None

def substituir_wad():
    origem = filedialog.askopenfilename(title="Selecione o Heretic.wad traduzido",
                                        filetypes=[("Arquivos WAD", "*.wad")])
    if not origem:
        return
    
    destino_original = localizar_heretic()
    if not destino_original:
        messagebox.showerror("Erro", "Heretic.wad original não encontrado em nenhum dos caminhos padrão.")
        return

    try:
        backup_path = destino_original + ".bak"
        if not os.path.exists(backup_path):
            shutil.move(destino_original, backup_path)
        else:
            os.remove(destino_original)

        shutil.copy(origem, destino_original)

        messagebox.showinfo("Sucesso", f"Heretic.wad substituído com sucesso!\nBackup salvo como Heretic.wad.bak")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")

# Interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Tradutor de Heretic.wad")
    root.geometry("400x200")

    lbl = tk.Label(root, text="Clique no botão para substituir o Heretic.wad original.", wraplength=350)
    lbl.pack(pady=20)

    btn = tk.Button(root, text="Selecionar Tradução e Substituir", command=substituir_wad, bg="#4CAF50", fg="white")
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
