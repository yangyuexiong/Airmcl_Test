import threading


class ThreadingA(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.name = threadName

    def run(self):
        print('In run:', self.name)

    def output(self):
        print('In output:', self.name)


class ThreadingB(ThreadingA):
    def __init__(self, threadName, threadID):
        super(ThreadingB, self).__init__(threadID)
        self.threadID = threadID

    def run(self):
        print('In run:', self.name, self.threadID)
