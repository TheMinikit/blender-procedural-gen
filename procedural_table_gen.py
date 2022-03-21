import bpy
import random


# Useful code
'''
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))

for object in bpy.data.collections["Gen_Table_Col"].all_objects:
        print(object.name)
        
children = getChildren(gen_table_obj)
for c in children:
    print(c.name)
    
for ob in bpy.data.objects:
    print("OBJ: " + str(ob.name))
    
'''


def simple_rand_table_gen():  
      
    single_table_legs = []
    all_table_legs = []
    all_table_tops = []

    for coll in bpy.data.collections:
        single_table_legs.clear()
        if "Legs" in coll.name and "All" not in coll.name:
            for obj in coll.all_objects:
                if "Full" in obj.name:
                    all_table_legs.append(obj)
        if "Tops" in coll.name:
            for obj in coll.all_objects:
                all_table_tops.append(obj)
        
    print("Found " + str(len(all_table_legs)) + " table legs examples")
    print("Found " + str(len(all_table_tops)) + " table tops examples")



    if len(bpy.data.collections['Table Generation Results'].all_objects) > 0:
        for obj in bpy.data.collections['Table Generation Results'].all_objects:
            bpy.data.objects.remove(obj, do_unlink=True)

    table_legs_index = random.randint(0,len(all_table_legs) - 1)
    table_top_index = random.randint(0,len(all_table_tops) - 1)

    copied_table_legs = all_table_legs[table_legs_index].copy()
    bpy.data.collections['Table Generation Results'].objects.link(copied_table_legs)
    copied_table_legs.location.x = 60
    copied_table_legs.location.y = -4
    copied_table_legs.location.z = 0.4

    copied_table_top = all_table_tops[table_top_index].copy()
    bpy.data.collections['Table Generation Results'].objects.link(copied_table_top)
    copied_table_top.location.x = 60
    copied_table_top.location.y = -4
    copied_table_top.location.z = 6.6
    #60 -4 0.2


def complex_rescale(obj, rand_scale=[0.3,0.3,1]):
    obj.scale = (0.3, 0.3, 1)
    obj.scale = (rand_scale[0], rand_scale[1], rand_scale[2])

def scale_reset(obj):
    obj.scale = (0.3, 0.3, 1.0)

def getChildren(myObject): 
    children = [] 
    for ob in bpy.data.objects: 
        if ob.parent == myObject: 
            children.append(ob) 
    return children 

def complex_recolor(obj, color):
    obj.select_set(True)
    bpy.ops.mesh.separate(type='LOOSE')
    mat = bpy.data.materials.new("PKHG")
    mat.diffuse_color = (color[0], color[1], color[2], color[3])
    
    for object in bpy.data.collections["Gen_Table_Col"].all_objects:
        object.active_material = mat
        
    obj_array = []
    for object in bpy.data.collections["Gen_Table_Col"].all_objects:
        obj_array.append(object)
        
    c = {}
    c["object"] = obj_array[0]
    c["active_object"] = obj_array[0]
    c["selected_objects"] = obj_array[0:]
    c["selected_editable_objects"] = obj_array[0:]
    bpy.ops.object.join(c)

def complex_add_modifier(obj):
    modifier_names = ["BEVEL"]
    gen_table_obj.modifiers.clear()
    mod_index = random.randint(0,len(modifier_names) - 1)
    mod = modifier_names[mod_index]
    gen_table_obj.modifiers.new(str(mod), mod)
    if mod == "BEVEL":
        gen_table_obj.modifiers.get(mod).segments = random.randint(1,6)


gen_table_obj = bpy.data.collections["Gen_Table_Col"].all_objects[0]
random_scale = [random.uniform(0.1, 0.45), random.uniform(0.1, 0.45), random.uniform(0.6, 2.5)]
random_color = [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), 1.0]

complex_rescale(gen_table_obj, random_scale)
#scale_reset(gen_table_obj)
complex_recolor(gen_table_obj, random_color)
complex_add_modifier(gen_table_obj)
    