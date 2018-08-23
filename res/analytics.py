import boto3
import botocore
import json
import config
import pprint, operator
import res.utils as utils
import res.glob as glob

# =======================================================================================================================
#
#  Supported services   : Elasticsearch Service, 
#  Unsupported services : Athena, EMR, CloudSearch, Kinesis, Quicksight, Data Pipeline, Glue
#
# =======================================================================================================================

#  ------------------------------------------------------------------------
#
#    Elasticsearch
#
#  ------------------------------------------------------------------------

def get_es_inventory(oId):

    """
        Returns Elasticsearch details

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: Elasticsearch inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/es.html
    """ 
    
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "es", 
        aws_region = "all", 
        function_name = "list_domain_names", 
        key_get = "DomainNames",
        join_key = "DomainName",
        detail_join_key = "DomainName",
        detail_function = "describe_elasticsearch_domain",
        detail_get_key = "DomainStatus"
    )


#  ------------------------------------------------------------------------
#
#    Cloudsearch
#
#  ------------------------------------------------------------------------

def get_cloudsearch_inventory(oId):

    """
        Returns cloudsearch details

        :param oId: ownerId (AWS account)
        :type oId: string

        :return: cloudsearch inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/cloudsearch.html
    """ 
    
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "cloudsearch", 
        aws_region = "all", 
        function_name = "describe_domains", 
        key_get = "DomainStatusList"
    )


#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')