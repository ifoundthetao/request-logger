from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import argparse
import time


sites_set = set([])

def interceptor(request):
    parsed_uri = urlparse(request.url)
    site_to_add = f"{parsed_uri.scheme}://{parsed_uri.netloc}"
    sites_set.add(site_to_add)


def main(page, is_quiet, wait_time=1):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    webdriver_service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(
            service=webdriver_service, 
            options = chrome_options, 
            )
    driver.request_interceptor = interceptor

    driver.get(page)
    time.sleep(wait_time)

    # Totally not necessary, as we are using a gross global. But it's conveying intent
    return sites_set
                    


parser = argparse.ArgumentParser()
parser.add_argument("page", help="Web Page to check")
parser.add_argument("-o", "--output", help="Write to a findings to a file.")
parser.add_argument("-q", "--quiet", help="Suppress all output", action="store_true")
parser.add_argument("-s", "--sort", help="Sorts output alphabetically", action="store_true")
parser.add_argument("-w", "--wait", help="Time to wait for page load. Defaults to 1 second.", type=int, default=1)

args = parser.parse_args()

if __name__ == '__main__':
    page = args.page
    is_sorted = args.sort
    is_quiet = args.quiet
    is_file_save = True if args.output else False
    wait_time = args.wait

    domain_list = main(page=page, is_quiet=is_quiet, wait_time=wait_time)

    if is_sorted:
        domain_list = sorted(domain_list)

    if is_file_save:
        output_file_name = args.output
        output_file_handle = open(args.output, "w+")

    for domain in domain_list:
        if is_file_save:
            output_file_handle.write(f"{domain}\n")
        if not is_quiet:
            print(domain)

    if is_file_save:
        output_file_handle.close()
