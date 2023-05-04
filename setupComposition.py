import subprocess

subprocess.run(['docker-compose', '-f', 'balcony-garden-docker-composition.yml', 'up', '-d'], check=True)