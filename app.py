import os
import yaml
import ast


class MetricsFetcher:
    def __init__(self):
        print('Starting...')

    def store_array_in_yaml(self):
        excluded_images = ast.literal_eval(
            os.environ['EXCLUDED_IMAGES'])
        if 'EXCLUDED_IMAGES' in os.environ and len(excluded_images) > 2:

            with open('./config.yaml') as file:
                try:
                    # print(yaml.safe_load(file))
                    config_data = yaml.safe_load(file)
                    if not 'excluded_images' in config_data:
                        config_data['receivers']['docker_stats']['excluded_images'] = excluded_images
                except yaml.YAMLError as exc:
                    print(exc)

            with open('./config.yaml', 'w') as file:
                yaml.dump(config_data, file)

    def default_params(self):
        if 'COLLECTION_INTERVAL' in os.environ:
            collection_interval = os.environ['COLLECTION_INTERVAL']
        else:
            collection_interval = '30s'

        if 'DOCKER_ENDPOINT' in os.environ:
            endpoint = os.environ['DOCKER_ENDPOINT']
        else:
            endpoint = 'unix:///var/run/docker.sock'

        if 'DOCKER_ENDPOINT' in os.environ:
            timeout = os.environ['TIMEOUT']
        else:
            timeout = '5s'

        with open('./config.yaml') as file:
            try:
                config_data = yaml.safe_load(file)
                if not 'excluded_images' in config_data:
                    config_data['receivers']['docker_stats']['collection_interval'] = collection_interval
                    config_data['receivers']['docker_stats']['endpoint'] = endpoint
                    config_data['receivers']['docker_stats']['timeout'] = timeout
            except yaml.YAMLError as exc:
                print(exc)

        with open('./config.yaml', 'w') as file:
            yaml.dump(config_data, file)

    def run(self):
        os.system("./otelcontribcol --config ./config.yaml")


if __name__ == '__main__':
    w = MetricsFetcher()
    w.store_array_in_yaml()
    w.default_params()
    w.run()
