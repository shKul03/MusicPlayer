from app.config import config
from opensearchpy import OpenSearch


def establish_connection():
    return OpenSearch(
        hosts=[{'host': config.os_host, 'port': config.os_port}],
    )

class OpensearchService:
    def __init__(self, **kwargs):
        self.client = establish_connection()
        self.index = kwargs.get('index')


    def initialise_index(self, index):
        if not self.client.indices.exists(index=self.index):
            index_body ={
                'settings':{
                    'index':{
                        'number_of_shards':1,
                        'number_of_replicas':1
                    }
                },
                'mappings':{
                    'properties':{
                        'username':{
                            'type':'keyword',
                            'normaliser':'lowercase'
                        },
                        'password':{
                            'type':'text'
                        }
                    }
                }
            }
            if self.client.create(index, index_body):
                print("Created")
            else:
                print("Error while creating")

        else:
            print("already exists")

conn = OpensearchService()
conn.initialise_index('a')