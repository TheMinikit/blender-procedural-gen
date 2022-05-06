import bpy
import random
import functools
import time

counter = 0

bl_info = {
    "name": "Procedural Model Generation",
    "author": "Dmitrij Kovner",
    "version": (1, 0),
    "blender": (3,1,0),
    "category": "Object",
    "description": "Plugin which procedurally generates tables and houses!"
}


class MESH_OT_monkey_grid(bpy.types.Operator):
    """Let's spread some joy"""
    bl_idname = 'mesh.monkey_grid'
    bl_label = "Monkey Grid"
    bl_options = {'REGISTER', 'UNDO'}

    count_x: bpy.props.IntProperty(
        name="X",
        description="Number of monkeys in X-direction",
        default=3,
        min=1,
        max=10,
    )
    count_y: bpy.props.IntProperty(
        name="Y",
        description="Number of monkeys in Y-direction",
        default=2,
        min=1,
        max=10,
    )
    size: bpy.props.FloatProperty(
        name="Size",
        description="Size of each monkey",
        default=0.5,
        min=0.01,
        max=1,
    )

    def execute(self, context):
        for idx in range(self.count_x * self.count_y):
            x = idx % self.count_x
            y = idx // self.count_x
            bpy.ops.mesh.primitive_monkey_add(
                size=self.size,
                location=(x, y, 1))

        return {'FINISHED'}



class VIEW3D_PT_proc_generation_plugin(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VGTU"
    bl_label = "ProcGen"

    def draw(self, context):
        self.layout.operator('mesh.monkey_grid',
                             text="Default Grid")


def register():
    bpy.utils.register_class(VIEW3D_PT_proc_generation_plugin)
    bpy.utils.register_class(MESH_OT_monkey_grid)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_proc_generation_plugin)
    bpy.utils.unregister_class(MESH_OT_monkey_grid)


def coinflip():
    return random.randint(0, 1)


def get_children(myobject):
    children = []
    for ob in bpy.data.objects:
        if ob.parent == myobject:
            children.append(ob)
    return children


class simple_table_gen:
    legs_dict = []
    tops_dict = []

    def simple_add_leg(self, obj):
        print("a")

    def simple_add_top(self, obj):
        print("a")

    def simple_get_legs(self):
        print("a")

    def simple_get_tops(self):
        print("a")

    def simple_print_legs(self):
        print("a")

    def simple_print_tops(self):
        print("a")

    def simple_remove_leg(self, index=-1):
        print("a")

    def simple_remove_top(self, index=-1):
        print("a")

    def simple_remove_legs(self):
        print("a")

    def simple_remove_tops(self):
        print("a")

    def simple_generate_table(self):
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

        table_legs_index = random.randint(0, len(all_table_legs) - 1)
        table_top_index = random.randint(0, len(all_table_tops) - 1)

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
        # 60 -4 0.2


class simple_house_gen:
    walls_dict = []
    roofs_dict = []

    def simple_add_wall(self, obj):
        print("a")

    def simple_add_roof(self, obj):
        print("a")

    def simple_get_walls(self):
        print("a")

    def simple_get_roofs(self):
        print("a")

    def simple_print_walls(self):
        print("a")

    def simple_print_roofs(self):
        print("a")

    def simple_remove_wall(self, index=-1):
        print("a")

    def simple_remove_roof(self, index=-1):
        print("a")

    def simple_remove_walls(self):
        print("a")

    def simple_remove_roofs(self):
        print("a")

    def simple_generate_house(self):
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

        table_legs_index = random.randint(0, len(all_table_legs) - 1)
        table_top_index = random.randint(0, len(all_table_tops) - 1)

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
        # 60 -4 0.2


