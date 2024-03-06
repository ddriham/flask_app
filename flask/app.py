from flask import Flask
import docker

app = Flask(__name__)


docker_client = docker.from_env()

@app.route('/')
def list_running_containers():
    containers = docker_client.containers.list()
    containers_names = [container.name for container in containers]
    return '<br>'.join(containers_names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
