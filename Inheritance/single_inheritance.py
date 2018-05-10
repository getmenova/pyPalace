class Apple:
    manufacturer = "Apple Inc"
    contact_web_site = "www.apple.com/contact"

    def contact_details(self):
        print('To contact us, log on to ',self.contact_web_site)

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 201*

    def manufacture_details(self):
        print("This Macbook was manufactured in {}".format(self.yearOfManufacture,self.manufacturer))

mac_book = MacBook()
mac_book.manufacture_details()
mac_book.contact_details()
