# irz-rootfs
Changes to root filesystem of IRZ RUH2b router

В данном репозитории лежат изменения rootfs к промышленному 3G роутеру IRZ RUH2b. Цель изменений - добавить в роутер поддержку WiFi

Прошивка, взятая за основу, лежит тут: http://www.radiofid.ru/upload/files/routers/irz_ruh/RUH2b.master.update.2014-10-28_17-17-43.bin

Использовалась информация из BitBucket-репозитория компании Радиофид: https://bitbucket.org/radiofid/

тулчейн: https://bitbucket.org/radiofid/irz-rxx-toolchain

ядро 4.4: https://bitbucket.org/radiofid/linux-radiofid/branch/irz-4.4.x

информация по прошивке через Serial интерфейс "Восстановление прошивки роутера (для версий HW 2.0, A1)" со страницы https://www.radiofid.ru/catalog/besprovodnaya-svyaz/routery/3g-routery/router-irz-ruh2b-hsupa-hsdpa-umts-edge-gprs-3g/

Прямая ссылка на документ по прошивке https://www.radiofid.ru/upload/docs/routers/irz_ruh/RUH2b-old_RestoreFW_RU.zip

А также информация, полученная от технической поддержки Радиофид.

Файлы конфигурации kernel, buildroot, инструкции по сборке и патчи к апстрим софту лежат в репозитории https://github.com/p1ne/irz-devel

Готовые прошивки и описание процедуры прошивки в репозитории https://github.com/p1ne/irz-firmware

*ВНИМАНИЕ* Поскольку у новой прошивки другое распределение разделов на flash-памяти, прошивка из Web-интерфейса успехом не увенчается. Шить надо через Serial-интерфейс по процедуре, описанной по ссылке "Восстановление прошивки роутера" при помощи USB-UART адаптера и самодельного кабеля. Годится любой USB-UART, проверялось на чипах CP210x и клоне FT232.

Из ограничений которые сейчас есть в данной сборке
- у меня wifi модуль RTL8188EU, на него и закладывался, поэтому ядро собрано только с ним
- для RTL чипов нужна отдельная ветка hostapd, поэтому в силу ограничений железа собрана только она
- аутентификация только WPA/WPA2 PSK, остальное не нужно лично мне, но можно попробовать сделать
- иногда при соединении с hostapd не проходит аутентификация, разбираюсь в данный момент. Проблема на форумах встречается
- из-за перехода на 4.4.x полностью выключен conntrack из соответствующего скрипта, сейчас в процессе сборки conntrack-tools
- все wifi-утилиты собираются вне buildroot костылями, прикручивание внутрь buildroot в планах

Wifi работает в трех режимах
- AP - роутер выступает в роли точки доступа и раздает инет через встроенную симку на eth0
- CLIENT - роутер соединяется к другой точке доступа и раздает ее инет на eth0
- AUTO - роутер стартует в режиме AP, раз в минуту сканируется эфир на наличие точки доступа с заданным SSID/BSSID и при ее наличии переключается в режим CLIENT. При ее пропадании переключается обратно в режим AP. Сейчас не реализовано переключение обратно при невозможности аутентификации на точке.
