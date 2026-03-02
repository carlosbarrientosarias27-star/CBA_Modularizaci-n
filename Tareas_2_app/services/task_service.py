# services/task_service.py

from models.task_model import tareas
from models import task_model
from utils.validators import validar_descripcion, validar_id


def agregar_tarea(descripcion):
    global contador_id
    ok, resultado = validar_descripcion(descripcion)
    if not ok:
        return False, f"❌ {resultado}"
    tarea = {
        "id":          contador_id,
        "descripcion": resultado,
        "completada":  False,
    }
    tareas.append(tarea)
    task_model.contador_id += 1
    return True, f"✅ Tarea #{tarea['id']} añadida: '{resultado}'"

def completar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for tarea in tareas:
        if tarea["id"] == resultado:
            if tarea["completada"]:
                return False, "⚠️  La tarea ya estaba completada."
            tarea["completada"] = True
            return True, f"✅ Tarea #{resultado} marcada como completada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def eliminar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for i, tarea in enumerate(tareas):
        if tarea["id"] == resultado:
            tareas.pop(i)
            return True, f"🗑️  Tarea #{resultado} eliminada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def listar_tareas():
    if not tareas:
        print("  📭 No hay tareas todavía.")
        return
    print(f"\n  {'ID':<5} {'ESTADO':<12} DESCRIPCIÓN")
    print("  " + "─" * 40)
    for t in tareas:
        estado = "✅ Hecha  " if t["completada"] else "⏳ Pendiente"
        print(f"  {t['id']:<5} {estado:<12} {t['descripcion']}")
    print()
