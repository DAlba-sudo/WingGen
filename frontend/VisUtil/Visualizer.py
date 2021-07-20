from frontend.VisUtil.VisModule import VisModule


VisModule

# this class will house the code for visualization
class Visualizer():
    def __init__(self) -> None:
        self.visModules = []                    # a list of all vis modules
    
    def addVisModule(self, visModule: VisModule):
        self.visModules.append(visModule)
    
    # main entry point
    def start(self):
        for module in self.visModules:
            module.visualize()
        
        # clears the visualizer list 
        self.visModules.clear()        