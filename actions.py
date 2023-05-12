from rcon.source import Client

class Actions():
    def __init__(self,player_id):
        self.player_id = player_id
        self.client = Client('127.0.0.1', 27015, passwd='soo8UiSheeph4th')


    def set_waypoint(self,waypoint):
        with self.client as client:
            client.run(f"/c remote.call('actions','set_waypoints',1,{self.player_id},{waypoint})")


    def set_mining_target(self,name,pos):
        with self.client as client:
            client.run(f"remote.call('actions','mining_target',{self.player_id},{name},{pos}")

    # def insert_to_inventory(self,name,)