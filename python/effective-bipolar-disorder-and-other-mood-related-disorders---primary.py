# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"E1161","system":"readv2"},{"code":"E1172","system":"readv2"},{"code":"E117z","system":"readv2"},{"code":"E1176","system":"readv2"},{"code":"Eu31.","system":"readv2"},{"code":"E116z","system":"readv2"},{"code":"E1170","system":"readv2"},{"code":"E1162","system":"readv2"},{"code":"E1171","system":"readv2"},{"code":"E1160","system":"readv2"},{"code":"E116.","system":"readv2"},{"code":"E1166","system":"readv2"},{"code":"F31.8","system":"readv2"},{"code":"F31.6","system":"readv2"},{"code":"F31","system":"readv2"},{"code":"F31.9","system":"readv2"},{"code":"F31.7","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-disorder-and-other-mood-related-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["effective-bipolar-disorder-and-other-mood-related-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["effective-bipolar-disorder-and-other-mood-related-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["effective-bipolar-disorder-and-other-mood-related-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
