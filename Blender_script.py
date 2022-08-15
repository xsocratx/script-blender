import bpy

for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)
    
collection = bpy.context.blend_data.collections.new(name='CONTENTS')
bpy.context.collection.children.link(collection)
    
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(3, 0, 0), scale=(1, 1, 1))

bpy.ops.mesh.primitive_cone_add(enter_editmode=False, align='WORLD', location=(6, 0, 0), scale=(1, 1, 1))

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(9, 0, 0), scale=(1, 1, 1))

for obj in bpy.data.objects:
    bpy.data.objects[obj.name].select_set(True)

bpy.ops.object.move_to_collection(collection_index=2)


bpy.ops.mesh.primitive_plane_add(size=6, enter_editmode=False, align='WORLD', location=(-16, 0, 0), scale=(1, 1, 1))

bpy.data.objects['Plane'].select_set(True)
bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name="DISTRIBUTOR")

bpy.ops.node.new_geometry_nodes_modifier()

