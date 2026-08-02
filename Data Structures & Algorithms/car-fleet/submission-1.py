class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = []
        for car_position, car_speed in cars:
            time_to_target = (target - car_position) / car_speed
            if not fleets:
                fleets.append(time_to_target)
            elif time_to_target > fleets[-1]:
                fleets.append(time_to_target)

        return len(fleets)
