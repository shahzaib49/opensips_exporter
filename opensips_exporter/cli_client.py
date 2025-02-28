from opensipscli import cli

class OpenSIPSClient:
    def __init__(self):
        self.cli = cli.OpenSIPSCLI()

    def get_lb_list(self):
        # returns the LB list as a dict (JSON already parsed)
        return self.cli.mi('lb_list')

    def list_all_profiles(self):
        return self.cli.mi('list_all_profiles')

    def get_profile_size(self, profile):
        # Note: pass profile as a positional parameter if that works
        return self.cli.mi('profile_get_size', [profile])
