bl_info = {
    "name": "Hello World",
    "blender": (2, 91, 0),
    "category": "Object",
}

def register():
    print("Hello World")

def unregister():
    print("Goodbye World")