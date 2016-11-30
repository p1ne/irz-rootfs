#!/bin/sh /usr/lib/irz-web/setscript
F=/mnt/rwfs/settings/settings.gre
. $F
echo "<pre>"
for i in `seq 1 10`; do
    i_=$(printf '%02d' $i)
    enabled_now=$(isOn `formq gre${i_}_enabled`)
    eval was_enabled=\$GRE${i_}_ENABLED
    setValue $F GRE${i_}_ENABLED $enabled_now
    echo "was_enabled=$was_enabled, enabled_now=$enabled_now"
    [ $was_enabled = "1" -a $enabled_now = "0" ] && \
        /etc/init.d/gre stop ${i_}
    [ $was_enabled = "0" -a $enabled_now = "1" ] && \
        /etc/init.d/gre start ${i_}
done

echo "</pre><hr><a href=\"config_gre.cgi\">Return</a>"
~
