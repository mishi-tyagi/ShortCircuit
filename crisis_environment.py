from crisis_model import Emergency, Unit

class CrisisEnvironment:
    def __init__(self):
        self.time = 0
        self.emergencies = []
        self.units = []

    def reset(self):
        self.time = 0
        self.emergencies = [
            Emergency(id="E1", type="fire", severity=1, location=(2,3), time_active=0)
        ]
        self.units = [
            Unit(id="A1", type="ambulance", location=(0,0), available=True)
        ]
        return self.get_state()

    def step(self, action):
        self.time += 1

        # simple escalation logic
        for e in self.emergencies:
            e.time_active += 1
            if e.time_active >= 3:
                e.severity += 1

        return self.get_state()

    def get_state(self):
        return {
            "time": self.time,
            "emergencies": [e.dict() for e in self.emergencies],
            "units": [u.dict() for u in self.units]
        }