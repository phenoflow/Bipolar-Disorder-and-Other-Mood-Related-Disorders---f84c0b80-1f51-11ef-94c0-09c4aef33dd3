# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"E111.","system":"readv2"},{"code":"E1114","system":"readv2"},{"code":"E1111","system":"readv2"},{"code":"E11y1","system":"readv2"},{"code":"E114.","system":"readv2"},{"code":"Eu311","system":"readv2"},{"code":"E11y0","system":"readv2"},{"code":"E1145","system":"readv2"},{"code":"E1113","system":"readv2"},{"code":"E1101","system":"readv2"},{"code":"E1112","system":"readv2"},{"code":"E1146","system":"readv2"},{"code":"E1142","system":"readv2"},{"code":"E1105","system":"readv2"},{"code":"Eu30.","system":"readv2"},{"code":"E1116","system":"readv2"},{"code":"E1144","system":"readv2"},{"code":"E1110","system":"readv2"},{"code":"E111z","system":"readv2"},{"code":"E1102","system":"readv2"},{"code":"E114z","system":"readv2"},{"code":"E1115","system":"readv2"},{"code":"E1104","system":"readv2"},{"code":"Eu30y","system":"readv2"},{"code":"Eu300","system":"readv2"},{"code":"E110.","system":"readv2"},{"code":"Eu310","system":"readv2"},{"code":"E1103","system":"readv2"},{"code":"Eu30z","system":"readv2"},{"code":"E11y.","system":"readv2"},{"code":"146D.","system":"readv2"},{"code":"E1141","system":"readv2"},{"code":"E1143","system":"readv2"},{"code":"E1100","system":"readv2"},{"code":"Eu312","system":"readv2"},{"code":"E1140","system":"readv2"},{"code":"E1106","system":"readv2"},{"code":"E110z","system":"readv2"},{"code":"Eu301","system":"readv2"},{"code":"F31.0","system":"readv2"},{"code":"F31.2","system":"readv2"},{"code":"F31.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-and-other-mood-related-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
