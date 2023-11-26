# -*- coding: utf-8 -*-

import sqlite3
import re
from datetime import datetime


def remove_codigos_cor(texto):
    # Remove códigos de cor ANSI
    return re.sub(r'\033\[[0-9;]+m', '', texto)


def formatar_data(data):
    if isinstance(data, datetime):
        return data.strftime('%d-%m-%Y %H:%M:%S')
    return data


def visualizar_dados():
    conn = sqlite3.connect('ficha_paciente.db')
    cursor = conn.cursor()

    # Recupera todos os registros da tabela
    cursor.execute('SELECT * FROM ficha_paciente')
    registros = cursor.fetchall()

    # Mostra os registros em grupos de 10
    for i in range(0, len(registros), 10):
        grupo_registros = registros[i:i + 10]
        for registro in grupo_registros:
            # Remove códigos de cor e formata as datas antes de imprimir
            registro_sem_cor = [remove_codigos_cor(str(formatar_data(coluna))) for coluna in registro]
            print(registro_sem_cor)

        # Pausa para permitir a visualização no console
        input("Pressione Enter para mostrar mais registros...")

    conn.close()


# Chama a função para visualizar dados
visualizar_dados()
