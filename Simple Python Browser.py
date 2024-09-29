import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView instance
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl("http://www.google.com")  # Default URL

        # Set up the toolbar
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        self.toolbar.addAction(reload_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)

        # Update URL bar
        self.browser.urlChanged.connect(self.update_url_bar)

        # Window settings
        self.setWindowTitle("Simple Python Browser")
        self.setGeometry(100, 100, 1200, 800)
        self.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(url)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
