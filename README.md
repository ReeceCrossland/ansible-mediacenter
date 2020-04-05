# media-ansible
This is to aid in the healthchecking and building of a media center environment. Currently very basic, hoping to give more flexible options relating to multi-server setups.

# What's included?
This installs the following software:

- Plex - Mediacenter
- Ombi - Manage adding film/tv
- Sonarr - TV show management
- Radarr - Film management
- Nginx - Web server
- Sabnzbd - NZB download management

# vars
The following variables can be passed:   
`httpauth_pass` - *required* raw input string - used to generate the httpauth for Nginx   
`plex_url` - *required* raw input string - your Plex URL, inclusive of preferred protocol, such as `https://`   
`plex_token` - *required* raw input string - Plex token    
`movie_library_id` - *required* int - Find your movie library ID so collections images can be automatically searched for (Plex generated ones look so bad)    

# Compatibility
It seems to work well for me on CentOS 7 ¯\\\_(ツ)\_/¯

# Requirements
Testing requires Molecule V2.* for now due to linting changes on 3.* and I'm too lazy to update

# CI Status
![Media-Ansible Molecule Tests](https://github.com/ReeceCrossland/media-ansible/workflows/Media-Ansible%20Molecule%20Tests/badge.svg?branch=master)
