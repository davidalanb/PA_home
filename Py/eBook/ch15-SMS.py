
class SMS_store:
    """
    each message is a tuple:
        (has_been_viewed, from_number, time_arrived, text_of_SMS)
    """

    def __init__(self):
        self.messages=[]

    def __str__(self):
        return '\n'.join(str(msg) for msg in self.messages)

    def __int__(self):
        return len(self.messages)

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its
        # has_been_viewed status is set False.
        msg = (False, from_number, time_arrived, text_of_SMS)
        self.messages.append( msg )
        pass

    def message_count(self):
        return int(self)

    def get_unread_indexes(self):
        # Returns list of indexes of all not-yet-viewed SMS messages

        unviewed=[]
        for i in range(len(self.messages)):
            msg = self.messages[i]
            has_been_read = msg[0]
            if not has_been_read:
                unviewed.append(i)

        return unviewed

        '''
        unviewed = []

        for i, msg in enumerate(self.messages):
            if msg[0] == False:
                unviewed.append(i)

        return unviewed
        '''
    def get_message(self, i):
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
        msg = self.messages[i]

        self.messages[i] = ( True, msg[1], msg[2], msg[3] )

        return msg[1], msg[2], msg[3]

    def delete(self, i):
        # Delete the message at index i
       self.messages.pop(i)

    def clear(self):
        # Delete all messages from inbox
        self.messages = []


def testing():

    my_inbox = SMS_store()

    messages = [(5550123, 2304, "Hey buddy"),
                (5550123, 2305, "How ya doin"),
                (5550123, 2306, "Okay WHATEVER")]

    for msg in messages:
        my_inbox.add_new_arrival( msg[0], msg[1], msg[2] )

    #print(my_inbox.get_unread_indexes())

    for i in my_inbox.get_unread_indexes():
        print( my_inbox.get_message(i) )

    print(my_inbox.get_unread_indexes())

    #print(my_inbox)

testing()

