import bpy, bmesh
import math, mathutils

def select_axis(context, orientation="Global", axis="-X", offset=0.0):
    
    # get all vertices.
    me = context.object.data      # return type: bpy.types.Mesh
    bm = bmesh.from_edit_mesh(me) # return type: bmesh.types.Bmesh


    for v in bm.verts:

        # update coordinates according to the orientation.
        x, y, z = v.co
        if orientation == "Global":
            mat = context.object.matrix_world
            x, y, z = mat @ v.co
        elif orientation == "Local":
            x, y, z = v.co

        # select vertices.
        if (axis == "-X" and x < -offset) or (axis == "+X" and x > offset) \
        or (axis == "-Y" and y < -offset) or (axis == "+Y" and y > offset) \
        or (axis == "-Z" and z < -offset) or (axis == "+Z" and z > offset):
            v.select_set(True)
        else:
            v.select_set(False)

    # display selection mark when select mode is changed.
    bm.select_flush(True)

    # select edges and faces made up of the selected vertices.
    #bpy.ops.mesh.select_more()

    # update mesh from bmesh.
    bmesh.update_edit_mesh(me)
    me.update()
