import os
import json

DATA_DIR = 'data'

def create_or_update_client(name, service):
    client_file = os.path.join(DATA_DIR, f'{name}.json')
    if os.path.exists(client_file):
       
        with open(client_file, 'r') as f:
            client_data = json.load(f)
        client_data['services'].append(service)
        with open(client_file, 'w') as f:
            json.dump(client_data, f)
        print(f'Servicio añadido al cliente {name}')
    else:
      
        client_data = {'name': name, 'services': [service]}
        with open(client_file, 'w') as f:
            json.dump(client_data, f)
        print(f'Nuevo cliente {name} creado')

def get_client_info(name):
    client_file = os.path.join(DATA_DIR, f'{name}.json')
    if os.path.exists(client_file):
        with open(client_file, 'r') as f:
            client_data = json.load(f)
        print(f'Información del cliente {name}:')
        print(client_data)
    else:
        print(f'Cliente {name} no encontrado')

if __name__ == '__main__':
    # Ejemplos de uso
    create_or_update_client('Cliente1', 'Internet')
    create_or_update_client('Cliente2', 'Telefonía')
    get_client_info('Cliente1')
    get_client_info('Cliente3')  # Cliente inexistente
