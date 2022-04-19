import bpy
import random
import functools
import time


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

counter = 0


def coinflip():
    return  random.randint(0,1)


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
    current_scale = obj.scale
    iterations = 10
    delta_x = (rand_scale[0] - current_scale[0]) / iterations
    delta_y = (rand_scale[1] - current_scale[1]) / iterations
    delta_z = (rand_scale[2] - current_scale[2]) / iterations
    counter = 0
    bpy.app.timers.register(functools.partial(smooth_scale, obj, delta_x, delta_y, delta_z, iterations, 0.05))    


def smooth_scale(obj, delta_x, delta_y, delta_z, iterations, delay=0.1):
    global counter
    counter += 1
    obj.scale = (obj.scale[0] + delta_x, obj.scale[1] + delta_y, obj.scale[2] + delta_z)
    if counter == iterations:
        return None
    return delay


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


def remove_modifiers(obj):
    gen_table_obj.modifiers.clear()


def complex_add_modifier(obj):
    modifier_names = ["BEVEL", "DECIMATE"]
    mod_index = random.randint(0,len(modifier_names) - 1)
    mod = modifier_names[mod_index]
    if coinflip():
        gen_table_obj.modifiers.new("Bevel", "BEVEL")
        gen_table_obj.modifiers.get("Bevel").affect = "EDGES"
        gen_table_obj.modifiers.get("Bevel").segments = random.randint(1, 6)
        gen_table_obj.modifiers.get("Bevel").width = random.uniform(0.1, 1.0)
    if coinflip():
        gen_table_obj.modifiers.new("Decimate", "DECIMATE")
        if coinflip:
            gen_table_obj.modifiers.get("Decimate").decimate_type = "COLLAPSE"
            gen_table_obj.modifiers.get("Decimate").ratio = random.uniform(0.5, 1.000) 
        else:
            gen_table_obj.modifiers.get("Decimate").decimate_type = "UNSUBDIV"
            gen_table_obj.modifiers.get("Decimate").iterations = random.randint(1, 4)


gen_table_obj = bpy.data.collections["Gen_Table_Col"].all_objects[0]
random_scale = [random.uniform(0.1, 0.45), random.uniform(0.1, 0.45), random.uniform(0.6, 2.5)]
random_color = [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), 1.0]

remove_modifiers(gen_table_obj)
complex_rescale(gen_table_obj, random_scale)
#scale_reset(gen_table_obj)
complex_recolor(gen_table_obj, random_color)
complex_add_modifier(gen_table_obj)
    