from controller.controller import Controller
from model.model import Model
from view.viewconsole import View

controller = Controller(View(), Model())
controller.start()
