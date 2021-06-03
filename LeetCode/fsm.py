from typing import List

class FSM(object):

  def __init__(self):
    self.states = set()
    self.events = set()
    self.initial_state = None
    self.current_state = None
    self.state_transition_map = {}

  def accept_states(self, states: List[str]) -> None:
    self.states = set(states)
    return None
  
  def accept_events(self, events: List[str]) -> None:
    self.events = set(events)
    return None
  
  def accept_state_transition(self, state: str, event: str, transition: str, actions: List[str]) -> bool:
    if state not in self.states:
      return False
    if event not in self.events:
      return False
    if transition not in self.states:
      return False
    transition_key: str = str(state) + "_" + str(event)
    self.state_transition_map[transition_key] = {"state":str(transition), "actions": list(actions)}
    return True
  
  def accept_initial_state(self, initial_state: str) -> bool:
    if initial_state not in self.states:
      return False
    self.initial_state = str(initial_state)
    return True

  def take_actions_to_perform(self, actions: List[str]):
    for action in actions:
      action()
    return True
  
  def run(self, event: str) -> str:
    if event not in self.events:
      return "Invalid event provided for the state"
    if not self.current_state:
      self.current_state = self.initial_state
    transition_key: str = str(self.current_state) + "_" + str(event)
    next_state: str = self.state_transition_map.get(transition_key, {}).get("state")
    next_actions: List[str] = self.state_transition_map.get(transition_key, {}).get("actions")
    self.take_actions_to_perform(next_actions)
    self.current_state: str = next_state
    return next_state +  " : " + next_actions

def send_to_slack():
  print("I'm sending to slack")

if __name__ == "__main__":
  fsm_obj = FSM()
  fsm_obj.accept_states(["Idle", "Ringing", "Talking", "Voicemail", "Idle"])
  fsm_obj.accept_events(["Incoming", "Pickup", "Hangup"])
  fsm_obj.accept_state_transition("Idle", "Incoming", "Ringing", [send_to_slack])
  fsm_obj.accept_state_transition("Ringing", "Pickup", "Talking", [send_to_slack])
  fsm_obj.accept_state_transition("Talking", "Hangup", "Idle", [send_to_slack])
  fsm_obj.accept_state_transition("Ringing", "Hangup", "Voicemail", [send_to_slack])
  fsm_obj.accept_initial_state("Idle")
  print(fsm_obj.run("Incoming"))
  print(fsm_obj.run("Pickup"))
  print(fsm_obj.run("Hangup"))