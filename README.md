# FreeIPA SSSD Tools

## overview

Repository of useful scripts for FreeIPA and SSSD.

## install

Clone the repository:

```bash

  cd ~
  git clone https://github.com/gcoop-libre/freeipa-sssd-tools

```

Add to ``~/.bashrc``:

```bash

   if [[ -d "$HOME/freeipa-sssd-tools" ]]
   then
       PATH="$HOME/freeipa-sssd-tools:$PATH"
   fi

```

## commands

- ad-sync-sss-cache
- adsearch
- ldbsearch
- log2ad-sync-sss-cache

## License

GNU General Public License, GPLv3.

## Author Information

This repo was created in 2021 by
 [Osiris Alejandro Gomez](https://osiux.com/), worker cooperative of
 [gcoop Cooperativa de Software Libre](https://www.gcoop.coop/).
