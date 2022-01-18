import os
import yaml
from decouple import config
import ast


class MetricsFetcher:
    def __init__(self):
        print('Starting...')

    def store_array_in_yaml(self):
        excluded_images = ast.literal_eval(
            config('EXCLUDED_IMAGES'))
        if len(excluded_images) > 0:

            with open('./config.yaml') as file:
                try:
                    # print(yaml.safe_load(file))
                    config_data = yaml.safe_load(file)
                    if not 'excluded_images' in config_data:
                        config_data['receivers']['docker_stats']['excluded_images'] = excluded_images
                        print(config_data)
                except yaml.YAMLError as exc:
                    print(exc)

            with open('./config.yaml', 'w') as file:
                yaml.dump(config_data, file)

    def default_params(self):
        print('find')

    def run(self):
        os.system("./otelcontribcol --config ./config.yaml")


if __name__ == '__main__':
    w = MetricsFetcher()
    w.store_array_in_yaml()
    w.run()
