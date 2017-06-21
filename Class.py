'''
Class is a blueprint for an object
'''

class phone():

    def __init__(self, p, s):
        self.processor = p
        self.screen_size = s

    def details(self):
        print "Details of the phone are: "
        print self.processor
        print self.screen_size

n = phone("Nokia n95:Quad core", "6 inch")
#n.__init__("Nokia n95:Quad core", "6 inch")
n.details()

s = phone("Sony-ericsson w500: Dual core", "6 inch")
#s.__init__("Sony-ericsson w500: Dual core", "6 inch")
s.details()