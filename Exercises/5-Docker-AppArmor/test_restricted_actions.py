
import docker

client = docker.from_env()

container = client.containers.get("flask-apparmor-test")

# Test reading a sensitive file
exit_code, output = container.exec_run(
    ["cat", "/etc/passwd"]
)
print("Read /etc/passwd:")
print("Exit code:", exit_code)
print(output.decode(errors="replace"))

# Test executing a shell
exit_code, output = container.exec_run(
    ["/bin/sh", "-c", "echo Shell execution successful"]
)
print("\nShell execution test:")
print("Exit code:", exit_code)
print(output.decode(errors="replace"))
