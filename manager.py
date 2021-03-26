from configparser import ConfigParser


class RelationManager:

    def __init__(self, database_service):
        config_object = ConfigParser()
        config_object.read("TicketingBackground/TicketingSystem/config.ini")
        self.ds = database_service

        config = config_object['QUE1']
        tmp = config['developers']
        self.developer_id_list = tmp.split(',')



    def assign_developer(self, ticket_id):
        self.ds.save_relationship(int(self.developer_id_list[0]),ticket_id, 'developer')
        id = self.developer_id_list.pop(0)
        self.developer_id_list.append(id)




