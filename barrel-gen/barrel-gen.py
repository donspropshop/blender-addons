bl_info = {
    "name": "Barrel Gen",
    "description": "Add on for generating barrels.",
    "author": "Don Newman",
    "version": (0, 1),
    "blender": (2, 91, 0),
    "location": "View3D > Add > Barrel",
    "category": "Object",
}

import bpy                              # pylint: disable=import-error

class BarrelGen(bpy.types.Operator):
    """Barrel Generator"""              # Tooltip for menu items and buttons
    bl_idname = "object.add_barrel"     # Unique reference ID for menu items and buttons
    bl_label = "Barrel"                 # Interface display name
    bl_options = {'REGISTER', 'UNDO'}   # Enable undo operation

    def execute(self, context):
        scene = context.scene
        barrelName = "Barrel"

        barrelMesh = bpy.data.meshes.new(barrelName)
        barrelObject = bpy.data.objects.new(barrelName, barrelMesh)

        scene.collection.objects.link(barrelObject)
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BarrelGen.bl_idname, icon="PLUS")

addon_keymaps = []

def register():
    bpy.utils.register_class(BarrelGen)
    bpy.types.VIEW3D_MT_add.append(menu_func)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(BarrelGen.bl_idname, 'ACCENT_GRAVE', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

    bpy.utils.unregister_class(BarrelGen)
    bpy.types.VIEW3D_MT_add.remove(menu_func)

# Allow running directly from Text Editor without installing
if __name__ == "__main__":
    register()