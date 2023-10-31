#!/usr/bin/env ruby

arg = ARGV[0]

pattern = /^h\w*n$/

matches = arg.scan(pattern)

puts "#{matches.join()}"
