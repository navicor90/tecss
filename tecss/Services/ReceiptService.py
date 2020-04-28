import csv

def receipt_from_liderpapel_csv(csv_reader):

    order_detail = {'code': 'empty',
                    'reference': 'empty',
                    'description': 'empty',
                    'type': 'empty', # no va
                    'quantity': 'empty',
                    'price': 'empty',
                    'fare': 'empty', # tarifa - Base2
                    'amount': 'empty',
                    'tax': 'empty' #iva
                  }

    order = {'detail': order_detail,
                'subtotal': 'empty',
                'shipping': 'empty',
                'iva_tax': 'empty',
                'net_price': 'empty',
                'order_id': 'empty',
                }

    """
    Subtotal Pedido (2 artículo/s): 25,40
    Gastos de envío y preparación: 0,00
    IVA: 1,78
    Precio Neto Venta: 27,18
    Pedido: 216260
    Usuario: 
    Fecha: 27-04-2020
    Destinatario: Juan Pérez
    Dirección de envío: Agulo
    Código Postal: 38820
    Población: Agulo
    Provincia: Sta.Cruz de Tenerife
    País: España
    Región de envío: No Peninsular
    Forma Pago: Prepago
    Observaciones del comprador : Mar Castilla Pedido
    """

    single_cell_data = {}
    column_data = {}
    number_of_columns_data = 9

    headers = csv_reader.next()
    not_csv_data = headers[number_of_columns_data:-1]
    headers = headers[0:number_of_columns_data]
    for h in headers:
        column_data[h] = []

    for row in csv_reader:
        for i, h in enumerate(headers):
            column_data[h].append(row[i])

    for cell in not_csv_data:
        k, v = cell.split(':')
        single_cell_data[k] = v



    return
def order_from_csv_file(file):
    #encoding = 'latin-1'
    reader = csv.reader(file, delimiter=';')
    receipt_dict = receipt_data_dict(reader)

