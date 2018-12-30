# Docker Compose Expand  [![PyPi version](https://img.shields.io/pypi/v/docker-compose-expand.svg)](https://pypi.python.org/pypi/docker-compose-expand/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/docker-compose-expand.svg)](https://pypi.python.org/pypi/docker-compose-expand/)  [![](https://img.shields.io/github/license/f9n/docker-compose-expand.svg)](https://github.com/f9n/docker-compose-expand/blob/master/LICENSE)








Expand your docker-compose.yml file with this tool.

# Install

```bash
$ pip3 install --user docker-compose-expand
```

# Usage

Your services in `docker-compose.yml` file.

```yaml
version: "3"
services:
  api:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9001:9001"

  products:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9002:9001"

  analysis:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9003:9001"

  monitoring:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9004:9001"
```

Instead of using the `docker-compose` tool, define the same services in the `docker-compose-expand.yml` file and use the `docker-compose-expand` tool that generates the `docker-compose.yml` file for your expandable services.

- You can define variables in `loop` field or `vars` field.

- In the `loop` field, you can refer to a variable which is in the `vars` field.

### Loop Field

```yaml
version: "3"
services:
  api:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9001:9001"

expand:
  vars:
  services:
    - name: "{{ name }}"
      service:
        image: ef9n/supervisord:0.1.0
        restart: on-failure
        volumes:
          - "/tmp/{{ name }}/:/opt/{{name}}/"
        ports:
          - "{{ port }}:9001"
      loop:
        - name: products
          port: 9002
        - name: analysis
          port: 9003
        - name: monitoring
          port: 9004
```

### Vars Field

```yaml
# Vars Field
version: "3"
services:
  api:
    image: ef9n/supervisord:0.1.0
    restart: on-failure
    ports:
      - "9001:9001"

expand:
  vars:
    supervisors:
      - name: products
        port: 9002
      - name: analysis
        port: 9003
      - name: monitoring
        port: 9004
  services:
    - name: "{{ name }}"
      service:
        image: ef9n/supervisord:0.1.0
        restart: on-failure
        volumes:
          - "/tmp/{{ name }}/:/opt/{{name}}/"
        ports:
          - "{{ port }}:9001"
      loop: "{{ supervisors }}"
```

# Examples

Look up the [examples](https://github.com/f9n/docker-compose-expand/tree/master/examples) directory.

# Credits

- [Docker Compose](https://github.com/docker/compose)
- [Ansible Yaml Standard](https://github.com/ansible/ansible)
