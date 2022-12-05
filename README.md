# _FreeIPA_ _SSSD_ Tools

[[_TOC_]]

## `ipa-api-syn` _API_ to synchronize _FreeIPA_ cache

See API Help in [`README-ipa-api-syn.md`](README-ipa-api-syn.md)

## Tools Overview

Repository of useful scripts for _FreeIPA_ and _SSSD_.

| script        | description                                        |
|---------------|----------------------------------------------------|
| `ipa-src-cfg` | Common functions and variables                     |
| `ipa-src-chk` | Check syntax using shellcheck                      |
| `ipa-src-hlp` | Generate Markdown Help                             |
| `ipa-src-tbl` | Generate Markdown Table Overview                   |
| `ipa-srv-mon` | Capture metrics of IPA process                     |
| `ipa-sss-all` | Generate and plot metrics in HTML gallery          |
| `ipa-sss-chk` | Verify Syntax of SynLog                            |
| `ipa-sss-dat` | Generate .dat file to plot SynLog                  |
| `ipa-sss-day` | Split SynLog by date                               |
| `ipa-sss-dff` | show attributes differences between sync requests from log |
| `ipa-sss-htm` | Generate HTML gallery of SynLog Plots Images       |
| `ipa-sss-log` | Generate report of SynLog                          |
| `ipa-sss-plt` | Plot SynLog between hours range                    |
| `ipa-sss-rsy` | IPA SSSD copy cache files to preserve RAMDISK      |
| `ipa-sss-sum` | Plot summarized SynLog attribute stats             |
| `ipa-sss-syn` | IPA SSSD Synchronize Cache                         |
| `ipa-sss-usr` | Split SynLog by user                               |
| `ipa-usr-all` | IPA SSSD get all users                             |
| `ipa-usr-syn` | IPA SSSD syn all usernames defined in file         |

See IPA tools source Help in [`ipa-src-hlp.md`](ipa-src-hlp.md)

## Install

### Manual

Clone the repository:

```bash

  cd /opt
  git clone https://gitlab.com/gcoop-libre/freeipa-sssd-tools

```

Add to ``/root/.bashrc``:

```bash

   if [[ -d "/opt/freeipa-sssd-tools" ]]
   then
       PATH="/opt/freeipa-sssd-tools:$PATH"
   fi

```

### Ansible/AWX

Use `gcoop-libre.freeipa_sssd_tools` from:

- https://gitlab.com/gcoop-libre/ansible_role_freeipa_sssd_tools
- https://github.com/gcoop-libre/ansible_role_freeipa_sssd_tools

## License

GNU General Public License, GPLv3.

## Author Information

This repo was created in 2021 by
 [Osiris Alejandro Gomez](https://osiux.com/), worker cooperative of
 [gcoop Cooperativa de Software Libre](https://www.gcoop.coop/).
