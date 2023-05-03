# Install Nginx and configure custom HTTP header response

class { 'nginx':
  ensure => 'installed',
}

nginx::resource::server { 'default':
  listen_port => 80,
  locations   => {
    '/redirect_me' => {
      'return' => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4',
    },
  },
  add_header  => {
    'X-Served-By' => '$hostname',
  },
}
