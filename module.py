import bpy, bmesh

def select_axis(context, axis, offset):
    # Get all vertex.
    me = context.object.data      # return type: bpy.types.Mesh
    bm = bmesh.from_edit_mesh(me) # return type: bmesh.types.Bmesh
    for v in bm.verts:

        if axis == "-X":
            if v.co.x < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+X":
            if v.co.x > offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "-Y":
            if v.co.y < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+Y":
            if v.co.y > offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "-Z":
            if v.co.z < -offset:
                v.select_set(True)
            else:
                v.select_set(False)

        elif axis == "+Z":
            if v.co.z > offset:
                v.select_set(True)
            else:
                v.select_set(False)


    bmesh.update_edit_mesh(me)
    me.update()
