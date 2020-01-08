class SMS_store:
    """SMS class to store messages"""
    def __init__(self):
        """Empty messages list"""
        self.inbox = []
    
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        return self.inbox.append((False, from_number, time_arrived, text_of_SMS))
    

inbox = SMS_store()
inbox.add_new_arrival("0101", "1234", "ABC")
inbox.add_new_arrival("0101", "1234", "ABCxyz")
print(inbox.inbox)