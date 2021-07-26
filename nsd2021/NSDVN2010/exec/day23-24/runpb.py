from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor

def runpb(host_list,playbooks):
    Options = namedtuple('Options',
                [
                    'connection','remote_user','ask_sudo_pass','verbosity',
                    'module_path','forks','become','become_method','become_user',
                    'check','listhosts','listtasks','listtags','syntax',
                    'sudo_user','sudo','diff'
                ]
    )
    options = Options(
        connection='smart',remote_user='root',ask_sudo_pass=False,verbosity=5,
        module_path=None,forks=5,become=None,become_method=None,become_user=None,
        check=False,listhosts=None,listtasks=None,listtags=None,syntax=None,
        sudo_user=None,sudo=None,diff=False
    )
    loader = DataLoader()
    passwords = dict(vault_pass='123456')
    inventory = InventoryManager(loader=loader,sources=host_list)
    variable_manager = VariableManager(loader=loader,inventory=inventory)
    playbook = PlaybookExecutor(
        playbooks=playbooks,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords
    )
    res = playbook.run()
    return res

if __name__ == '__main__':
    print(runpb(host_list=['myansi/hosts'],playbooks=['myansi/lamp.yaml']))