# Script de Auditoría Forense: Cálculo de Similitud de Jaccard entre Código GPL y Salida de IA

def jaccard_similarity(str1, str2):
    # Convertir textos a conjuntos de tokens (palabras / palabras clave)
    set1 = set(str1.split())
    set2 = set(str2.split())
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    return len(intersection) / len(union) if len(union) > 0 else 0

# 1. Código Original bajo Licencia GPL (Caso Quake III Arena)
codigo_gpl = """
// Fast Inverse Square Root - Quake III Arena (Licensed under GNU GPL v2)
float Q_rsqrt( float number ) {
    long i;
    float x2, y;
    const float threehalfs = 1.5F;
    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;
    i  = 0x5f3759df - ( i >> 1 );
    y  = * ( float * ) &i;
    y  = y * ( threehalfs - ( x2 * y * y ) );
    return y;
}
"""

# 2. Salida Generada por la IA (Mutilando la cabecera de la licencia GPL)
codigo_ia = """
float Q_rsqrt( float number ) {
    long i;
    float x2, y;
    const float threehalfs = 1.5F;
    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;
    i  = 0x5f3759df - ( i >> 1 );
    y  = * ( float * ) &i;
    y  = y * ( threehalfs - ( x2 * y * y ) );
    return y;
}
"""

# Cálculo Cuantitativo
similitud = jaccard_similarity(codigo_gpl, codigo_ia)
print(f"--- RESULTADO DE LA AUDITORÍA FORENSE ---")
print(f"Similitud de Jaccard calculada: {similitud * 100:.2f}%")
print("Conclusión: Existe duplicación literal del algoritmo con omisión de la Licencia GPL.")
