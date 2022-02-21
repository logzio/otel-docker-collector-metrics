import os
import yaml
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class MetricsFetcher:
    def __init__(self):
        logger.info('Starting...')

    def store_array_in_yaml(self):
        excluded_images = [ad.strip()
                           for ad in os.environ["EXCLUDED_IMAGES"].split(",")]
        if len(excluded_images) > 0:

            with open('./config.yaml') as file:
                try:
                    config_data = yaml.safe_load(file)
                    config_data['receivers']['docker_stats']['excluded_images'] = excluded_images
                except yaml.YAMLError as exc:
                    logger.error(exc)

            with open('./config.yaml', 'w') as file:
                yaml.dump(config_data, file)

    def default_params(self):

        with open('./config.yaml') as file:
            try:
                config_data = yaml.safe_load(file)
                config_data['receivers']['docker_stats']['collection_interval'] = os.getenv(
                    'COLLECTION_INTERVAL', '30s')
                config_data['receivers']['docker_stats']['endpoint'] = os.getenv(
                    'DOCKER_ENDPOINT', 'unix:///var/run/docker.sock')
                config_data['receivers']['docker_stats']['timeout'] = os.getenv(
                    'TIMEOUT', '5s')

            except yaml.YAMLError as exc:
                logger.error(exc)

        with open('./config.yaml', 'w') as file:
            yaml.dump(config_data, file)

    def run(self):
        try:
            subprocess.run(["./otelcontribcol", "--config", "./config.yaml"])
        except subprocess.CalledProcessError as e:
            logger.error(e)


if __name__ == '__main__':
    w = MetricsFetcher()
    if 'EXCLUDED_IMAGES' in os.environ:
        w.store_array_in_yaml()
    w.default_params()
    w.run()
