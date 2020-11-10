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
        if self.start_tag == self.end_tag and config("GENO_FOLD_IDENTIFIER") in data:
            data = data.replace("/", "")
            if "p" in data.split(".")[-1]:
                self.data.append(data)

    def get_parsed_list(self, data: str) -> List[str]:
        self.feed(data)
        return self.data  # print((self.data))


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


get_ch_num = lambda file_name: file_name.split("_genomic")[0].split("p")[-1]


def file_name_from_url(url: str) -> str:
    _ = url.split("//")[1].split("/")
    file_name = _[-1]  # print(file_name)
    return file_name


def dir_name_from_url(url: str) -> str:
    _ = url.split("//")[1].split("/")
    del _[0]
    del _[-1]
    dir_name = "/".join(_) + "/"  # print(dir_name)
    return dir_name


def ftp_url_split(url: str) -> Tuple[str, str, str]:
    file_name = file_name_from_url(url)
    dir_name = dir_name_from_url(url)
    ch_num = get_ch_num(file_name)
    return (dir_name, file_name, ch_num)


ftp_url = lambda urls: urls[0].split("//")[1].split("/")[0]


def download_file_from_ftp(
    ftp_url: str, data_folder: str, dir_name: str, file_name: str
) -> None:
    # https://titanwolf.org/Network/Articles/Article?AID=a5c53dad-13fb-40dc-a0dd-faed9011d054#gsc.tab=0
    with FTP(ftp_url) as ftp:
        ftp.login(passwd=config("EMAIL"))
        ftp.cwd(dir_name)  # ftp.dir()

        with open(data_folder + file_name, "wb") as d:
            ftp.voidcmd("TYPE I")
            total = ftp.size(file_name)  # print(size(total))
            with tqdm(
                total=total,
                # unit_scale=True,
                # leave=True,
            ) as pbar:

                def cb(data):
                    pbar.update(len(data))
                    d.write(data)

                ftp.retrbinary("RETR {}".format(file_name), cb)


print_download_title = lambda i, urls, file_name: print(
    "{}/{} [{:.0f}%]: {}".format(i + 1, len(urls), (i + 1) / len(urls) * 100, file_name)
)


def download(urls: List[str]) -> None:
    assert isinstance(urls, list)  # print(urls)

    _ftp_url = ftp_url(urls)  # print(_ftp_url)

    for i, url in enumerate(urls):
        (dir, file_name, chnum) = ftp_url_split(url)

        data_folder = config("DATA_FOLDER")
        assert data_folder is not None
        # assert

        print_download_title(i, urls, file_name)
        try:
            if file_name in listdir(data_folder):
                print("Already exists")
                # TODO: checksum verification
                break
            else:
                download_file_from_ftp(_ftp_url, data_folder, dir, file_name)
                # TODO: checksum verification
                # print("Checking Checksum...")
        except (error_temp, error_reply) as e:
            print(e)
            exit(1)


chromosomes_urls = list(
    map(chromosome_download_url, get_chromosome_names(chromosome_url))
)


download(chromosomes_urls)


def all_chromosomes_present():
    # TODO: check if all chromosomes are present
    pass


def read_fasta(ch_num: int):  # Use context manager
    # TODO: unzip chromosome files
    pass


def fasta_value_at_loaction(ch_num: int, index: int) -> str:
    pass


def check_value_at_location(ch_num: int, index: int, value: str) -> bool:
    # fasta_value_at_loaction()
    # TODO: check snp location
    pass


def get_neighbors(ch_num: int, index: int, range: int) -> List[str]:
    # TODO: get neighbouring region
    pass
