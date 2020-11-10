#!../venv/bin/python
from typing import List, Set, Dict, Tuple, Optional, Callable
import requests
from html.parser import HTMLParser
from ftplib import FTP, error_temp, error_reply
from tqdm import tqdm
from collections import namedtuple
from hurry.filesize import size
from os import listdir
from os.path import isfile, join
from decouple import config


class NcbiFtpHTMLParser(HTMLParser):
    start_tag: str = ""
    end_tag: str = ""
    data: List[str] = []

    def handle_starttag(self, tag, attrs):
        self.start_tag = tag

    def handle_endtag(self, tag):
        self.end_tag = tag

    def handle_data(self, data):
        if (
            self.start_tag == self.end_tag and config("GENO_FOLD_IDENTIFIER") in data
        ):  # HARDCODED
            data = data.replace("/", "")
            if "p" in data.split(".")[-1]:
                self.data.append(data)

    def get_parsed_list(self, data: str) -> List[str]:
        self.feed(data)
        return self.data
        # print((self.data))


chromosome_url = config("CHROMOSOME_URL")
chromosome_download_url = (
    lambda name: chromosome_url + name + "/" + name + config("FASTA_EXT")
)


def get_chromosome_names(url: str) -> List[str]:
    r = requests.get(url)
    assert r.status_code == 200, "Internet connection failed."
    assert (
        r.headers["content-type"] == "text/html;charset=UTF-8"
    ), "Response is not html."

    parser = NcbiFtpHTMLParser()
    return parser.get_parsed_list(r.text)


def download(urls: List[str]) -> None:
    assert isinstance(urls, list)
    # print(urls)

    ftp_url = urls[0].split("//")[1].split("/")[0]
    print(ftp_url)

    def url_split(url: str) -> Tuple[str, str]:
        _ = url.split("//")[1].split("/")
        del _[0]
        file_name = _[-1]
        # print(file_name)

        del _[-1]
        dir = "/".join(_) + "/"
        # print(dir)
        return (dir, file_name)

    for i, url in enumerate(urls):
        dir = url_split(url)[0]
        file_name = url_split(url)[1]

        print(
            "{}/{} [{:.0f}%]: {}".format(
                i + 1, len(urls), (i + 1) / len(urls) * 100, file_name
            )
        )
        try:
            with FTP(ftp_url) as ftp:
                ftp.login(passwd=config("EMAIL"))
                ftp.cwd(dir)
                # ftp.dir()

                data_folder = config("DATA_FOLDER")
                if file_name in listdir(data_folder):
                    print("Already exists")
                else:
                    with open(data_folder + file_name, "wb") as d:
                        ftp.voidcmd(
                            "TYPE I"
                        )  # https://titanwolf.org/Network/Articles/Article?AID=a5c53dad-13fb-40dc-a0dd-faed9011d054#gsc.tab=0
                        total = ftp.size(file_name)
                        # print(size(total))
                        with tqdm(
                            total=total,
                            unit_scale=True,
                            miniters=1,
                            leave=True,
                        ) as pbar:

                            def cb(data):
                                pbar.update(len(data))
                                d.write(data)

                            ftp.retrbinary("RETR {}".format(file_name), cb)
        except (error_temp, error_reply) as e:
            print(e)
            exit(1)


chromosomes_urls = list(
    map(chromosome_download_url, get_chromosome_names(chromosome_url))
)


download(chromosomes_urls)


# TODO: checksum verification
# TODO: check if all chromosomes are present
# TODO: unzip chromosome files
# TODO: check snp location
# TODO: get neighbouring region
