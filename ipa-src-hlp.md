---
fontsize: 8pt
code-block-font-size: 8pt
classoption: landscape
---

# `ipa src` commands


## `ipa-src-cfg` Common functions and variables

### Usage

```bash

  ipa-src-cfg

```

### Description

Common functions and variables for FreeIPA SSSD Tools scripts.


## `ipa-src-chk` Check syntax using shellcheck

### Usage

```bash

  ipa-src-chk

```

### Description

Check syntax using shellcheck.

### Examples

```bash

  ipa-src-chk

    1 ipa-sss-htm SC2034
    1 ipa-sss-plt SC2034 SC2119 SC2120

```


## `ipa-src-hlp` Generate Markdown Help

### Usage

```bash

  ipa-src-hlp

```

### Description

Generate a markdown output for usage of each command script.


## `ipa-src-tbl` Generate Markdown Table Overview

### Usage

```bash

  ipa-src-tbl

```

### Description

Generate a markdown table output for each command script.


# `ipa srv` commands


## `ipa-srv-mon` Capture metrics of IPA process

### Usage:

```bash

  ipa-srv-mon

```

### Description

Capture metrics of IPA process using pgrep, netstat and lsof

- LDAP simultaneous connections (port 389)
- LDAP SSL Simultaneous connections (port 636)
- KRB5 simultaneous connections (port 88)
- All TCP simultaneous connections
- kdcproxy simultaneous process
- dirsrv simultaneous process
- pkiuser simultaneous process
- simultaneous Open Files
- Host Average

### Example:

```bash

	ipa-srv-mon
  2022-02-13_16:01 389:4 636:20 88:0 ALL:28 KDCP:2 DSRV:1 PKIU:1 LSOF:1807 AVG:average: 0,08, 0,08, 0,05

```


# `ipa sss` commands


## `ipa-sss-all` Generate and plot metrics in HTML gallery

### Usage

```bash

  ipa-sss-all [IPA_SSS_SYN_LOG] [YYYY-MM-DD]

```

### Description

Split `ipa-sss-syn.log` by date, generate `.dat` files, plot
between hours range and generate _HTML_ gallery of SynLog Plots Images.

### Example

```bash

  ipa-sss-all

  /var/www/html/syn/img/2022-11-14-seconds-vs-total-vs-ips-0700-1900.png
  /var/www/html/syn/index.html

```


## `ipa-sss-chk` Verify Syntax of SynLog

### Usage

```bash

  ipa-sss-chk [IPA_SSS_SYN_LOG] [IPA_SSS_CHK_LOG]

```

### Description

Verify syntax of `ipa-sss-syn.log`, output check in `ipa-sss-chk.log`

### Examples

```bash

	ipa-sss-chk ipa-sss-syn.log

	LINE=0000207 COLUMN=11 INVALID lastLogon= NOT MATCH lastLogon=2021-10-21

```


## `ipa-sss-dat` Generate .dat file to plot SynLog

### Usage

```bash

  ipa-sss-dat [IPA_SSS_SYN_LOG] [DATE]

```

### Description

Generate data file from `ipa-sss-syn.log` to generate plot

### Examples

```bash

	ipa-sss-dat ipa-sss-syn.log

	ipa-sss-dat ipaai-2022-02-22-ipa-sss-syn.log 2022-02-22

```


## `ipa-sss-day` Split SynLog by date

### Usage

```bash

  ipa-sss-day [IPA_SSS_SYN_LOG] [YYYY-MM-DD]

```

### Description

Split `ipa-sss-syn.log` by date.

### Examples

Example split all days:

```bash

  ipa-sss-day ipa-sss-syn.log

      3866 2021-11-24-ipa-sss-syn.log
      4060 2021-11-25-ipa-sss-syn.log
      4041 2021-11-26-ipa-sss-syn.log
      3865 2021-11-27-ipa-sss-syn.log
      3865 2021-11-28-ipa-sss-syn.log
      4424 2021-11-29-ipa-sss-syn.log
      4088 2021-11-30-ipa-sss-syn.log

```

Example split specific day:

```bash

  ipa-sss-day ipa-sss-syn.log 2022-01-01

      3861 2022-01-01-ipa-sss-syn.log

```

Example split specific day between hour range:

```bash

  XSTART=10:00 XEND=18:00 ipa-sss-day ipa-sss-syn.log 2022-01-01

      2861 2022-01-01-ipa-sss-syn.log

```

## `ipa-sss-dff` show attributes differences between sync requests from log

### Usage:

```bash

  ipa-sss-dff [IPA_SSS_SYN_LOG]

```

### Description

Show attributes differences between user sync requests from log

Attributes list:

