
import docker

client = docker.from_env()

# Check whether the image exists
image = client.images.get("flask-apparmor")
print("Image found:", image.tags)

# Inspect the existing container
try:
    container = client.containers.get("flask-apparmor-test")
    info = client.api.inspect_container(container.id)

    print("Container:", container.name)
    print("Status:", info["State"]["Status"])
    print("Security options:", info["HostConfig"]["SecurityOpt"])
    print("AppArmor profile:", info["AppArmorProfile"])

except docker.errors.DockerException as e:
    print("Docker error:", e)
