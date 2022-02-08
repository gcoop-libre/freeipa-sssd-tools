SHELL:=/bin/bash

DAY  ?= $$(date +'%F')
LOG  ?= ipa-sss-syn.log
USR  ?= ipaai

plt: log dat png

log:
	ipa-sss-day $(LOG) $(DAY)
	ipa-sss-usr $(LOG) $(DAY)

sum:
	ipa-sss-sum userAccountControl $(USR)-$(DAY)-$(LOG)
	ipa-sss-sum accountExpired     $(USR)-$(DAY)-$(LOG)
	ipa-sss-sum pwdExpired         $(USR)-$(DAY)-$(LOG)
	ipa-sss-sum sss_cache          $(USR)-$(DAY)-$(LOG)

dat:
	ipa-sss-dat $(USR)-$(DAY)-$(LOG) $(DAY)

png:
	ipa-sss-plt $(DAY)

hlp:
	ipa-src-hlp >ipa-src-hlp.md

chk:
	@ipa-src-chk

dev: chk hlp
