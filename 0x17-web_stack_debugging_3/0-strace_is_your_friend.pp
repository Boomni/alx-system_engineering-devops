# Puppet manifest to fix Apache 500 error

# Install Apache package
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Fix Apache configuration
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => present,
  mode    => '0644',
  content => "
<VirtualHost *:80>
  ServerAdmin webmaster@localhost
  DocumentRoot /var/www/html

  <Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
",
  notify  => Service['apache2'],
}

