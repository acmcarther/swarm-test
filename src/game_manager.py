from play_manager import PlayManager
from physics_manager import PhysicsManager
from graphics_manager import GraphicsManager
from clock import Clock

class GameManager:

    def initialize(self):
        self.has_errors = False
        self.is_finished = False
        self.init_components()
        self.link_components()
        self.catch_errors()

    def running(self):
        return not (self.has_errors or self.is_finished)

    def tick(self):
        self.physics_manager.tick()
        self.play_manager.tick()
        self.graphics_manager.tick()
        self.catch_errors()
        if self.play_manager.is_finished:
            self.is_finished = True

    def clean_up(self):
        self.physics_manager.clean_up()
        self.play_manager.clean_up()
        self.graphics_manager.clean_up()

    def init_components(self):
        self.clock = Clock()
        self.physics_manager = PhysicsManager()
        self.play_manager = PlayManager()
        self.graphics_manager = GraphicsManager()

    def link_components(self):
        self.physics_manager.initialize(self.play_manager, self.graphics_manager, self.clock)
        self.play_manager.initialize(self.graphics_manager, self.physics_manager, self.clock)
        self.graphics_manager.initialize(self.play_manager, self.physics_manager)

    def catch_errors(self):
        if self.physics_manager.failed():
            self.add_errors(self.physics_manager.errors)
        if self.play_manager.failed():
            self.add_errors(self.play_manager.errors)
        if self.graphics_manager.failed():
            self.add_errors(self.graphics_manager.errors)

