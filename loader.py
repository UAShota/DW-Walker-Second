"""
Default project loader module
"""

import argparse

from sources.engine import *


class Loader:
    """ Default project loader """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-cfg", required=True)
        self.parser.add_argument("-mod", choices=["w", "t", "wt", "wg"], required=True)

    def run(self):
        """ Application entry point """
        tmp_args = self.parser.parse_args()
        # Разберем конфиг
        if tmp_args.cfg:
            tmp_name = tmp_args.cfg
            tmp_config = __import__("sources.config_%s" % tmp_name, fromlist=["*"])
        else:
            tmp_name = ":"
            tmp_config = __import__("sources.config", fromlist=["*"])
        # Разберем модули
        if "w" in tmp_args.mod:
            tmp_walker = Walker(tmp_config.WalkerConfig, "%s-w" % tmp_name)
            if "g" in tmp_args.mod:
                tmp_trader = Trader(tmp_config.TraderConfig, "%s-t" % tmp_name, tmp_walker.send, tmp_walker.lock)
                tmp_walker.trade = tmp_trader.trade
        if "t" in tmp_args.mod:
            Trader(tmp_config.TraderConfig, "%s-t" % tmp_name)


if __name__ == "__main__":
    Loader().run()
