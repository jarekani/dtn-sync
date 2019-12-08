import random
import string
import subprocess
import os

def generate_random_name(length = 8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def get_tmp_folder():
    dir = os.path.join("/tmp", generate_random_name())
    os.mkdir(dir)

    return dir

def get_tmp_file():
    folder = get_tmp_folder()
    return os.path.join(folder, generate_random_name())

def run_command(command, input=None, env_vars = []):
    for env in env_vars:
        name, value = env
        os.environ[name] = value

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    if input is not None:
        process.stdin.write(input)

    std, stderr = process.communicate()

    process.stdin.close()

    for env in env_vars:
        name, value = env
        os.environ[name] = ""

    if stderr:
        raise Exception(stderr)

    return std

def get_file_checksum(file):
    output = run_command(["sha1sum", "-b", file])

    # Remove file-name from the output
    return output[0:40]

def get_node_name():
    return "TODO"

def generate_dtn_config(interfaces):
    f = open(os.path.abspath(os.path.dirname(__file__)) + "/dtn.conf", "w+")
    counter = 0
    interfaces_list = "net_interfaces ="
    for interface in interfaces:
        f.write("net_lan" + str(counter) + "_interface = " + interface + "\n")
        interfaces_list = interfaces_list + " lan" + str(counter)
        counter = counter + 1

    f.write(interfaces_list + "\n")
    f.write("routing = epidemic\n")
    f.close()
