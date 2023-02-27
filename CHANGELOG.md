# [_FREEIPA-SSSD-TOOLS CHANGELOG_](https://gitlab.com/gcoop-libre/freeipa-sssd-tools.git)

 - this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [`Unreleased - 2023-02-27`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.6.1...develop)

### `CHANGELOG`

- update ChangeLog from v0.5.0 to v0.6.0

### `ipa-sss-dff`

- set V (value) with whitespace when V is empty to fix Markdown syntax

### `ipa-sss-syn`

- replace USERNAME with USERFQDN to prevent errors

### `pre-commit`

- define filetype bash in shell-lint hooks config

## [`v0.6.1 - 2023-02-27`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.6.0...v0.6.1) _fix format date in filter function for ipa-srv-mon.log in ipa-sss-dat_

### `ipa-sss-dat`

- fix format date in filter function for ipa-srv-mon.log

## [`v0.6.0 - 2023-02-13`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.5.1...v0.6.0) _add support to convert datetime to local timezone by default in ipa-sss-syn_

### `CHANGELOG`

- add ChangeLog from v0.1.0 to v0.5.0

### `ipa-src-hlp`

- update commands help with support for local time zone in ipa-sss-syn

### `ipa-sss-syn`

- improve help adding TO_UTC environment variable and datetime conversion example
- show TO_UTC and UTC variables in debug when IPA_SSS_SYN_DEBUG is enabled
- move default TO_UTC=0 from defaults to config function, to allow define TO_UTC in .ipa-config when TO_UTC is not defined as environment variable
- validate LDB_HOST option in config
- return 1970-01-01 00:00 when UNIX time is 0 and use --utc in date convertion using variable UTC define by TO_UTC option
- use 11644473600 as constant to calculate datetime diff between LDAP and UNIX time
- define TO_UTC=0 to convert datetime to local timezone by default

## [`v0.5.1 - 2022-12-22`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.5.0...v0.5.1) _add config function in ipa-srv-mon to read configuration from .ipa-config_

### `ipa-srv-mon`

- add config function to read configuration from .ipa-config

## [`v0.5.0 - 2022-12-19`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.4.0...v0.5.0) _add ipa-sss-ldb to count cache records, add ipa-sss-rsy to backup and ipa-sss-rtr to restore SSSD cache to preserve RAMDISK_

### `ipa-src-hlp`

- update commands help, add ipa-sss-rtr
- update commands help, add ipa-sss-ldb
- update commands help, add ipa-sss-rsy

### `ipa-sss-ldb`

- add script for count records of groups and users in LDB cache

### `ipa-sss-rsy`

- don't sync when LDB_CHK=1 and records count of groups or users are 0
- add script for copy cache files to preserve ramdisk

### `ipa-sss-rtr`

- fix abort when not found groups or users in SSSD cache
- add script for restore backup of cache files to preserve ramdisk

### `README`

- add ipa-sss-rtr in Tools Overview
- add ipa-sss-ldb in Tools Overview
- add ipa-sss-rsy in Tools Overview

## [`v0.4.0 - 2022-11-28`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.3.0...v0.4.0) _update scripts to generate and plot metrics and get and sync users_

### `doc`

- add GNU GENERAL PUBLIC LICENSE Version 3
- add Project Description in .description

### `general`

- shellcheck disable SC1091

### `gitignore`

- add ipa-api-syn configs

### `ipa-src-hlp`

- update commands help
- update ipa-ss-day help with split hour range

### `ipa-sss-all`

- add script for generate and plot metrics in HTML gallery

### `ipa-sss-dat`

- define directory in path of OVW variable

### `ipa-sss-day`

- filter log between hour range with XSTART and XEND variables

### `ipa-sss-plt`

- replace tabs with spaces
- add default umask 0022
- plot labels of slow cron per minute syncs
- plot total per minute labels
- change scale of total syn per minute
- add total syns and hour range in title
- allow to overwrite XSTART with environment variable

### `ipa-sss-syn`

- replace unnecessary assignment with no-op

### `ipa-sss-usr`

- fix invalid log name

### `ipa-usr-all`

- add script for get all users in external LDAP/AD

### `ipa-usr-syn`

- check USERLIST file exists before try delete
- add script for sync all usernames defined in file

### `Makefile`

- passing XSTART and XEND variables to filter hour range with ipa-sss-day
- change default USR from ipaai to root

### `README`

- add ipa-sss-all, ipa-usr-all and ipa-usr-syn in Tools Overview

## [`v0.3.0 - 2022-05-03`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.2.0...v0.3.0) _add API to enqueue cache synchronization requests and process them sequentially_

### `gitignore`

- added compiled python file extension

### `gitlab-ci`

- remove change directory, replace *.py with directory ipa-api-syn
- Added parameter to show errors only
- join ignored-modules lines to prevent whitespace in python-stage
- add flask and flask_restful to ignored-modules in python-stage
- remove scalar before change directory in python-stage
- add && after change directory before execute pylint
- fix change directory before execute pylint en python-stage
- add ignored-modules=api.root,api.sync,api.query in pylint

### `ipa-api-syn`

- Code formated automatically by pyhton-black
- add PyYAML pip dependency in requirements.txt
- add python pip dependencies in requirements.txt
- add python shebang in ipa-que-syn.py
- Added whole freeIPA syncronization API project

### `ipa-api-syn/api/query.py`

- changed get method to accept a new parameter to return the n last records from processed database and return a json list

### `ipa-api-syn/api/sync.py`

