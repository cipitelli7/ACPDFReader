import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def read_pdf(file_path):
    """Lê e extrai o texto de um PDF."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def highlight_text(file_path, output_path, page_num, text, color=(1, 1, 0)):
    """Destaca um texto específico em uma página com a cor desejada."""
    doc = fitz.open(file_path)
    page = doc[page_num]
    for inst in page.search_for(text):
        annot = page.add_highlight_annot(inst)
        annot.set_colors(stroke=color)
        annot.update()
    doc.save(output_path)
    print(f"Texto destacado salvo em {output_path}")

def underline_text(file_path, output_path, page_num, text):
    """Sublinha um texto específico em uma página."""
    doc = fitz.open(file_path)
    page = doc[page_num]
    for inst in page.search_for(text):
        page.add_underline_annot(inst)
    doc.save(output_path)
    print(f"Texto sublinhado salvo em {output_path}")

def add_annotation(file_path, output_path, page_num, text, x, y):
    """Adiciona uma anotação (nota) em uma página específica."""
    doc = fitz.open(file_path)
    page = doc[page_num]
    page.insert_textbox((x, y, x+200, y+50), text, fontsize=10, color=(1, 0, 0))
    doc.save(output_path)
    print(f"Anotação adicionada e salva em {output_path}")

def add_bookmark(file_path, output_path, title, page_num):
    """Adiciona um bookmark para facilitar a navegação no PDF."""
    doc = fitz.open(file_path)
    doc.set_toc([(1, title, page_num + 1)])
    doc.save(output_path)
    print(f"Bookmark '{title}' adicionado na página {page_num + 1} e salvo em {output_path}")

def draw_shape(file_path, output_path, page_num, shape, rect, color=(0, 0, 1)):
    """Desenha um círculo, quadrado ou seta em uma página."""
    doc = fitz.open(file_path)
    page = doc[page_num]
    if shape == "circle":
        page.draw_circle(rect, color=color, width=2)
    elif shape == "rectangle":
        page.draw_rect(rect, color=color, width=2)
    elif shape == "arrow":
        page.draw_line((rect[0], rect[1], rect[2], rect[3]), color=color, width=2)
    doc.save(output_path)
    print(f"{shape.capitalize()} desenhado e salvo em {output_path}")

def find_text(file_path, search_text):
    """Encontra páginas que contêm um texto específico."""
    doc = fitz.open(file_path)
    found_pages = []
    for page_num, page in enumerate(doc):
        if page.search_for(search_text):
            found_pages.append(page_num)
    return found_pages

def open_toolbox():
    """Cria uma interface gráfica simples com uma caixa de ferramentas."""
    root = tk.Tk()
    root.title("Ferramentas de Edição de PDF")
    
    tk.Label(root, text="Ferramentas Disponíveis").pack()
    tk.Button(root, text="Destacar Texto", command=lambda: print("Destacar Texto")) .pack()
    tk.Button(root, text="Sublinhar Texto", command=lambda: print("Sublinhar Texto")) .pack()
    tk.Button(root, text="Adicionar Anotação", command=lambda: print("Adicionar Anotação")) .pack()
    tk.Button(root, text="Adicionar Bookmark", command=lambda: print("Adicionar Bookmark")) .pack()
    tk.Button(root, text="Desenhar Forma", command=lambda: print("Desenhar Forma")) .pack()
    tk.Button(root, text="Localizar Texto", command=lambda: print("Localizar Texto")) .pack()
    
    root.mainloop()

# Exemplo de uso
pdf_file = "example.pdf"
output_file = "edited_example.pdf"
print(read_pdf(pdf_file))
highlight_text(pdf_file, output_file, 0, "Palavra-chave", color=(1, 0, 0))
underline_text(pdf_file, output_file, 0, "Texto importante")
add_annotation(pdf_file, output_file, 0, "Minha nota", 100, 100)
add_bookmark(pdf_file, output_file, "Capítulo 1", 0)
draw_shape(pdf_file, output_file, 0, "circle", (150, 150, 200, 200))
draw_shape(pdf_file, output_file, 0, "rectangle", (50, 50, 100, 100))
draw_shape(pdf_file, output_file, 0, "arrow", (100, 100, 200, 200))
print("Texto encontrado nas páginas:", find_text(pdf_file, "Palavra-chave"))

# Abrir caixa de ferramentas
tk.Button(None, text="Abrir Ferramentas", command=open_toolbox).pack()
tk.mainloop()
