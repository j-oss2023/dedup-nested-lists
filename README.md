# Ansible Filter Plugin for Deduplicating Nested Lists

This Ansible filter plugin provides a straightforward way to deduplicate nested lists within dictionaries, preserving the order of elements. It's particularly useful in scenarios where your playbook generates lists with potential duplicates and you need a clean, unique list for further operations.

## Requirements

- Ansible 2.9 or later (though it might work with earlier versions, it has only been tested on Ansible 2.9+).

## Installation

To use this filter plugin, you need to copy it into your Ansible filter plugins directory. If you're not sure where to place it, you can define a custom directory for filter plugins in your `ansible.cfg` file:

```ini
[defaults]
filter_plugins = ./path/to/your/filter_plugins
```

Then, copy the `deduplicate_nested_lists.py` file (assuming this is the name of the file containing the provided code) into this directory.

## Usage

Once installed, the filter can be applied in your playbooks or roles to dictionaries containing lists that you want to deduplicate. Here's a simple example of how to use it:

```yaml
---
- name: Deduplicate nested lists example
  hosts: localhost
  gather_facts: no
  vars:
    sample_data:
      key1: [1, 2, 2, 3]
      key2: ["a", "a", "b", "c", "c"]
  tasks:
    - name: Deduplicate lists in a dictionary
      debug:
        msg: "{{ sample_data | dedup_nested_lists }}"
```

This will output:

```yaml
ok: [localhost] => {
    "msg": {
        "key1": [1, 2, 3],
        "key2": ["a", "b", "c"]
    }
}
```

## How It Works

The `dedup_nested_lists` filter takes a dictionary as input. Each key in the dictionary should have a list as its value. The filter then iterates over each list, removing any duplicate entries while preserving the original order of the elements. If the input is not a dictionary or if any value within the dictionary is not a list, the filter will raise an `AnsibleFilterError`.

## Contributing

Contributions to improve `dedup-nested-lists` are welcome. Please ensure to follow best practices and open a pull request for any enhancements.


## Acknowledgments

A humble thank you to all contributors and users of this plugin for your support and feedback.
