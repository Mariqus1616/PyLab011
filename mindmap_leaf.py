class MindMapLeaf(object):
    def __init__(self,name:str, shape:str):
        self.name = name
        self.shape = shape

    @staticmethod
    def get_shape_representation(shape:str) -> str:
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}((",
            "rectangle": "[{}]",
            "ellipse": "[{}]",
        }
        return shapes.get(shape, '{}')

    def display(self, indent=0):
        print(' '*indent+ str(self))

    def __str__(self):
        shape_representation = self.get_shape_representation(self.shape)
        return shape_representation.format(self.name)

if __name__ == '__main__':
    mml = MindMapLeaf("Trevor","hexagon")
    mml.display()


