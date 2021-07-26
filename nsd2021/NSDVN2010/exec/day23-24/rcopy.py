from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(
            src = dict(required=True,type='str'),
            dest = dict(required=True,type='str')
        )
    )
    shutil.copy(module.params['src'],module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()