from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_docker_is_installed(Package):
    pkg = Package('docker-service')
    assert pkg.is_installed


def test_docker_running_and_enabled(Service):
    docker = Service('docker-service')
    assert docker.is_running
    assert docker.is_enabled
