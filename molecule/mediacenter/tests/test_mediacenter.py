import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


class TestMediaCenter:
    def test_nginx_process_started(self, host):
        nginx = host.process.filter(comm='nginx')
        assert len(nginx) > 0

    def test_plex_process_started(self, host):
        plex = host.process.filter(comm='Plex')
        assert len(plex) >= 1

    def test_ombi_process_started(self, host):
        ombi = host.process.filter(comm='Ombi')
        assert len(ombi) > 0

    def test_mono_process_started(self, host):
        mono = host.process.filter(comm='mono')
        assert len(mono) > 0

    def test_tautulli_usenet_process_started(self, host):
        tautulli_usenet = host.process.filter(comm='python')
        assert len(tautulli_usenet) >= 2
