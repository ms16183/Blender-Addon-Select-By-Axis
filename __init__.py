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

import bpy, bmesh
from bpy.props import FloatProperty, EnumProperty

# class must be named Hoge_OT_Piyo.
class SelectVertex_OT_SelectMesh(bpy.types.Operator):

    bl_idname = "mesh.select_vertex"
    bl_label = "<- X"
    bl_description = "Select <- X"
    bl_options = {'REGISTER', 'UNDO'}

    axis: EnumProperty(
            name="Axis",
            description="Forcused Axis",
            default="-X",
            items=[
                ("-X", "-X", "Select according to X axis."),
                ("+X", "+X", "Select according to X axis."),
                ("-Y", "-Y", "Select according to Y axis."),
                ("+Y", "+Y", "Select according to Y axis."),
                ("-Z", "-Z", "Select according to Z axis."),
                ("+Z", "+Z", "Select according to Z axis."),
            ]
    )

    offset: FloatProperty(
        name="Offset",
        description="Offset",
        default=0.0000,
        step=0.0001
    )

    def execute(self, context):
        # Get all vertex.
        me = context.object.data      # return type: bpy.types.Mesh
        bm = bmesh.from_edit_mesh(me) # return type: bmesh.types.Bmesh
        for v in bm.verts:

            if self.axis == "-X":
                if v.co.x < self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)

            elif self.axis == "+X":
                if v.co.x > -self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)

            elif self.axis == "-Y":
                if v.co.y < self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)

            elif self.axis == "+Y":
                if v.co.y > -self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)

            elif self.axis == "-Z":
                if v.co.z < self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)

            elif self.axis == "+Z":
                if v.co.z > -self.offset:
                    v.select_set(True)
                else:
                    v.select_set(False)


        bmesh.update_edit_mesh(me)
        me.update()

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
