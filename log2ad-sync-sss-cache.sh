#!/bin/bash

BIN="$(basename "$0")"
AD_SYNC_CACHE_SSS='ad-sync-cache-sss'
LASTTIMELOG='last_time.log'
LOGFILE="$(date '+%Y-%m-%d').log"

[[ -z "$1" ]] || LOGFILE="$1"
[[ -e "$1" ]] || exit 1

run_script () {
  NOW="$(date +'%F %T')"
  printf "%s %s sAMAccountName: %s " "$NOW" "$BIN" "$1"
  $AD_SYNC_CACHE_SSS "$1"
}

run_script_upd_time () {
  run_script "$1"
  printf "LastTimeLog: %s\\n" "$2"
  sed -ie "s/^$1\\s.*/$1 $2/g" $LASTTIMELOG
}

run_script_apnd_time () {
  run_script "$1"
  printf "LastTimeLog: %s\\n" "$2"
  echo "$1 $2" >> $LASTTIMELOG
}

sed -i 's/\[//g' "$LOGFILE"
sed -i 's/\]//g' "$LOGFILE"

sort -nrk3 "$LOGFILE"  \
  | awk -F: '!x[$2]++' \
  | tr ':' ' '         \
  | tr '-' ':'         \
  | while read -r TIME ACCOUNT _
do

touch "$LASTTIMELOG"
LAST_TIME="$(awk "/$ACCOUNT/ {print \$2}" "$LASTTIMELOG")"

if [[ -n "$TIME" ]]
then
	if [[ -n "$LAST_TIME" ]]
	then
		[[ $(date -d "$TIME" '+%H%M%S') -gt $(date -d "$LAST_TIME" '+%H%M%S') ]] && run_script_upd_time "$ACCOUNT" "$TIME"
	else
	  run_script_apnd_time "$ACCOUNT" "$TIME"
	fi
fi

done