class complex_table_gen:
    complex_limits = []

    def complex_rescale(self, obj, rand_scale=[0.3, 0.3, 1]):
        current_scale = obj.scale
        iterations = 10
        delta_x = (rand_scale[0] - current_scale[0]) / iterations
        delta_y = (rand_scale[1] - current_scale[1]) / iterations
        delta_z = (rand_scale[2] - current_scale[2]) / iterations
        counter = 0
        bpy.app.timers.register(functools.partial(self.smooth_scale, obj, delta_x, delta_y, delta_z, iterations, 0.05))

    def smooth_scale(self, obj, delta_x, delta_y, delta_z, iterations, delay=0.1):
        global counter
        counter += 1
        obj.scale = (obj.scale[0] + delta_x, obj.scale[1] + delta_y, obj.scale[2] + delta_z)
        if counter == iterations:
            return None
        return delay

    def scale_reset(self, obj):
        obj.scale = (0.3, 0.3, 1.0)

    def complex_recolor(self, obj, color):
        obj.select_set(True)
        bpy.ops.mesh.separate(type='LOOSE')
        mat = bpy.data.materials.new("PKHG")
        mat.diffuse_color = (color[0], color[1], color[2], color[3])

        for object in bpy.data.collections["Gen_Table_Col"].all_objects:
            object.active_material = mat

        obj_array = []
        for object in bpy.data.collections["Gen_Table_Col"].all_objects:
            obj_array.append(object)

        c = {"object": obj_array[0],
             "active_object": obj_array[0],
             "selected_objects": obj_array[0:],
             "selected_editable_objects": obj_array[0:]}
        bpy.ops.object.join(c)

    def remove_modifiers(self, obj):
        gen_table_obj.modifiers.clear()

    def complex_add_modifier(self, obj):
        modifier_names = ["BEVEL", "DECIMATE"]
        mod_index = random.randint(0, len(modifier_names) - 1)
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


class complex_house_gen:
    complex_limits = []

    def complex_rescale(self, obj, rand_scale=[0.3, 0.3, 1]):
        current_scale = obj.scale
        iterations = 10
        delta_x = (rand_scale[0] - current_scale[0]) / iterations
        delta_y = (rand_scale[1] - current_scale[1]) / iterations
        delta_z = (rand_scale[2] - current_scale[2]) / iterations
        counter = 0
        bpy.app.timers.register(functools.partial(self.smooth_scale, obj, delta_x, delta_y, delta_z, iterations, 0.05))

    def smooth_scale(self, obj, delta_x, delta_y, delta_z, iterations, delay=0.1):
        global counter
        counter += 1
        obj.scale = (obj.scale[0] + delta_x, obj.scale[1] + delta_y, obj.scale[2] + delta_z)
        if counter == iterations:
            return None
        return delay

    def scale_reset(self, obj):
        obj.scale = (0.3, 0.3, 1.0)

    def complex_recolor(self, obj, color):
        obj.select_set(True)
        bpy.ops.mesh.separate(type='LOOSE')
        mat = bpy.data.materials.new("PKHG")
        mat.diffuse_color = (color[0], color[1], color[2], color[3])

        for object in bpy.data.collections["Gen_Table_Col"].all_objects:
            object.active_material = mat

        obj_array = []
        for object in bpy.data.collections["Gen_Table_Col"].all_objects:
            obj_array.append(object)

        c = {"object": obj_array[0],
             "active_object": obj_array[0],
             "selected_objects": obj_array[0:],
             "selected_editable_objects": obj_array[0:]}
        bpy.ops.object.join(c)

    def remove_modifiers(self, obj):
        gen_table_obj.modifiers.clear()

    def complex_add_modifier(self, obj):
        modifier_names = ["BEVEL", "DECIMATE"]
        mod_index = random.randint(0, len(modifier_names) - 1)
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


#gen_table_obj = bpy.data.collections["Gen_Table_Col"].all_objects[0]
#random_scale = [random.uniform(0.1, 0.45), random.uniform(0.1, 0.45), random.uniform(0.6, 2.5)]
#random_color = [random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), 1.0]

#st = simple_table_gen()
#ct = complex_table_gen()

#ct.remove_modifiers(gen_table_obj)
#ct.complex_rescale(gen_table_obj, random_scale)
# scale_reset(gen_table_obj)
#ct.complex_recolor(gen_table_obj, random_color)
#ct.complex_add_modifier(gen_table_obj)