- added error message when OperationalError arise

### `ipa-api-syn/app.py`

- Added docstring to fulfill missing docstring pylint message
- change route definitions to include query listing capabilities

### `ipa-api-syn/config_example.yml`

- new parameter to set if priviledge escalation is required to run script

### `ipa-api-syn/__init__.py`

- test_config parameter was not used, use default settings file if none otherwise use the comming from test_config
- Changed comment string to docstring
- initialize API without assigning the object as it's not being used

### `ipa-api-syn/ipa-que-syn`

- Takes script var initialization outside the main loop to fix #7

### `ipa-api-syn/ipa-que-syn.py`

- change import order
- added a howto run example in case script is not call correctly
- added proper command's argument handling
- added stdout and stderr as part of the result string stored in database
- change log to include both stderr and and stdout from executed command
- add sudo to script string when escalate priviledge is true
- get config to escalate privileges

### `ipa-api-syn/uwsgi.py`

- solves syntax error introduced by pylint suggestion
- Solves missing module docstring by adding module documentation
- solves relative import from app as from ipa-api-syn.app
- solves undefined variable appr renaming it as app

### `ipa-que-syn`

- Changed logging format

### `ipa-que-syn-py`

- Changed wait time from 5s to 1s
- Moved sleep time at main while level
- Added IPA_SSS_SYN_SHOW environment variable when calling syn script

### `ipa-que-syn.py`

- Changed wait time from 5s to 1s
- Moved sleep time at main while level
- Added IPA_SSS_SYN_SHOW environment variable when calling syn script
- Added account argument to script call
- Cast script return code to string
- Added a sleep time at the end
- Added more log lines
- Added statement to get return code from subprocess

### `pre-commit`

- improve hooks, add black

### `query.py`

- Added descendent order to get last record
- Added format to timestamps return values
- logging format improvement
- Fix missing query argument as tuple
- Fix missing query argument
- Added missing userid argument
- Solved syntax errors
- Changed logging format
- Added logic to return latest status for a processed account

### `README`

- include README-ipa-api-syn.md
- improve README-ipa-api-syn.md with examples and minor fixes

### `README-ipa-api-syn.md`

- Added result output examples fix #2
- Added small documentation on API ussage

### `settings_example.py`

- added DBPROCS variable to be used on query end-point

### `sync.py`

- Added log message when account cloud no be queued
- Changed the way the endpoint returns operational results to return and error if account were not processed
- Changed logging format
- Added timestamp to log output format

## [`v0.2.0 - 2022-05-02`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/v0.1.0...v0.2.0) _added tools to split, filter, analyze and graph log files_

### `add`

- ipa-sss-plt.cfg with gnuplot styles

### `examples`

- add service metrics in ipa-srv-mon.log
- add report of ipa-sss-syn in markdown

### `gitlab-ci`

- add shellcheck --version
- remove tag shell in shell-check stage to test gitlab-runner
- add tag ansible in shell-check stage to test gitlab-runner

### `ipa-config`

- define DIR_TMP and DIR_PDF
- define PLT_X_TICS_FONT to use in ipa-sss-sum
- define MON_DATE format for ipa-srv-mon
- define common variables for ipa-sss-(dat|plt|htm)
- define HTM variables examples

### `ipa-src-cfg`

- add stderror function
- add function cfg to fail on undefined config variables
- add function config to read config options from .ipa-config
- add Common functions and variables

### `ipa-src-chk`

- add output example
- add Check syntax using shellcheck

### `ipa-src-hlp`

- update commands help
- add commands Help
- add Generate Markdown Help

### `ipa-src-tbl`

- add Generate Markdown Table Overview

### `ipa-sss-chk`

- add Verify Syntax of SynLog

### `ipa-sss-dat`

- add functions params, validate, filter, defaults, srv2dat, log2dat, totals, main and use DIR_DAT
- add Generate .dat file to plot SynLog

### `ipa-sss-day`

- add Split SynLog by date

### `ipa-sss-diff`

- replace empty value with whitespace to prevent markdown format error

### `ipa-sss-hlp`

- sort commands output

### `ipa-sss-log`

- add functions config, params, log2md and main to redirect output to file
- add Generate report of SynLog

### `ipa-sss-plt`

- add functions defaults, params, validate, plot, main and use PLT variables
- add Plot SynLog between hours range

### `ipa-sss-sum`

- add functions defaults, params, validate, sum2dat, dat2plt, main and use PLT variables
- add Plot summarized SynLog attribute stats

### `ipa-sss-usr`

- remove unnecesary output
- add Split SynLog by user

### `Makefile`

- add current directory in execution of ipa-src-chk in chk rule
- add htm rule
- indent defaults variables
- add XSTART and XEND variable with defaults to png rule

### `pre-commit`

- add end-of-file-fixer, trailing-whitespace and shell-lint

### `README`

- add ipa-sss-dff in Tools Overview
- add ipa-srv-mon in tools overview
- add ipa-sss-htm in Tools Overview
- add Tools Overview with link to ipa-src-hlp.md

## [`v0.1.0 - 2022-05-02`](https://gitlab.com/gcoop-libre/freeipa-sssd-tools/-/compare/7506d8d...v0.1.0) _first public version of ipa-sss-syn_

### `config`

- add ipa-config.example

### `ipa-sss-syn`

- refactor general

### `pre-commit`

- add shell-lint

### `README`

- fix typo in gcoop-libre.freeipa_sssd_tools repositories

