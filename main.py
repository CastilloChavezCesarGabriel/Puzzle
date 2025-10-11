from model.puzzleModel import Model
from view.puzzleView import View
from controller.puzzleController import Controller

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model,view)
    controller.run()