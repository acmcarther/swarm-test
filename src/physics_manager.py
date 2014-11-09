class PhysicsManager:

  def initialize(self, play_manager, graphics_manager, clock):
    self.errors = []
    self.play_manager = play_manager
    self.graphics_manager = graphics_manager
    self.clock = clock
    self.last_tick = clock.time()

  def failed(self):
    if self.errors:
      return True
    else:
      return False

  def tick(self):
    delta_t = self.clock.time() - self.last_tick
    print "Debug: Physics Tick %f" % delta_t
    self.last_tick = self.clock.time()

  def clean_up(self):
    print "Debug: Physics Clean Up"

