#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def main():

    module = AnsibleModule(
        argument_spec={
            'name': {'type': 'str', 'required': True}
        }
    )

    name = module.params['name']

    module.exit_json(
        changed=False,
        message=f"Hello {name}"
    )

if __name__ == '__main__':
    main()