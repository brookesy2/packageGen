import mappingHelper
import scandir
from lxml import etree
from collections import defaultdict
import click


# Boring ole object to hold some details
class MetadataType(object):
    filename = ""
    xmlname = ""


#Create something way over complicated to get all the files and their xmlname mappings
def create_filelist(path):
    #Scan the main dir to find the folders in it
    directorymapping = mappingHelper.directorymapping()
    directories = []
    for entry in scandir.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir() and entry.name in mappingHelper.directorynames():
            directories.append(entry)

    #Scan each of the dirs found from the main dir
    directorydict = {}
    for directory in directories:
        directorydict[directory.name] = scandir.scandir(directory.path)

    #Create a dict and fill it with directories and metadata objects
    filesdict = defaultdict(list)
    for directory, directorydetails in directorydict.items():
        for x in directorydetails:
            try:
                suffixname = x.name.split('.')[1]
            except:
                suffixname = None
                print("Suffix not found or no suffix for {}, more than likely something folder based like reports".format(x.name))
            if suffixname in mappingHelper.suffixnames():
                filemeta = MetadataType()
                filemeta.filename = x.name.split('.')[0]
                filemeta.xmlname = directorymapping.get(directory)
                filesdict[directorymapping.get(directory)].append(filemeta)

    return filesdict


#Create the package file.
def create_package(files):
    #create package.xml
    packageNS = "http://soap.sforce.com/2006/04/metadata"
    packageNsmap = {None: packageNS}
    package = etree.Element("Package", nsmap=packageNsmap)

    for k, v in files.items():
        types = etree.SubElement(package, "types")

        for row in v:
            members = etree.SubElement(types, "members")
            members.text = row.filename

        name = etree.SubElement(types, "name")
        name.text = k

    version = etree.SubElement(package, "version")
    version.text = "27.0"

    packageXML = etree.ElementTree(package)
    #print(etree.tostring(packageXML, encoding='utf8', method='xml'))
    packageXML.write("package.xml", pretty_print=True, xml_declaration=True)


@click.command()
@click.option('--path', default='.', help='Path of the directory to scan')
def run(path):
    files = create_filelist(path)
    create_package(files)


if __name__ == '__main__':
    run()


