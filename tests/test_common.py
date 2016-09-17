from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_apt_transport_https_is_installed(Package):
    pkg = Package('apt-transport-https')
    assert pkg.is_installed


def test_ca_certificates_is_installed(Package):
    pkg = Package('ca-certificates')
    assert pkg.is_installed


def test_tree_is_installed(Package):
    pkg = Package('tree')
    assert pkg.is_installed


def test_pwgen_is_installed(Package):
    pkg = Package('pwgen')
    assert pkg.is_installed


def test_git_is_installed(Package):
    pkg = Package('git')
    assert pkg.is_installed


def test_htop_is_installed(Package):
    pkg = Package('htop')
    assert pkg.is_installed


def test_python_is_installed(Package):
    pkg = Package('python')
    assert pkg.is_installed


def test_python_pip_is_installed(Package):
    pkg = Package('python-pip')
    assert pkg.is_installed
