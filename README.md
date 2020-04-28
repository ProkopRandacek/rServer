# rServer
My custom webserver software

# Setup
To install the server, simply clone this repository and install the dependencies (in `program/` do `pip install -r requirements.txt`)
To run the server run the `main.py` file in `program/` (You need to be in the same folder as `main.py` when you are running the server becatuse all the paths are by default relative)

# Configuration

Note: `content/`, `assets/` and `config/` dont need to be used. You can have all in one folder or whatever. All the paths to all files are set in `rules` or `config.json` files. If you want to change the `config/config.json` file location. You need to change the `configPath` variable in `program/config.py`

## `content/`
Contains all pure content files (for example the text on your home page)

## `assets/`
Contains all resources needed by pages (css, fonts, icons, images, ...)

## `config/`
Contains following files:

- `conf.json` file with general server settings
  - `address` = the address server is running on
  - `port` = the port server should listen on (80 for http, 443 for https)
  - `findFile` = Not implemented yet
  - `debug` = show debug messages
  - `path` paths to:
    - `root` = root folder of your files (is used at beginig of every other path)
    - `templete` = your template html
    - `certfile` = certfile for https
    - `keyfile` = your keyfile for https
    - `notfound` = your 404 page
    - `contentTypes` = your content types rules
    - `rules` = your rules file
    - `navbar` = your navbar rules file
    - `log` = log file FIXME
  - `log`
    - `timepre` = string that is put before the time on output
    - `timepos` = string that is but after the time on output
    - `separator` = string that is used for separating parts of output messages
    - `saveToFile` = wheter or not the program should write log to log file
- `contentTypes`
  - contains rules for what content type headers to send for what file extensions see example for syntax explanation (`text/plain` is used by default)
- `rules`
  - contains rules for what request should return what files
- `navbar`
  - contains rules for navbar generation (see example)

[My configuration](https://github.com/prokoprandacek/randacek.dev)

### Todo
- Scan for new pages on startup
- add pages to rules somehow automaticaly
- Better separate example config files and the program
- Even more user friendly
- Add code description for easy modifications
- implement that "304 Not Modified" thing
