# Request Logger

Request Logger will use Selenium to load up a webpage, and it will log all domains which are accessible that requests are made to.

Tool is useful for getting an initial foothold of what requests are being made from a page.
You can then use that information to continue to spider and build out more surface area of connections.

# Usage Instructions

    usage: request-logger.py [-h] [-r] [-o OUTPUT] [-q] [-w WAIT] page
    
    positional arguments:
      page                  Web Page to check
    
    optional arguments:
      -h, --help            show this help message and exit
      -s, --sort            Sorts output alphabetically
      -o OUTPUT, --output OUTPUT
                            Write to a findings to a file.
      -q, --quiet           Suppress all output
      -w WAIT, --wait WAIT  Time to wait for page load. Defaults to 1 second.
