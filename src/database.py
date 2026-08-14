# Etapa 0.1 de la base de datos de prueba.

# Simulacion de base de datos. Reglas de reetiquetado.
# Diccionario que mapea el codigo original con el esperado

# Diccionario base
PRODUCT_RULES = {
    "8802021105304": {
        "sku": "CREMA-ANTIEDAD-50ML",
        "name": "Crema Facial Antiedad 50ml",
        "expected_new_ean": "8802021105304",
        "client": "Cliente Cosméticos SA"
    },
    "7809876543210": {
        "sku": "PERFUME-ROSE-100ML",
        "name": "Perfume Rose Edition 100ml",
        "expected_new_ean": "7801111222233",
        "client": "Cliente Perfumes Global"
    }
}

# Función que retorna el codigo esperado comprobando si existe o no en las reglas
def get_product_rule(ean_code: str):
    return PRODUCT_RULES.get(ean_code, None);
