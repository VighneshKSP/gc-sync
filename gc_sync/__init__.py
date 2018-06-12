import configparser
import pathlib

import requests

__version__ = '0.1.0'

CONFIG_URL = 'https://gist.githubusercontent.com/VighneshKSP/64c59e95285362bb37f09dcf68ed0c09/raw/12facf6f4405da3d5a29e0132e4f30624d13b5c7/.gitconfig'

GLOBAL_GIT_CONFIG = '/home/vighnesh/.gitconfig'

SYNC_CONFIG = '/home/vighnesh/my-config'

def main():
    try:
        # Get the config
        response = requests.get(CONFIG_URL)
    except Exception:
        print('Encountered error while fetching configuration')
    else:
        # save the config to local file
        with open(pathlib.Path(SYNC_CONFIG), 'w+') as config:
            config.write(response.text)

        # Include the config in the global git config
        config = configparser.ConfigParser()
        config.read(GLOBAL_GIT_CONFIG)
        config['include'] = {'path': SYNC_CONFIG}

        # write to global config
        with open(GLOBAL_GIT_CONFIG, 'x') as global_config:
            config.write(global_config)

# Initiate
main()
