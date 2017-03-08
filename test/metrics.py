#!/usr/bin/env python

import random
import time

def gen_metrics(service_name, service_version, instance_count, timestamp):
    """ """
    measurement = "micro_service"
    tag_set     = "service_name={0},service_version={1}".format(service_name, service_version)
    field_set   = "instances={0}".format(instance_count)

    data_point  = "{measurement},{tag_set} {field_set} {timestamp}".format(
                                                                        measurement=measurement,
                                                                        tag_set=tag_set,
                                                                        field_set=field_set,
                                                                        timestamp=timestamp
                                                                    )
    return data_point

def print_metrics():
    """ """
    instance_count = random.choice([1,2,3,4])
    timestamp   = int(time.time() * 10**9)
    print gen_metrics('jenkins-8080', '1.651.1', instance_count, timestamp)
    print gen_metrics('jenkins-50000', '1.651.1', instance_count, timestamp)


if __name__ == '__main__':
    print_metrics()
