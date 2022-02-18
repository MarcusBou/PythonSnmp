from DBMIBManager import Manager
from MIBGraphDrawe import ProcentGraph
import time

mang = Manager()
gra = ProcentGraph('RandomNumbDB', 20)

while True: # a while loop for drawing the diagram and adding random data to a database
    gra.draw_usage('Random')#calls draw usage method, and says it takes randoms value from the database
    mang.generate_random_data_to_db()#method generate random data to database
    time.sleep(2)#threads sleep for 2 seconds




