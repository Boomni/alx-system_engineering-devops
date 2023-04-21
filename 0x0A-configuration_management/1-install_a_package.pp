# Using puppet to install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
