# Opentelementry Docker metrics collector

To simplify shipping metrics from one or many sources, we created Docker Metrics Collector. Docker Metrics Collector is a container that runs Metricbeat with the modules you enable at runtime.

## Installation

1. Use `git` to clone this repository into a suitable folder:

```sh
git clone https://github.com/logzio/otel-docker-collector-metrics.git otel-docker-collector-metrics
```

2.  `Docker` to build a container from this image:

```sh
docker build -t 'otel-docker-collector-metrics:latest' ./otel-docker-collector-metrics
```

## OR you can pull images from docker hub

Pull the Docker image
Download the Opentelementry Docker metrics collector:

```sh
docker pull logzio/docker-otel-collector-metrics
```

## Usage

1. Use the following docker command to run your container.

```sh
docker run --name otel-docker-collector-metrics \
 --env METRICS_TOKEN=<<TOKEN>> \
 --env DOCKER_ENDPOINT=<<DOCKER_ENDPOINT>> \
 --env LOGZIO_LISTENER=<<LOGZIO_LISTENER>> \
 --env COLLECTION_INTERVAL=<<COLLECTION_INTERVAL>> \
 --env TIMEOUT=<<TIMEOUT>> \
 -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(pwd)/config.yaml:/config.yaml \
	/otel-docker-collector-metrics:latest
```

or if it's image from Docker hub

```sh
docker run --name otel-docker-collector-metrics \
 --env METRICS_TOKEN=<<METRICS_TOKEN>> \
 --env DOCKER_ENDPOINT=<<DOCKER_ENDPOINT>> \
 --env LOGZIO_LISTENER=<<LOGZIO_LISTENER>> \
 --env COLLECTION_INTERVAL=<<COLLECTION_INTERVAL>> \
 --env TIMEOUT=<<TIMEOUT>> \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v $(pwd)/config.yaml:/config.yaml \
 logzio/otel-docker-collector-metrics:latest
```

If you prefer to store these environment variables in a file like [this example](./docker.env), you can run docker like so:

```sh
docker run -d --env-file=docker.env -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/config.yaml:/config.yaml otel-docker-collector-metrics:latest
```

| Name                | Description                                                                                                                                           |
| ------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| METRICS_TOKEN       | Your Logz.io metrics account token. Replace <<METRICS_TOKEN>> with the token(see 'Metrics account plan' section') of the account you want to ship to. |
| DOCKER_ENDPOINT     | Address to reach the desired Docker daemon.                                                                                                           |
| LOGZIO_LISTENER     | Database user related what you created for the project                                                                                                |
| COLLECTION_INTERVAL | The interval at which to gather container stats.                                                                                                      |
| TIMEOUT             | The request timeout for any docker daemon query.                                                                                                      |

### 3. Check Logz.io for your metrics

Give your metrics a few minutes to get from your system to ours,
and then open [Logz.io](https://app.logz.io/#/dashboard/kibana).

You can view your metrics in Grafana.
We offer preconfigured dashboards for several sources,
which you can find by clicking **<i class="fas fa-th-large"></i> > Manage**
in the left menu.

## License

is licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
