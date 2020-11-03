from Bio import Entrez
from decouple import config
from time import process_time
import xml.etree.ElementTree as ET
from urllib.error import HTTPError

Entrez.email = config('EMAIL')


def get_snp_data(snp_id):
    """ get a numeric id of the snp and return a parsed xml file """
    stime = process_time()
    try:
        response = Entrez.efetch(db='SNP', id=snp_id, retmode='flt').read()
    except HTTPError as err:
        print("{}. SNP with the given id was not found.\n\t\tThis could be due to a lack of internet connection.".format(err))
        exit(1)
    etime = process_time()
    print("SNP Data Downloaded in: {:.2}ms".format((etime - stime)*1000))

    parsed_data = ET.fromstring(response)
    # print(parsed_data)
    return parsed_data


def process_snp_data(parsed_data, name=""):
    """ get parsed xml data -> output a well defined dict with key snp info """
    stime = process_time()
    _snp_info = dict()
    _snp_info['id'] = parsed_data.find('SNP_ID').text

    genes = parsed_data.find('GENES')
    _snp_info['genes'] = list()
    for gene in genes:
        name = gene.find('NAME').text
        gene_id = gene.find('GENE_ID').text
        _snp_info['genes'].append({ 'name': name, 'id': gene_id })

    _snp_info['chr'] = parsed_data.find('CHR').text
    _snp_info['chrpos'] = parsed_data.find('CHRPOS').text
    _snp_info['created_date'] = parsed_data.find('CREATEDATE').text.split(' ')[0]
    _snp_info['updated_date'] = parsed_data.find('UPDATEDATE').text.split(' ')[0]
    _snp_info['class'] = parsed_data.find('SNP_CLASS').text
    _snp_info['docsum'] = parsed_data.find('DOCSUM').text
    _snp_info['validated'] = parsed_data.find('VALIDATED').text.split(',')
    _snp_info['fxn_class'] = parsed_data.find('FXN_CLASS').text

    global_mafs = parsed_data.find('GLOBAL_MAFS')
    mafs = global_mafs.findall('MAF')

    from pprint import pprint

    # pprint(mafs)
    # <MAF>
    #     <STUDY>GENOME_DK</STUDY>
    #     <FREQ>C=0.475/19</FREQ>
    # </MAF>
    _snp_info['freq'] = list()
    for maf in mafs:
        # print("{}: {}".format(maf.find('STUDY').text, maf.find('FREQ').text))
        study_name = maf.find('STUDY').text
        data = maf.find('FREQ').text.split('=')
        dominant_allele = data[0]
        rest_data = data[1].split('/')
        freq = rest_data[0]
        sample_size = rest_data[1]

        _snp_info['freq'].append({
            'study_name': study_name, 
            'freq': freq, 
            'dominant_allele': dominant_allele, 
            'sample_size': sample_size
            })

    if len(_snp_info['genes']) >= 1:
        gene = _snp_info['genes'][0]
        name = "{}_{}".format(gene['name'], gene['id'])
    else:
        name = _snp_info['id']
    _snp_info['name'] = name if name == "" else name

    pprint(_snp_info)

    etime = process_time()
    print("SNP Data Processed in: {:.2}ms".format((etime - stime)*1000))

    return _snp_info


if __name__ == '__main__':
    root = get_snp_data(3057)
    # snp_info = process_snp_data(root, "Pitch Perception")
    snp_info = process_snp_data(root)