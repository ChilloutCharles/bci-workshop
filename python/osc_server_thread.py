import threading
import math
import pickle
import os.path

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

SAVE_PATH = 'saved_weights.pkl'


def weight_handler(tune_addr, args, value):
    [serv_thread] = args
    param_addr_prefix = tune_addr.replace('_tune', '')

    new_weight = 1.0 / math.pow(math.e, 10.0 * (1.0 - value))
    weight_dict = serv_thread.get_weights()

    for param_addr in weight_dict:
        if param_addr.startswith(param_addr_prefix):
            weight_dict[param_addr] = new_weight

    serv_thread.set_weights(weight_dict)


class osc_server_thread(threading.Thread):
    def __init__(self, weights_dict, ip, port):
        threading.Thread.__init__(self)

        self.weights_dict = weights_dict
        if os.path.isfile(SAVE_PATH):
            print('Loading tune settings')
            with open(SAVE_PATH, 'rb') as f:
                self.weights_dict = pickle.load(f)

        dispatcher = Dispatcher()
        dispatcher.map("/avatar/parameters/osc*_tune", weight_handler, self)
        self.osc_server = BlockingOSCUDPServer((ip, port), dispatcher)

    def get_weights(self):
        return self.weights_dict

    def set_weights(self, weights_dict):
        self.weights_dict = weights_dict

    def run(self):
        print('Running OSC Server')
        self.osc_server.serve_forever()

        print('Saving tune settings')
        with open(SAVE_PATH, 'wb') as f:
            pickle.dump(self.weights_dict, f)

        print('Stopping OSC Server')

    def stop(self):
        self.osc_server.shutdown()

    def __del__(self):
        self.stop()


if __name__ == '__main__':
    server = osc_server_thread({}, '127.0.0.1', 9001)
    server.start()
    server.osc_server.shutdown()
