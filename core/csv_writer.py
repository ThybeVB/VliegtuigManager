import locale, csv

class CsvWriter:
    def generate_csv(self, full_flight_list, include_all_fields=True):
        
        locale.setlocale(locale.LC_ALL, 'nl_BE.UTF-8')
        try:
            with open('Vluchten.csv', 'w', newline='') as invoice_file:
                writer = csv.writer(invoice_file)
                header = ["IATA Code", "Vliegt vanuit", "Vliegt naar", "Tijdstip"]
                if include_all_fields:
                    header.extend(["Vliegtuig", "Type", "Luchtmaatschappij"])

                writer.writerow(header)

                for flight in full_flight_list:
                    flight_record = [flight[1], flight[2], flight[3], flight[4]]
                    if include_all_fields:
                        flight_record.extend([flight[6], flight[7], flight[8]])

                    writer.writerow(flight_record)
        except Exception as e:
            print("Fout bij wegschrijven: ", e)