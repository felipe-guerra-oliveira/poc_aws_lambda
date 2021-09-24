#!/bin/python

import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

session = boto3.Session(region_name="sa-east-1")
ec2 = session.client('ec2')

def get_my_ec2_instances():
    try:
        filters = [{
            'Name': 'tag:Project',
            'Values': ['POC']
        }]
        response = ec2.describe_instances(Filters=filters)
        return response['Reservations']
    except Exception as e:
        logger.error(('Erro ao tentar pegar os dados das instâncias EC2 %s') % (e))
        raise e

def stop_ec2_instance(ec2_instance_id):
    try:
        response = ec2.stop_instances(InstanceIds=[ec2_instance_id])
        logger.info('Instância %s parada...[%s]' % (ec2_instance_id, response['StoppingInstances'][0]))

    except Exception as e:
        logger.error(('Erro ao tentar iniciar a instância EC2:%s [%s]') % (ec2_instance_id, e))
        raise e

def start_ec2_instance(ec2_instance_id):
    try:
        ec2.start_instances(InstanceIds=[ec2_instance_id])
        logger.info('Instância %s iniciada...' % (ec2_instance_id))

    except Exception as e:
        logger.error(('Erro ao tentar iniciar a instância EC2:%s [%s]') % (ec2_instance_id, e))
        raise e

def cloudwatch_handler(event, context):
    try:
        instances = get_my_ec2_instances()

        #Navega em todas as instâncias do array
        for instance in instances[0]['Instances']:
            stop_ec2_instance(instance['InstanceId'])
            # if instance['State']['Name'] == 'stopped':
            #     start_ec2_instance(instance['InstanceId'])
            # elif instance['State']['Name'] == 'running':
                # stop_ec2_instance(instance['InstanceId'])

    except Exception as e:
        logger.error(e)
        raise e

if __name__ == '__main__':
    cloudwatch_handler(None, None)
