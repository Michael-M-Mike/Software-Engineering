class Hole:
    def __init__(self, base, size):
        self.base = base
        self.size = size
        
        
class Segment:
    def __init__(self, name, parent_process, base, size, free):
        self.name = name
        self.parent_process = parent_process
        self.size = size
        self.base = base
        self.free = free

    def deallocate(self):
        if not self.free:
            self.name = "Hole"
            self.parent_process = None
            self.size = None
            self.base = None
            self.free = True

        
class Process:

    count = 0

    def __init__(self, segments, old=False):
        if old:
            self.name = "Old Process"
        else:
            self.name = "Process " + str(Process.count)
        Process.count += 1
        self.segments = segments

    def deallocate(self):
        for seg in self.segments:
            seg.deallocate()


class Memory:
    def __init__(self, segments):
        self.segments = []
        self.processes = []

        for segment in segments:
            self.segments.append(segment)
