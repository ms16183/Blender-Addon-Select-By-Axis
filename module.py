import bpy, bmesh
import math, mathutils

def select_axis(context, orientations, axis, offset):
    
    bpy.ops.mesh.select_mode(type="VERT")

    # Get all vertex.
    me = context.object.data      # return type: bpy.types.Mesh
    bm = bmesh.from_edit_mesh(me) # return type: bmesh.types.Bmesh

    for v in bm.verts:

        x, y, z = v.co

        if orientations == "Global":
            mat = context.object.matrix_world
            x, y, z = mat @ v.co

        if axis == "-X":
            if x < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+X":
            if x > offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "-Y":
            if y < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+Y":
            if y > offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "-Z":
            if z < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+Z":
            if z > offset:
                v.select_set(True)
            else:
                v.select_set(False)


    bmesh.update_edit_mesh(me)
    me.update()
