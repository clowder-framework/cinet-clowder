import os
import shutil
import logging

from pyclowder.extractors import Extractor
from pyclowder.utils import CheckMessage
import pyclowder.files


class EarthChemPublisher(Extractor):
    def __init__(self):
        Extractor.__init__(self)

        # parse command line and load default logging configuration
        self.setup()

        # setup logging for the exctractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

    # Check whether dataset already has metadata
    def check_message(self, connector, host, secret_key, resource, parameters):
        # TODO: Return bypass and download it directly to destination ourselves
        return CheckMessage.bypass

    def process_message(self, connector, host, secret_key, resource, parameters):
        logger = logging.getLogger('__main__')

        for f in resource["files"]:
            filename = f["filename"]
            logger.info("Handling %s " % filename)

if __name__ == "__main__":
    extractor = EarthChemPublisher()
    extractor.start()