""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import os
import json
import time
import grpc
import pyvelociraptor
from pyvelociraptor import api_pb2
from pyvelociraptor import api_pb2_grpc
from connectors.cyops_utilities.builtins import download_file_from_cyops
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('rapid7-velociraptor')


class Velociraptor(object):
    def __init__(self, config):
        try:
            cert_file_iri = config.get('cert_file', {}).get('@id')
            filename = download_file_from_cyops(cert_file_iri).get('cyops_file_path')
            file_path = os.path.join('/tmp', filename)
            self.config = pyvelociraptor.LoadConfigFile(file_path)
        except Exception as err:
            logger.exception("{0}".format(str(err)))
            raise ConnectorError("{0}".format(str(err)))

    def make_request(self, query, env_dict={}, org_id=None):
        try:
            creds = grpc.ssl_channel_credentials(
                root_certificates=self.config["ca_certificate"].encode("utf8"),
                private_key=self.config["client_private_key"].encode("utf8"),
                certificate_chain=self.config["client_cert"].encode("utf8"))

            options = (('grpc.ssl_target_name_override', "VelociraptorServer",),)

            env = []
            for k, v in env_dict.items():
                env.append(dict(key=k, value=v))

            with grpc.secure_channel(self.config["api_connection_string"],
                                     creds, options) as channel:
                stub = api_pb2_grpc.APIStub(channel)

                request = api_pb2.VQLCollectorArgs(
                    org_id=org_id,
                    max_wait=1,
                    max_row=100,
                    Query=[api_pb2.VQLRequest(
                        Name="Executing Query",
                        VQL=query,
                    )],
                    env=env,
                )

                for response in stub.Query(request):
                    if response.Response:
                        resp = json.loads(response.Response)
                        return resp

                    elif response.log:
                        logger.debug("%s: %s" % (time.ctime(response.timestamp / 1000000), response.log))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def build_query_string(params):
    params = {k: v for k, v in params.items() if v is not None and v != '' and v is not False}
    query_string = ""
    for k, v in params.items():
        if isinstance(v, str) and k != "env" and k != "spec":
            query_string += f"{k}='{v}',"
        else:
            if isinstance(v, bool):
                query_string += f"{k}=TRUE,"
            else:
                query_string += f"{k}={v},"
    query_string = query_string.strip(",")
    return query_string


def list_clients(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM clients({q})"
    response = v.make_request(query)
    return response


def run_artifacts_collection(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT collect_client({q}) FROM scope()"
    response = v.make_request(query)
    return response


def get_flow_results(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM flow_results({q})"
    response = v.make_request(query)
    return response


def list_flows(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM flows({q})"
    response = v.make_request(query)
    return response


def create_flow_download(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT create_flow_download({q}) FROM scope()"
    response = v.make_request(query)
    return response


def dump_artifact_definitions(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM artifact_definitions({q})"
    response = v.make_request(query)
    return response


def create_hunt(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT hunt({q}) FROM scope()"
    response = v.make_request(query)
    return response


def list_hunts(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM hunts({q})"
    response = v.make_request(query)
    return response


def get_hunt_results(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT * FROM hunt_results({q})"
    response = v.make_request(query)
    return response


def create_hunt_download(config, params):
    v = Velociraptor(config)
    q = build_query_string(params)
    query = f"SELECT create_hunt_download({q}) FROM scope()"
    response = v.make_request(query)
    return response


def run_vql_query(config, params):
    v = Velociraptor(config)
    response = v.make_request(params.get('query'))
    return response


def _check_health(config):
    try:
        response = run_vql_query(config, params={"query": "SELECT * FROM info()"})
        return True
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


operations = {
    'list_clients': list_clients,
    'run_artifacts_collection': run_artifacts_collection,
    'get_flow_results': get_flow_results,
    'list_flows': list_flows,
    'create_flow_download': create_flow_download,
    'dump_artifact_definitions': dump_artifact_definitions,
    'create_hunt': create_hunt,
    'list_hunts': list_hunts,
    'get_hunt_results': get_hunt_results,
    'create_hunt_download': create_hunt_download,
    'run_vql_query': run_vql_query
}
