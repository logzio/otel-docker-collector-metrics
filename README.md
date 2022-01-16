# OpenTelementry Docker Metrics Collector

To simplify shipping metrics from one or many sources, we created Docker Metrics Collector. Docker Metrics Collector is a container that runs Opentelemetry collector.

## Pull the Docker image of the OpenTelementry Docker Metrics Collector

```sh
docker pull logzio/docker-otel-collector-metrics
```

## Run the OpenTelementry Docker Metrics Collector

```sh
docker run --name otel-docker-collector-metrics \
 --env METRICS_TOKEN="<<METRICS-SHIPPING-TOKEN>>" \
 --env DOCKER_ENDPOINT="<<DOCKER_ENDPOINT>>" \
 --env LOGZIO_LISTENER="<<LOGZIO_LISTENER>>" \
 --env COLLECTION_INTERVAL="<<COLLECTION_INTERVAL>>" \
 --env TIMEOUT="<<TIMEOUT>>" \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v $(pwd)/config.yaml:/config.yaml \
 logzio/otel-docker-collector-metrics:latest
```

If you prefer to store these environment variables in an [`.env` file](./docker.env), run the following command:

```sh
docker run -d --env-file=docker.env -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/config.yaml:/config.yaml logzio/otel-docker-collector-metrics:latest
```

| Name                | Description                                                                                                                      |
| ------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| METRICS_TOKEN       | Your Logz.io metrics account token. Replace <<METRICS-SHIPPING-TOKEN>> with the token of the account you want to ship to.        |
| DOCKER_ENDPOINT     | Address to reach the required Docker Daemon.                                                                                     |
| LOGZIO_LISTENER     | Your Logz.io listener address, with port 8070 (http) or 8071 (https). For example, for example: `https://listener.logz.io:8071`. |
| COLLECTION_INTERVAL | The interval at which container stats are gathered.                                                                              |
| TIMEOUT             | The request timeout for any Docker Daemon query.                                                                                 |

### Check Logz.io for your metrics

Give your metrics a few minutes to get from your system to ours,
and then open [Logz.io](https://app.logz.io/#/dashboard/kibana).

You can view your metrics in Grafana.
We offer preconfigured dashboards for several sources,
which you can find by clicking **<i class="fas fa-th-large"></i> > Manage**
in the left menu.

## Versions

0.1.0:

- Created Dockerfiles for amd64 and arm64
- Define config.yaml file

## License

Licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
