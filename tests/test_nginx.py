from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_nginx_is_installed(Package):
    pkg = Package('nginx')
    assert pkg.is_installed


def test_nginx_running_and_enabled(Service):
    nginx = Service('nginx')
    assert nginx.is_running
    assert nginx.is_enabled
