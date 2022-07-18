import os
import shutil
import logging

from pyclowder.extractors import Extractor
from pyclowder.utils import CheckMessage
import pyclowder.files

from hsclient import HydroShare


class HydrosharePublisher(Extractor):
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

        # TODO: How to pass in HS credentials?

        # https://www.hydroshare.org/hsapi/
        # https://github.com/hydroshare/hsclient
        hs = HydroShare()
        hs.sign_in()

        # Create the new, empty resource
        new_resource = hs.create()

        # Get the HydroShare identifier for the new resource
        resIdentifier = new_resource.resource_id
        logger.info('The HydroShare Identifier for your new resource is: ' + resIdentifier)

        # Construct a hyperlink for the new resource
        logger.info('Your new resource is available at: ' +  new_resource.metadata.url)

        # Set the Title for the resource
        new_resource.metadata.title = 'Resource for Testing the HS RDF HydroShare Python Client'

        # Set the Abstract text for the resource
        new_resource.metadata.abstract = (
            'This resource was created as a demonstration of using the HS RDF '
            'Python Client for HydroShare. Once you have completed all of the '
            'steps in this notebook, you will have a fully populated HydroShare '
            'Resource.'
        )

        # Call the save function to save the metadata edits to HydroShare
        new_resource.save()

        for f in resource["files"]:
            filename = f["filename"]
            logger.info("Handling %s " % filename)

if __name__ == "__main__":
    extractor = HydrosharePublisher()
    extractor.start()