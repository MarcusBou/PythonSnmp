import matplotlib.pyplot as plt
from MongoDBFile import DatabaseConn
from DBMIBManager import Manager

mang = Manager()


class ProcentGraph:
    def __init__(self, db, ran):
        self.range_preset = ran # to set range of x and y
        self.db = DatabaseConn(db) # database where to get data from
        plt.ion()
        x = range(self.range_preset)
        y = range(self.range_preset)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim(0, 100)# sets max value on y
        self.ax.set_xlim(0, 20)# sets max value on x
        self.line1, = self.ax.plot(x, y, 'b-')

    def draw_usage(self, indicator):
        y = []
        for data in self.db.get_sorted_db("$natural", -1).limit(self.range_preset): # takes a certian limit from the database
            y.append(data[indicator])# Puts into a container of y
        if len(y) >= self.range_preset: # checks length, and if returned less than size
            self.line1.set_ydata(y)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
