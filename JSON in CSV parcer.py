import json
import csv
import xmltodict

def gen_json():
    with open('webdata/offers0_1.xml') as xml_file:
        my_dict=xmltodict.parse(xml_file.read())
    xml_file.close()

    with open('test.txt', 'w') as outdata:
        json.dump(my_dict, outdata, ensure_ascii=False)
    outdata.close()


def gen_csv():

    with open('test.txt') as json_file:
        data = json.load(json_file)

    ready_to_import = data['КоммерческаяИнформация']["ПакетПредложений"]["Предложения"]["Предложение"]

    data_file = open('data_import.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)

    count = 0

    for dat in ready_to_import: #find out every item in the json (use to transfer Xml into Json)
        if count == 0:
            header = ('Ид', 'Артикул', 'Наименование', 'Склад', 'БазоваяЕдиница', 'Количество', 'Цены', 'Цена')
            csv_writer.writerow(header)
            for dat in ready_to_import:  # find out every item in the json (use to transfer Xml into Json)
                x = dat['Цены']  # find the key
                for key in x.values():  # brut the items in the key
                    key = dict(key)  # swithch str in to dict
                    price = dict(key=key['ЦенаЗаЕдиницу'])
                    count += 1
                    itemsimport = (list(dat.values())+list(price.values()))
                csv_writer.writerow(itemsimport)
    data_file.close()

def main():
    gen_json()
    gen_csv()

if __name__ == '__main__':
    main()