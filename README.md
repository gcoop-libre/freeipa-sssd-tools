# _FreeIPA_ _SSSD_ Tools

## Overview

Repository of useful scripts for _FreeIPA_ and _SSSD_.

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

- https://gitlab.com/gcoop-libre/ansible_freeipa_sssd_tools
- https://github.com/gcoop-libre/ansible_freeipa_sssd_tools

## `ipa-sss-syn` _IPA_ _SSSD_ Synchronize Cache

### Usage

```bash

  [IPA_SSS_SYN_SHOW=1] [IPA_SSS_SYN_DEBUG=1] ipa-sss-syn sAMAccountName

```

### Description

  Search `sAMAccountName` attributes in external
  _LDAP/ActiveDirectory_ and _SSSD_ local cache and
  force synchronization (require SUDO or root) comparing
  `userAccountControl` with `adUserAccountControl` and
  `accountExpires` with `adAccountExpires`.

### Example

```bash

  ipa-sss-syn admin

```

### Standard Output

```

  2021-11-25
  09:49
  user                       root
  sAMAccountName             admin
  lockoutTime                1970-01-01T00:00
  pwdLastSet                 2021-11-23T12:51
  pwdExpireDate              2021-12-23
  pwdExpireDays              27
  pwdExpired                 0
  physicalDeliveryOfficeName 12345678
  lastLogon                  2021-11-25
  userAccountControl         512
  adUserAccountControl       512
  accountExpires             1970-01-01T00:00
  accountExpiresDays         0
  accountExpired             0
  adAccountExpires           1970-01-01T00:00
  dataExpireTimestamp        2021-11-25T18:37
  sss_cache                  0
  newDataExpireTimestamp     2021-11-25T18:37
  newAdUserAccountControl    512
  newAdAccountExpires        1970-01-01T00:00
  error                      0
  seconds                    1

```

### Debug Output

```

  physicalDeliveryOfficeName 12345678
  userAccountControl         512
  lastLogon                  2021-11-25       11:50 (132823146503300910)
  pwdLastSet                 2021-11-23       12:51 (132821454705963591)
  accountExpires             1970-01-01       00:00 (0)
  lockoutTime                1970-01-01       00:00 (0)
  adUserAccountControl       512
  adAccountExpires           1970-01-01       00:00 (0)
  dataExpireTimestamp        2021-11-25       18:37 (1637865468)
  sAMAccountName             admin
  AD_LCK                     1970-01-01T00:00
  AD_PWD                     2021-11-23T12:51
  AD_UAC                     512
  SS_UAC                     512
  AD_EXP                     1970-01-01T00:00
  SS_DEX                     2021-11-25T18:37
  SS_SEC                     1637865420
  EXPIRE                     0

```

### Environment Variables

  `IPA_SSS_SYN_DEBUG=(0|1) Default: 0`

    Show or hide debug variables, ldapsearch and ldbsearch output.

  `IPA_SSS_SYN_SHOW=(0|1)  Default: 1`

    Show or hide output log.

  `IPA_SSS_SYN_PIVOT=(0|1) Default: 1`

    Enable to show in two columns format or Disable to show one line.

### Config Example

  Write config in `~/.ipa-config`:

```

  # LDAP/AD
  LDAP_BIND_DN: OU=users,DC=addomain,DC=com
  LDAP_DOMAIN: addomain.com
  LDAP_HOST: 10.0.0.1:389
  LDAP_LDIF_WRAP: no
  LDAP_NET_TIMEOUT: 5
  LDAP_PASS: 53cr37
  LDAP_SCOPE: sub
  LDAP_SEARCH_BASE: OU=users,DC=addomain,DC=com
  LDAP_USER: admin@addomain.com
  # LDB
  IPA_DOMAIN: ipa.addomain.com
  LDB_FILTER: (objectCategory=user)
  LDB_HOST: /var/lib/sss/db/cache_ipa.addomain.com.ldb
  MAX_PWD_AGE: 30

```

## License

GNU General Public License, GPLv3.

## Author Information

This repo was created in 2021 by
 [Osiris Alejandro Gomez](https://osiux.com/), worker cooperative of
 [gcoop Cooperativa de Software Libre](https://www.gcoop.coop/).
