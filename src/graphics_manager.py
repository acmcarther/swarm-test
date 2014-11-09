class GraphicsManager:

  def initialize(self, play_manager, physics_manager):
    self.errors = []
    self.play_manager = play_manager
    self.physics_manager = physics_manager

  def failed(self):
    if self.errors:
      return True
    else:
      return False

  def tick(self):
    print "Debug: Graphics Tick."

  def clean_up(self):
    print "Debug: Graphics Clean Up."
