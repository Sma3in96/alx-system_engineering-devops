#!/usr/bin/env ruby

arg = ARGV[0]

pattern = /hb(t|n)/

matches = arg.scan(pattern)

puts "#{matches.join()}"
