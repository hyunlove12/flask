from textMining.model import SamsungReport

if __name__ == '__main__':
    #f = SamsungReport.read_file()
    sam = SamsungReport()
    # sam.download()
    #print(sam.extract_noun())
    print(sam.remove_stopword())