```

	user
	sAMAccountName
	lockoutTime
	pwdLastSet
	pwdExpireDate
	pwdExpireDays
	pwdExpired
	physicalDeliveryOfficeName
	lastLogon
	userAccountControl
	adUserAccountControl
	accountExpires
	accountExpireDays
	accountExpired
	adAccountExpires
	dataExpireTimestamp
	sss_cache
	newDataExpireTimestamp
	newAdUserAccountControl
	newAdAccountExpires
	error
	seconds

```

### Example:

```bash

	ipa-sss-dff

```

See full example output in [`ipa-sss-dff.md`](examples/ipa-sss-dff.md)
and [`ipa-sss-dff.pdf`](examples/ipa-sss-dff.pdf)


## `ipa-sss-htm` Generate HTML gallery of SynLog Plots Images

### Usage

```bash

  ipa-sss-htm

```

### Description

Generate HTML gallery of SynLog Plots Images


## `ipa-sss-ldb` IPA SSSD cache count records

### Usage

```bash

  ipa-sss-ldb [groups|users]

```

### Description

Execute `ldapsearch` in `/var/lib/sss/db/cache_DOMAIN.ldb` to get
total records of groups and users.

### Example

```bash

  ipa-sss-ldb

   55 cn=groups,cn=example.com,cn=sysdb
    1 cn=users,cn=example.com,cn=sysdb

```


## `ipa-sss-log` Generate report of SynLog

### Usage

```bash

  ipa-sss-log [IPA_SSS_SYN_LOG] [YYYY-MM-DD] [REGEX_EXCLUDE]

```

### Generate stats report from `ipa-sss-syn.log`

### Examples

```bash

	ipa-sss-log ipa-sss-syn.log

```

See full example output in [ipa-sss-syn.md](examples/ipa-sss-syn.md) and
[ipa-sss-syn.pdf](examples/ipa-sss-syn.pdf)


## `ipa-sss-plt` Plot SynLog between hours range

### Usage:

```bash

  ipa-sss-plt [YYYY-MM-DD] [X_START] [X_END]

```

### Description

Plot SynLog Stats:

- LDAP Simultaneous Connections
- KRB5 Simultaneous Connections
- Average Host
- Total SYNs
- SYNs > 20s
- SYNs < 20s
- No-SYNs

### Example:

```bash

  ipa-sss-plt 2022-01-01 07:00 19:00

```

See full example output in [`ipa-sss-plt.md`](examples/ipa-sss-plt.md)
and [`ipa-sss-plt.pdf`](examples/ipa-sss-plt.pdf)


## `ipa-sss-rsy` IPA SSSD copy cache files to preserve RAMDISK

### Usage

```bash

  ipa-sss-rsy [SSS_BAK]

```

### Description

  Copy SSSD cache files in /var/lib/sss/db to preserver hAMDISK.

### Example

```bash

  ipa-sss-rsy

```


## `ipa-sss-sum` Plot summarized SynLog attribute stats

### Usage

```bash

  ipa-sss-sum [LOG_ATTRIBUTE] [IPA_SSS_SYN_LOG]

```

### Description

Plot log attribute stats.

### Example

```bash

	ipa-sss-sum userAccountControl

```


## `ipa-sss-syn` IPA SSSD Synchronize Cache

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


## `ipa-sss-usr` Split SynLog by user

### Usage

```bash

  ipa-sss-usr [IPA_SSS_SYN_LOG] [YYY-MM-DD]

```

### Description

Split `ipa-sss-syn.log` by user.

### Examples

```bash

  ipa-sss-usr ipa-sss-syn.log root

```


# `ipa usr` commands


## `ipa-usr-all` IPA SSSD get all users

### Usage

```bash

  ipa-usr-all

```

### Description

  Search `sAMAccountName` of all users in external
  _LDAP/ActiveDirectory_

### Example

```bash

  ipa-usr-all

```

### Standard Output

```

	1234
	5678
	admin

```

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
  LDAP_SEARCH_USERS: OU=users,DC=addomain,DC=com
  LDAP_EXCLUDE_USERS: '[A-Z\-]+'
  LDAP_USER: admin@addomain.com
  # LDB
  IPA_DOMAIN: ipa.addomain.com
  LDB_FILTER: (objectCategory=user)
  LDB_HOST: /var/lib/sss/db/cache_ipa.addomain.com.ldb
  MAX_PWD_AGE: 30

```


## `ipa-usr-syn` IPA SSSD syn all usernames defined in file

### Usage

```bash

  ipa-usr-syn

```

### Description

  Execute ipa-sss-syn for all usernames defined in file.

### Example

```bash

  ipa-usr-syn

```

### Standard Output

```

	1234
	5678
	admin

```

