# Sky is the limit, let's bring that limit higher
exec { 'update ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
  provider => 'shell',
}

-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
