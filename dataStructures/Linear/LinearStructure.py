class LinearStructure:

    def process_element(self, element):
        pass

    def getting_element_out(self):
        pass

    def enter_element(self, element):
        self.process_element(element)

    def take_out_element(self):
        return self.getting_element_out()

