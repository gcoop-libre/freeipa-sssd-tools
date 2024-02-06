# _FreeIPA SSSD Tools_

| _date_     | _tag_      | _description_                                                                                                                                                                                                                                                                  |
|------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2024-02-06 | `  v0.9.1` | add ipa-hlt-chk and ipa-hlt-gui to check Network, DNS, NTP, SSSD, KRB5 and others dependencies to determine health of IPA                                                                                                                                                      |
| 2023-06-28 | `  v0.9.0` | add ipa-sss-err for filter SynLog of sAMAccountName with at least one sync error (error!=0), add ipa-sss-exp for filter SynLog when record date match with accountExpires date and add ipa-sss-nsy for filter SynLog of sAMAccountName with at least one no sync (sss_cache=0) |
| 2023-04-25 | `  v0.8.0` | add /resyn in ipa-api-syn to run ipa-sss-syn with IPA_SSS_SYN_LAST=1 to skip error=2 validation                                                                                                                                                                                |
| 2023-04-05 | `  v0.7.3` | ipa-sss-plt: plot syn errors with error code in label                                                                                                                                                                                                                          |
| 2023-03-07 | `  v0.7.2` | replace date -d with date $UTC and accountExpires=0 or dataExpireTimestamp=1 with 1970-01-01 00:00 in ipa-sss-syn                                                                                                                                                              |
| 2023-03-07 | `  v0.7.1` | force invalidate cache when dataExpireTimestamp <= NOW in ipa-sss-syn                                                                                                                                                                                                          |
| 2023-03-06 | `  v0.7.0` | report errors (40,41,42,43) when failed syn and add wait after invalidate and populate (Default 0s) in ipa-sss-syn                                                                                                                                                             |
| 2023-02-27 | `  v0.6.1` | fix format date in filter function for ipa-srv-mon.log in ipa-sss-dat                                                                                                                                                                                                          |
| 2023-02-13 | `  v0.6.0` | add support to convert datetime to local timezone by default in ipa-sss-syn                                                                                                                                                                                                    |
| 2022-12-22 | `  v0.5.1` | add config function in ipa-srv-mon to read configuration from .ipa-config                                                                                                                                                                                                      |
| 2022-12-19 | `  v0.5.0` | add ipa-sss-ldb to count cache records, add ipa-sss-rsy to backup and ipa-sss-rtr to restore SSSD cache to preserve RAMDISK                                                                                                                                                    |
| 2022-11-28 | `  v0.4.0` | update scripts to generate and plot metrics and get and sync users                                                                                                                                                                                                             |
| 2022-05-03 | `  v0.3.0` | add API to enqueue cache synchronization requests and process them sequentially                                                                                                                                                                                                |
| 2022-05-02 | `  v0.2.0` | added tools to split, filter, analyze and graph log files                                                                                                                                                                                                                      |
| 2022-05-02 | `  v0.1.0` | first public version of ipa-sss-syn                                                                                                                                                                                                                                            |

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
| `ipa-sss-ldb` | IPA SSSD cache count records                       |
| `ipa-sss-log` | Generate report of SynLog                          |
| `ipa-sss-plt` | Plot SynLog between hours range                    |
| `ipa-sss-rsy` | IPA SSSD copy cache files to preserve RAMDISK      |
| `ipa-sss-rtr` | Restore SSSD cache files to preserve RAMDISK       |
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
- https://gitlab.com/osiux/ansible_role_freeipa_sssd_tools
- https://github.com/gcoop-libre/ansible_role_freeipa_sssd_tools
- https://github.com/osiris/ansible_role_freeipa_sssd_tools
- https://codeberg.org/osiux/ansible_role_freeipa_sssd_tools

## License

GNU General Public License, GPLv3.

## Author Information

This repo was created in 2021 by
 [Osiris Alejandro Gomez](https://osiux.com/), worker cooperative of
 [gcoop Cooperativa de Software Libre](https://www.gcoop.coop/).
