bl_info = {
    "name": "Move X Axis",
    "blender": (2, 91, 0),
    "category": "Object",
}

import bpy

class ObjectMoveX(bpy.types.Operator):
    """Object Moving Script"""          # Tooltip for menu items and buttons
    bl_idname = "object.move_x"         # Unique reference ID for menu items and buttons
    bl_label = "Move X by One"          # Interface display name
    bl_options = {'REGISTER', 'UNDO'}   # Enable undo operation

    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            if obj.select_get():
                obj.location.x += 1.0

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

# Allow running directly from Text Editor without installing
if __name__ == "__main__":
    register()