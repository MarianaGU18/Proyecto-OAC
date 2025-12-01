# 📌 Suma de valores negativos en bytes

Este proyecto implementa la suma de valores negativos almacenados en una lista de bytes (0x00–0xFF).  
La lógica se desarrolla en dos entornos:

| Componente | Función |
|----------|---------|
| `suma_negativos.py` | Procesa una lista `U` y suma solo los valores negativos interpretados en complemento a 8 bits |
| `mem_program.mif`   | Versión equivalente para ser cargada como memoria en una FPGA mediante Quartus |

