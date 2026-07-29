class TimeMap:

    def __init__(self):
        self.store={}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key,timestamp)]=value


    def get(self, key: str, timestamp: int) -> str:
        while timestamp >=0:
            if (key,timestamp) in self.store:
                return self.store[(key,timestamp)]
            timestamp-=1
        return ""

        
