class IdHandler:
    def __init__(self) -> None:
        self.__next_id = -1
    
    def id(self) -> int:
        self.__next_id += 1
        return self.__next_id

id_handler = IdHandler()