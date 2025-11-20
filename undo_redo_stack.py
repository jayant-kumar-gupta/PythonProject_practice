class Text_Editor:
    def __init__(self):
        self.array = []
        self.backed_texts = []
    def write(self,text):
        if self.backed_texts:
            self.backed_texts =[]
        self.array.append(text)
    def show(self):
        print(" ".join(self.array))
    def undo(self):
        if not self.array:
            print("Cannot undo")
            return
        self.backed_texts.append(self.array.pop())
    def redo(self):
        if not self.backed_texts:
            print("Cannot redo")
            return
        self.array.append(self.backed_texts.pop())

# editor = Text_Editor()
# editor.write("Hello")
# editor.write("World")
# editor.write("!")
# editor.show()
# editor.undo()
# editor.undo()
# editor.show()
# editor.write("Python")
# editor.show()
# editor.redo()
# editor.show()