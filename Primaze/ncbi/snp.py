from logging import debug, show, temp, error  # type: ignore
from decouple import config  # type: ignore
from time import process_time

from urllib.error import HTTPError
import xml.etree.ElementTree as ET
from Bio import Entrez  # type: ignore


Entrez.email = config("EMAIL")


class SNP:
    def __init__(self, snp_id, name=""):
        self.id = snp_id
        self.name = name
        self.raw_data = self.get_snp_data()
        self.data = self.process_snp_data()
        debug(self)

    def __repr__(self):
        return "SNP<{}@{}>".format(self.data["name"], self.data["chrpos"])

    def get_snp_data(self):
        """ get a numeric id of the snp and return a parsed xml file """
        stime = process_time()
        try:
            response = Entrez.efetch(db="SNP", id=self.id, retmode="flt").read()
        except HTTPError as err:
            error(
                "{}. SNP with the given id was not found.\n\t\tThis could be due to a lack of internet connection.".format(
                    err
                )
            )
            exit(1)
        etime = process_time()
        show("SNP Data Downloaded in: {:.2}ms".format((etime - stime) * 1000))

        self.raw_data = ET.fromstring(response)  # print(self.raw_data)
        return self.raw_data

    def process_snp_data(self):
        """ get parsed xml data -> output a well defined dict with key snp info """
        # stime = process_time()
        _snp_info = dict()
        _snp_info["id"] = self.raw_data.find("SNP_ID").text

        genes = self.raw_data.find("GENES")
        _snp_info["genes"] = list()
        for gene in genes:
            name = gene.find("NAME").text
            gene_id = gene.find("GENE_ID").text
            _snp_info["genes"].append({"name": name, "id": gene_id})

        _snp_info["chr"] = self.raw_data.find("CHR").text
        _snp_info["chrpos"] = self.raw_data.find("CHRPOS").text
        _snp_info["created_date"] = self.raw_data.find("CREATEDATE").text.split(" ")[0]
        _snp_info["updated_date"] = self.raw_data.find("UPDATEDATE").text.split(" ")[0]
        _snp_info["class"] = self.raw_data.find("SNP_CLASS").text
        _snp_info["docsum"] = self.raw_data.find("DOCSUM").text
        _snp_info["validated"] = self.raw_data.find("VALIDATED").text.split(",")
        _snp_info["fxn_class"] = self.raw_data.find("FXN_CLASS").text

        global_mafs = self.raw_data.find("GLOBAL_MAFS")
        mafs = global_mafs.findall("MAF")

        # pprint(mafs)
        # <MAF>
        #     <STUDY>GENOME_DK</STUDY>
        #     <FREQ>C=0.475/19</FREQ>
        # </MAF>
        _snp_info["freq"] = list()
        for maf in mafs:
            # print("{}: {}".format(maf.find('STUDY').text, maf.find('FREQ').text))
            study_name = maf.find("STUDY").text
            data = maf.find("FREQ").text.split("=")
            dominant_allele = data[0]
            rest_data = data[1].split("/")
            freq = rest_data[0]
            sample_size = rest_data[1]

            _snp_info["freq"].append(
                {
                    "study_name": study_name,
                    "freq": freq,
                    "dominant_allele": dominant_allele,
                    "sample_size": sample_size,
                }
            )

        if len(_snp_info["genes"]) >= 1:
            gene = _snp_info["genes"][0]
            name = "{}_{}".format(gene["name"], gene["id"])
        else:
            name = _snp_info["id"]
        _snp_info["name"] = name if self.name == "" else self.name

        # pprint(_snp_info)

        # etime = process_time()
        # print("SNP Data Processed in: {:.2}ms".format((etime - stime)*1000))

        return _snp_info


# if __name__ == '__main__':
#     # stime = process_time()
#     root = get_snp_data(3057)
#     snp_info = process_snp_data(root)
