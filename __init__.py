bl_info = {
        "name": "Select according to the axiu",
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

if "bpy" in locals():
    import imp
    imp.reload(module)
else:
    from . import module


import bpy, bmesh
from bpy.props import FloatProperty, EnumProperty

# class must be named Hoge_OT_Piyo.
class SelectVertices_OT_SelectMesh(bpy.types.Operator):

    bl_idname = "mesh.select_according_to_the_axis"
    bl_label = "Select according to the axis"
    bl_description = "Select according to the axis"
    bl_options = {'REGISTER', 'UNDO'}

    orientation: EnumProperty(
            name="Orientation",
            description="Orientation",
            default="Global",
            items=[
                ("Global", "Global", "Global orientation."),
                ("Local", "Local", "Local orientation."),
            ]
    )

    axis: EnumProperty(
            name="Axis",
            description="Target axis",
            default="-X",
            items=[
                ("-X", "-X", "Select according to the X axis."),
                ("+X", "+X", "Select according to the X axis."),
                ("-Y", "-Y", "Select according to the Y axis."),
                ("+Y", "+Y", "Select according to the Y axis."),
                ("-Z", "-Z", "Select according to the Z axis."),
                ("+Z", "+Z", "Select according to the Z axis."),
            ]
    )

    offset: FloatProperty(
        name="Offset",
        description="Offset",
        default=0.0,
        step=0.1
    )

    def execute(self, context):

        module.select_axis(context, self.orientation, self.axis, self.offset)
        return {'FINISHED'}


class SelectVerticesByAxis_MT_ParentMenu(bpy.types.Menu):

    bl_idname = "mesh.parent_menu"
    bl_label = "Select according to the axis"
    bl_discription = "Select according to the axis"

    def draw(self, context):
        layout = self.layout
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="-X").axis = "-X"
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="+X").axis = "+X"
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="-Y").axis = "-Y"
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="+Y").axis = "+Y"
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="-Z").axis = "-Z"
        layout.operator(SelectVertices_OT_SelectMesh.bl_idname, text="+Z").axis = "+Z"



def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(SelectVerticesByAxis_MT_ParentMenu.bl_idname)


classes = [
    SelectVertices_OT_SelectMesh,
    SelectVerticesByAxis_MT_ParentMenu,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_fn)
    print(bl_info["name"] + " is valid.")


def unregister():
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print(bl_info["name"] + "is invalid.")


if __name__ == "__main__":
    register()
