#!/usr/bin/env ruby

require 'open3'

# Set up some constants for the paths to the Figlet and Cowsay commands
FIGLET_PATH = "/usr/bin/figlet"
COWSAY_PATH = "/usr/bin/cowsay"

# Message to print with Cowsay.
Revelation_20_15 = "And if anyone’s name was not found written in this book of life, he was thrown into the lake of fire."

# Set up a regular expression to extract the author name and email address from each log line
AUTHOR_REGEX = /^([^<]+) <([^>]+)>/

# Change to the root directory of the Git repository
Dir.chdir(`git rev-parse --show-toplevel`.chomp)

# Use the Git log command to get the list of authors
authors = `git log --format="%aN <%aE>" | sort -uf`.split("\n")

# Use regular expressions to extract just the names and email addresses from the authors list
names = authors.map { |author| author.match(AUTHOR_REGEX)[1] }
emails = authors.map { |author| author.match(AUTHOR_REGEX)[2] }

# Generate a numbered list of authors
author_list = names.map.with_index { |name, i| "#{i+1}. #{name} <#{emails[i]}>" }

# Use the Figlet command to generate a banner for the script
banner, _ = Open3.capture2(FIGLET_PATH, "-c", "-f", "slant", "AUTHORS")

# Use the Cowsay command to generate a footer-banner for the script
footer, _ = Open3.capture2(COWSAY_PATH, "-f", "turtle", Revelation_20_15)

# Write the authors list to an AUTHORS file in the root of the Git directory
File.open("AUTHORS", "w") do |file|
  # file.write("#{banner}\n\n#{names.join("\n")}\t<#{emails.join("\n")}>\n\n#{footer}")
  file.write("#{banner}\n\n#{author_list.join("\n")}\n\n#{footer}")
end

# Print the banner and the list of authors using Cowsay
puts `echo "#{banner}\n\n#{names.join("\n")}\n\n#{emails.join("\n")}\n\n#{footer}"`
