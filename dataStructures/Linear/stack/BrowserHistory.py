class BrowserHistory_n:

    def __init__(self, homepage: str):
        self.pages_stack = [homepage]
        self.forward_history_stack = []

    def visit(self, url: str) -> None:
        if self.forward_history_stack:
            self.forward_history_stack = []
        self.pages_stack.append(url)

    def back(self, steps: int) -> str:

        for _ in range(steps):
            if len(self.pages_stack) == 1:
                return self.pages_stack[-1]
            self.forward_history_stack.append(self.pages_stack.pop())

        return self.pages_stack[-1]

    def forward(self, steps: int) -> str:

        for _ in range(steps):
            if not self.forward_history_stack:
                return self.pages_stack[-1]
            self.pages_stack.append(self.forward_history_stack.pop())
        
        return self.pages_stack[-1]
    
    def display_browser_history(self):

        for i in range(len(self.pages_stack) - 1, -1, -1):
            print(i, ': ', self.pages_stack[i], sep = '')
    

class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current_index = 0
        self.lastPage = 0

    def visit(self, page):
        self.current_index += 1
        if self.current_index == len(self.history):
            self.history.append(page)
        else:
            self.history[self.current_index] = page
        self.lastPage = self.current_index

    def back(self, steps):

        self.current_index = max( 0, self.current_index - steps )
        return self.history[self.current_index]
    
    def forward(self, steps):

        self.current_index = min(self.lastPage, self.current_index + steps)
        return self.history[self.current_index]
    
    def display_browser_history(self):

        for i in range(len(self.history)-1, -1, -1):
            print(i, ': ',  self.history[i], sep='')


if __name__ == '__main__':

    my_browser = BrowserHistory('google.com')
    my_browser.visit('facebook.com')
    my_browser.visit('linkedin.com')
    my_browser.visit('leetcode.com')
    my_browser.display_browser_history()
    print(my_browser.back(100))
    print(my_browser.forward(100))
    print(my_browser.back(1000))
    my_browser.visit('boot.dev')
    my_browser.display_browser_history()
