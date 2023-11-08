# Puppet file to fix wordpress server

exec {'fix wordpress':
  command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php'
}
