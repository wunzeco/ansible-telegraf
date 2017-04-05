#!/usr/bin/env python
#
#  Description: This script outputs usage metric data of a kong node.

import argparse
import requests
import logging
import json
import sys

#LOGFILE = "/var/log/{}.log".format(os.path.basename(__file__))
KONG_ADMIN_URL = 'http://localhost:8001'

logging.basicConfig(
    stream=sys.stdout,
    #filename=LOGFILE,
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s: %(message)s'
)


# Get Kong node usage metrics
def get_kong_node_usage_metrics(opts):
    """ Returns Kong node usage metrics """

    url = "{0}/status".format(opts['base_url'])

    r = requests.get(url)
    try:
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.debug("http response body - %s", r.text)
        logging.error("An exception occurred: (%s)", e)
        sys.exit(2)

    print r.text

    return True


##################
## Args Parsing ##
##################
parser = argparse.ArgumentParser(description='Kong Metrics Collector Script.')
parser.add_argument('-l', '--admin-url', metavar='KONG_ADMIN_URL', dest='base_url',
        default=KONG_ADMIN_URL, required=False, help='Kong Admin URL e.g. http://localhost:8001')

args = parser.parse_args()


if __name__ == '__main__':
    opts = vars(args)
    logging.debug("Arguments: %s", opts)

    #import pdb; pdb.set_trace()
    get_kong_node_usage_metrics(opts)
