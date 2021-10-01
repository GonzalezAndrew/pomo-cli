'''
State Machine States:
    READY  (0)  := The state machine is ready to recieve changes.
    PAUSED (1)  := The state machine is in a paused state and cannot be affected.
    LOCKED (2)  := The state machine is in use and locked.

start command:
    The following will be ran during start up of the pomo cli tool:
        1. Verify the state machine is not in a paused or locked state. The state machine needs to be in READY.
        2. Verify the config & temp directory is in the proper place.
        3. Verify the temp directory does not have any timestamp files that will be mistake when referened.
    The following will be ran when the start command is invoked:
        1. Verify the temp directory does not have any timestamp files that will be mistake when referened.
        2. Start the time & create the timestamp file in the temp directory
'''
import os

class State():
    def __init__(self):
        self.state = "READY"
        self.state_int = 0

    def pause_state(self):
        self.state = "PAUSED"
        self.state_int = 1

    def lock_state(self):
        self.state = "LOCKED"
        self.state_int = 2

    def __config_pomo_dir(self):
        ''' Configure the pomo config directory.
        '''
        pass

    def __config__tmp_dir(self):
        ''' Configure the temporary pomo directory.
        '''
        pass
    
    def __create_timestamp_file(self, overwrite: bool = False):
        ''' Create the timestamp file in the temp directory.
        :params overwrite: Overwrite the timestamp file. This is used when
            changing the state machine to a PAUSED state.
        :rtype: None
        :return: None
        '''
        pass