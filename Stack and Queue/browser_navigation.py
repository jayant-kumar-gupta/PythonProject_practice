class Browser:
    def __init__(self):
        self.array = []
        self.backed_pages = []
    def visit(self, url):
        if self.backed_pages:
            self.backed_pages = []
        self.array.append(url)
    def current(self):
        return self.array[-1] if self.array else "Home page"
    def back(self):
        if not self.array:
            return "Cannot go back. No browser opened"
        deleted = self.array.pop()
        self.backed_pages.append(deleted)
        return deleted
    def forward(self):
        if not self.backed_pages:
            print("Cannot forward.")
            return
        self.array.append(self.backed_pages[-1])
        self.backed_pages.pop()

google_chrome = Browser()
# Do your operations here