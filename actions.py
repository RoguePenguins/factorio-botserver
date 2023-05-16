from rcon.source import Client
import json 

class Actions():
    def __init__(self,player_id):
        self.player_id = player_id
        self.client = Client('127.0.0.1', 27015, passwd='soo8UiSheeph4th')


    def set_waypoint(self,waypoint):
        with self.client as client:
            client.run(f"/c remote.call('actions','move',{waypoint})")


    def set_mining_target(self,entity_name,pos):
        with self.client as client:
            client.run(f"remote.call('actions','mining_target',{self.player_id},{entity_name},{pos}")

    # parses json input into rcon call

    ## schema
    # [{action: [params]}]
    ## 
    def parse(self, json_str):
        tasks = json.loads(json_str)

        for task in tasks:
            for action, params in task.items():
                if action == "move":
                    self.set_waypoint(**params)
                elif action == "mining_target":
                    self.set_mining_target(**params)
                # Add more actions here as needed        
