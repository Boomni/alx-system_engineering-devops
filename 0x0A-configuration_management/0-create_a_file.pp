# Using Puppet, create a file in /tmp

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

