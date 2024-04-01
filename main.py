# from database.models import *
from gpio.relais import Relais
from webservice.httpservice import *
from interface.frontend import Server
from time import sleep
import multiprocessing

#def database():
    # drop_db_table()
    # create_db_table("schema.sql","processcontrol.sql")

def gpio_process():
    cluster_0_0 = Relais(3)
    while True: 
        try:
            cluster_0_0.turn_on()
            sleep(4)
            cluster_0_0.turn_off()
            sleep(4)
        except Error as e:
            print(e)

def interface_process():
    server = Server()
    server.run()

if __name__ == '__main__':
    try:
        p1 = multiprocessing.Process(target=gpio_process)
        p2 = multiprocessing.Process(target=interface_process)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Shutting down.")
        p1.terminate()
        p2.terminate()
    print("PVMiner Application finished.")