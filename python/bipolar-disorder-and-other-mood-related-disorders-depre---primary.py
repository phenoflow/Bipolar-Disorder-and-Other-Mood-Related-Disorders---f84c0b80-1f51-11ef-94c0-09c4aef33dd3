# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"E1150","system":"readv2"},{"code":"E1151","system":"readv2"},{"code":"E1154","system":"readv2"},{"code":"E11y3","system":"readv2"},{"code":"Eu313","system":"readv2"},{"code":"E11y2","system":"readv2"},{"code":"E1155","system":"readv2"},{"code":"E115.","system":"readv2"},{"code":"E1152","system":"readv2"},{"code":"E1156","system":"readv2"},{"code":"Eu314","system":"readv2"},{"code":"Eu315","system":"readv2"},{"code":"E11yz","system":"readv2"},{"code":"E115z","system":"readv2"},{"code":"E1153","system":"readv2"},{"code":"F31.3","system":"readv2"},{"code":"F31.5","system":"readv2"},{"code":"F31.4","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-and-other-mood-related-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bipolar-disorder-and-other-mood-related-disorders-depre---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bipolar-disorder-and-other-mood-related-disorders-depre---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bipolar-disorder-and-other-mood-related-disorders-depre---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
