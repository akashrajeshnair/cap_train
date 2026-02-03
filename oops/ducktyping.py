# duck typing
class Pencil:
    def use(self):
        return "Writing"
    
class Sharpener:
    def use(self):
        return "Sharpening"
    
def perform_task(tool):
    print(tool.use())

perform_task(Pencil())
perform_task(Sharpener())