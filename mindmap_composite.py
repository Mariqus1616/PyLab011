from mindmap_leaf import MindMapLeaf

class MindMapComposite(object):
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        shape_representation = MindMapComposite.get_shape_representation(self.shape)
        return shape_representation.format(self.name)

    @staticmethod
    def get_shape_representation(shape: str) -> str:
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}((",
            "rectangle": "[{}]",
            "ellipse": "[{}]"
        }
        return shapes.get(shape,"{}")

    def display(self, indent=0):
        if indent == 0:
            print("mindmap\n  root", end="")
            print(str(self))
            indent=2
        else:
            print(' ' * indent + str(self))

        for child in self.children:
            child.display(indent+2)

if __name__ == "__main__":
    mindMap = MindMapComposite("mindmap", "circle")
    tools = MindMapComposite("tools", "Bang")

    tools.add_child(MindMapLeaf("Pen and paper", "retangle"))
    tools.add_child(MindMapLeaf("mermaid", "retangle"))
    mindMap.add_child(tools)



    mindMap.display()



