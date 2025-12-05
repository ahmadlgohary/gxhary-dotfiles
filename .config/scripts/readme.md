- create cron job
`EDITOR=nvim crontab -e`
`* * * * * ~/.config/scripts/battery_notify.py`

`sudo systemctl start cronie`
`sudo systemctl enable cronie`
