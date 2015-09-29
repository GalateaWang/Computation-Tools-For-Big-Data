cat $1 | tr $'\n' ' ' | tr '[:blank:]' $'\n' | grep -v '^$' | sort | uniq -c | sort -nr | head -10 | cut -c 9-
