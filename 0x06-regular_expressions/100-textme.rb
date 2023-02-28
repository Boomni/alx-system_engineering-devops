#!/usr/bin/env ruby
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
result = matches.join(", ")
puts result
