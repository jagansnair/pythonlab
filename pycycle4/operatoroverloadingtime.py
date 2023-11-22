class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        total_seconds = self.second + other.second
        carry_minutes, self.second = divmod(total_seconds, 60)

        total_minutes = self.minute + other.minute + carry_minutes
        carry_hours, self.minute = divmod(total_minutes, 60)

        self.hour += other.hour + carry_hours

        return Time(self.hour, self.minute, self.second)

    def __str__(self):
        return f"{self.hour} hours, {self.minute} minutes, {self.second} seconds"


o1 = Time(2, 40, 10)
o2 = Time(4, 20, 50)

sum_of_time = o1 + o2
print("Sum of time:", sum_of_time)
