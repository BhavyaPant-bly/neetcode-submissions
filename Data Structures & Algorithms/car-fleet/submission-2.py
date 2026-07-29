class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times=[]
        combined = sorted(zip(position, speed))

        position = [p for p, s in combined]
        speed = [s for p, s in combined]
        
        for i,car in enumerate(position):
            time = (target - car)/speed[i]  
            while(len(times) and times[-1]<=time):
                times.pop()        
            times.append(time)
        return len(times)

        