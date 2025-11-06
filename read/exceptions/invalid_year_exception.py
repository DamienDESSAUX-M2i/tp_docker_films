class InvalidYearException(Exception):
    def __init__(self, msg: str, *args):
        super().__init__(*args)
        self.msg = msg
    
    def display_message_error(self) -> None:
        print(self.msg)