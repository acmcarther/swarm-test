class PlayManager:

  def initialize(self, graphics_manager, physics_manager, clock):
    self.is_finished = False
    self.tick_count = 0
    self.errors = []
    self.graphics_manager = graphics_manager
    self.physics_manager = physics_manager
    self.clock = clock

  def failed(self):
    if self.errors:
      return True
    else:
      return False

  def tick(self):
    self.tick_count = self.tick_count + 1
    print "Debug: Play Tick."
    if self.tick_count > 10000:
      self.is_finished = True

  def clean_up(self):
    print "Debug: Play Clean Up"

