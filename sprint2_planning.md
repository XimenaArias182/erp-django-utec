# Sprint 2 Planning — ERP Django
## Semanas W07–W09 · Espiral 3: CRUD Web y Autenticación

**Sprint Goal:**
Al finalizar el Sprint 2, el ERP mostrará lista y detalle de las entidades principales, con formularios de alta/edición/borrado protegidos por autenticación y 3 roles de acceso.

## HUs seleccionadas
| ID | Historia | Puntos | Semana |
|---|---|---|---|
| HU-E3-01 | Ver lista de productos | 2 | W07 |
| HU-E3-02 | Ver detalle de un producto | 2 | W07 |
| HU-E3-03 | Ver listas de clientes y proveedores | 2 | W07 |
| HU-E3-04 | Ver detalle de ventas con sus líneas | 3 | W07 |

## DoD — Sprint 2
- ListView responde HTTP 200 y muestra objetos de la BD
- DetailView responde 200 con datos correctos y 404 para IDs inexistentes
- python manage.py test tests → ≥ 78 tests OK