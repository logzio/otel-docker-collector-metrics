# OpenTelementry Docker Metrics Collector

To simplify shipping metrics from one or many sources, we created Docker Metrics Collector. Docker Metrics Collector is a container that runs Opentelemetry collector.

## Pull the Docker image of the OpenTelementry Docker Metrics Collector

```sh
docker pull logzio/docker-otel-collector-metrics
```

## Run the OpenTelementry Docker Metrics Collector

```sh
docker run --name docker-otel-collector-metrics \
 --env METRICS_TOKEN="<<METRICS-SHIPPING-TOKEN>>" \
 --env LOGZIO_LISTENER="<<LOGZIO_LISTENER>>" \
 -v /var/run/docker.sock:/var/run/docker.sock \
 logzio/docker-otel-collector-metrics:latest
```

If you prefer to store these environment variables in an [`.env` file](./docker.env), run the following command:

```sh
docker run -d --env-file=docker.env -v /var/run/docker.sock:/var/run/docker.sock logzio/docker-otel-collector-metrics:latest
```

| Name                | Description                                                                                                               |
| ------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| METRICS_TOKEN       | Your Logz.io metrics account token. Replace <<METRICS-SHIPPING-TOKEN>> with the token of the account you want to ship to. |
| LOGZIO_LISTENER     | Your Logz.io listener address, For example: `https://listener.logz.io:8053`.                                              |
| DOCKER_ENDPOINT     | Address to reach the required Docker (default: `unix:///var/run/docker.sock`)Daemon.                                      |
| COLLECTION_INTERVAL | The interval at which container stats are gathered (default: `30s`).                                                      |
| TIMEOUT             | The request timeout for any Docker Daemon query ( default: `5s`).                                                         |

| EXCLUED_IMAGES | A list of strings, [regexes](https://pkg.go.dev/regexp), or [globs](https://github.com/gobwas/glob) whose referent container image names will not be among the queried containers. !-prefixed negations are possible for all item types to signify that only unmatched container image names should be monitored. For example:`imageNameToExclude1,imageNameToExclude2` ( default: `nil`) |

### Check Logz.io for your metrics

Give your metrics a few minutes to get from your system to ours,
and then open [Logz.io](https://app.logz.io/#/dashboard/metrics).

List of metrics:

<ul>
<li>container_blockio_io_service_bytes_recursive_read</li>
<li>container_blockio_io_service_bytes_recursive_write</li>
<li>container_cpu_percent</li>
<li>container_cpu_throttling_data_periods</li>
<li>container_cpu_throttling_data_throttled_periods</li>
<li>container_cpu_throttling_data_throttled_time</li>
<li>container_cpu_usage_kernelmode</li>
<li>container_cpu_usage_system</li>
<li>container_cpu_usage_total</li>
<li>container_cpu_usage_usermode</li>
<li>container_memory_active_anon</li>
<li>container_memory_active_file</li>
<li>container_memory_anon</li>
<li>container_memory_file</li>
<li>container_memory_file_dirty</li>
<li>container_memory_file_mapped</li>
<li>container_memory_file_writeback</li>
<li>container_memory_inactive_anon</li>
</ul>

Also you can filter by labels:

<ul>
<li>container_hostname</li>
<li>container_id</li>
<li>container_image_name</li>
<li>container_name</li>
</ul>

## Versions

0.1.0:

-   Created Dockerfiles for amd64 and arm64
-   Define config.yaml file

## License

Licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
