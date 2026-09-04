#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import subprocess

def main():

    module = AnsibleModule(argument_spec={})

    uptime = subprocess.check_output(
        "uptime -p",
        shell=True
    ).decode().strip()

    module.exit_json(
        changed=False,
        uptime=uptime
    )

if __name__ == '__main__':
    main()#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import subprocess

def main():

    module = AnsibleModule(argument_spec={})

    uptime = subprocess.check_output(
        "uptime -p",
        shell=True
    ).decode().strip()

    module.exit_json(
        changed=False,
        uptime=uptime
    )

if __name__ == '__main__':
    main()