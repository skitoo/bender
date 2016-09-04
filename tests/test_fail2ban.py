from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_fail2ban_is_installed(Package):
    pkg = Package('fail2ban')
    assert pkg.is_installed


def test_fail2ban_running_and_enabled(Service):
    fail2ban = Service('fail2ban')
    assert fail2ban.is_running
    assert fail2ban.is_enabled


def test_jail_local_file_exists(File):
    assert File('/etc/fail2ban/jail.local').exists


def test_nginx_badbots_file_exists(File):
    assert File('/etc/fail2ban/filter.d/nginx-badbots.conf').exists


def test_nginx_nohome_file_exists(File):
    assert File('/etc/fail2ban/filter.d/nginx-nohome.conf').exists


def test_nginx_noproxy_file_exists(File):
    assert File('/etc/fail2ban/filter.d/nginx-noproxy.conf').exists


def test_nginx_noscript_file_exists(File):
    assert File('/etc/fail2ban/filter.d/nginx-noscript.conf').exists
