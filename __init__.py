bl_info = {
        "name": "Axis Select",
        "author": "ms16183",
        "version": (1, 0),
        "blender": (2, 80, 0),
        "location": "3D Viewport> Select",
        "description": "Select accroding to the axis.",
        "warning": "",
        "support": "TESTING",
        "wiki_url": "",
        "tracker_url": "",
        "category": "Mesh"
}

import bpy

# class must be named Hoge_OT_Piyo.
class SelectVertex_OT_SelectMesh(bpy.types.Operator):

    bl_idname = "mesh.select_vertex"
    bl_label = "<- X"
    bl_description = "Select <- X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}



def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SelectVertex_OT_SelectMesh.bl_idname)


classes = [
    SelectVertex_OT_SelectMesh,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_fn)
    print("Valid '%s'." % bl_info["name"])


def unregister():
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("Invalid '%s'." % bl_info["name"])


if __name__ == "__main__":
    register()
