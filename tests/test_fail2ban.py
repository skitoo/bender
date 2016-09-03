from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_fail2ban_is_installed(Package):
    pkg = Package('fail2ban')
    assert pkg.is_installed


def test_fail2ban_running_and_enabled(Service):
    fail2ban = Service('fail2ban')
    assert fail2ban.is_running
    assert fail2ban.is_enabled
