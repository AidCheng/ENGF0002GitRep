# Bug report

## The known bugs including

- The frogger died when stepping on the turtle
- The game won't update when frogger lose the first life
- When all the lives are consumed, the game won't continue
- Frog died when entering the left-hand home
- Game won't fail when the time is over
- The frogger will move out of the game field when going down at the initial position

## Bug fix

- Died when entering the log:

    ```py
    # fr_model line-372
    for log in self.logs:
        if log.contains(self.frog):  
            'cause of the bug: a typo (on_long = log), should be on_log'
            on_log = log
            break
    ```

- Update new life

    ```py
    # fr_model line-329
    def new_life(self):
        self.controller.update_lives(self.lives)
        'MISSING FOLLOWING LINE'
        self.rest_postion()
    ```

- Restart game when all lives are consumed
  
  ```py
  # fr_model line-340
  def restart(self):
    self.level
    self.score = 0
    self.reset_level()
    self.dont_update_speed = True
    'MISSING FOLLOWING LINE CAUSED THE BUG'
    self.game_running = True
  ```

- Did not create left hand home when initialising
  
    ```py
    # fr_model line-271
    x = (spacing + GRID_SIZE)//2
    'create the first home here’
    self.homes_x.append(x)
    self.homes_occupied.append(False)

    for i in range(0,6):
        x = x + GRID_SIZE
        self.homes_x.append(x)
        self.homes_occupied.append(False)
    ```

- Game fail when time over

    ```py
    # fr_model line-460
    'define check_time function'
    def check_time(self):
        remaining_time = int(self.end_time - time.time())
        if remaining_time == 0:
            self.game_over()

    update(self):
        if [condition]:
            'add following line'
            self.check_time()
    ```

- Frogger move out the game field

    ```py
    # fr_model line-134
    def move(self.dir):
        'add the following codes'
        (self.initial_x,self.intial_y) = self.start_position
        (self.current_x,self.current_y) = self.get_position()

        if self.current_y >= self.initial_y and dir == Direction.DOWN:
            self.moving = False
            return
        
        # *codes for moving control
    ```