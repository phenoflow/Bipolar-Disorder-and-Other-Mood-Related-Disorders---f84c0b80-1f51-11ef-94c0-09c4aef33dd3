# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"Eu31z","system":"readv2"},{"code":"Eu31y","system":"readv2"},{"code":"Eu319","system":"readv2"},{"code":"Eu317","system":"readv2"},{"code":"Eu316","system":"readv2"},{"code":"E117.","system":"readv2"},{"code":"Eu318","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-and-other-mood-related-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
