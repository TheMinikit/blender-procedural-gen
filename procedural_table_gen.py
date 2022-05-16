import bpy
import random
import functools
import time
import os
from bpy.props import BoolProperty, StringProperty

bl_info = {
    "name": "Procedural Model Generation",
    "author": "Dmitrij Kovner",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "category": "Object",
    "description": "Plugin which procedurally generates tables and houses!"
}

bpy.types.Scene.legs_list = []
bpy.types.Scene.tops_list = []
bpy.types.Scene.walls_list = []
bpy.types.Scene.roofs_list = []
bpy.types.Scene.doors_list = []
bpy.types.Scene.chimneys_list = []

bpy.types.Scene.tabledim_checkbox = BoolProperty(
    name="Pakeisti modelio matus",
    description="Funkcija keicianti modelio x,y,z matmenys",
    default=True)

bpy.types.Scene.tablecol_checkbox = BoolProperty(
    name="Pakeisti modelio spalvas",
    description="Funkcija keicianti modelio r,g,b spalvas",
    default=True)

bpy.types.Scene.tablebev_checkbox = BoolProperty(
    name="Panaudoti 'Bevel' modifikatori",
    description="Funkcija pridedanti modifikatori 'Bevel' prie modelio",
    default=True)

bpy.types.Scene.tabledec_checkbox = BoolProperty(
    name="Panaudoti 'Decimate' modifikatori",
    description="Funkcija pridedanti modifikatori 'Decimate' prie modelio",
    default=True)

bpy.types.Scene.housedim_checkbox = BoolProperty(
    name="Pakeisti modelio matus",
    description="Funkcija keicianti modelio x,y,z matmenys",
    default=True)

bpy.types.Scene.housecol_checkbox = BoolProperty(
    name="Pakeisti modelio spalvas",
    description="Funkcija keicianti modelio r,g,b spalvas",
    default=True)

bpy.types.Scene.housebev_checkbox = BoolProperty(
    name="Panaudoti 'Bevel' modifikatori",
    description="Funkcija pridedanti modifikatori 'Bevel' prie modelio",
    default=True)

bpy.types.Scene.housedec_checkbox = BoolProperty(
    name="Panaudoti 'Decimate' modifikatori",
    description="Funkcija pridedanti modifikatori 'Decimate' prie modelio",
    default=True)

bpy.types.Scene.remleg = StringProperty(
    name="Koju id",
    description="Koju trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.remtop = StringProperty(
    name="Stalvirsio id",
    description="Stalvirsio trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.remwall = StringProperty(
    name="Sienos id",
    description="Sienos trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.remroof = StringProperty(
    name="Stogo id",
    description="Stogo trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.remdoor = StringProperty(
    name="Duru id",
    description="Duru trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.remchimney = StringProperty(
    name="Zidinio id",
    description="Zidinio trinimo indeksas",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_minx = StringProperty(
    name="min x",
    description="Stalo matmens x minimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_maxx = StringProperty(
    name="max x",
    description="Stalo matmens x maksimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_miny = StringProperty(
    name="min y",
    description="Stalo matmens y minimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_maxy = StringProperty(
    name="max y",
    description="Stalo matmens y maksimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_minz = StringProperty(
    name="min z",
    description="Stalo matmens z minimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_maxz = StringProperty(
    name="max z",
    description="Stalo matmens z maksimumo riba",
    default="1",
    maxlen=10,
)

bpy.types.Scene.table_minr = StringProperty(
    name="min r",
    description="Stalo raudonos spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_maxr = StringProperty(
    name="max r",
    description="Stalo raudonos spalvos maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_ming = StringProperty(
    name="min g",
    description="Stalo zalios spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_maxg = StringProperty(
    name="max g",
    description="Stalo zalios spalvos maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_minb = StringProperty(
    name="min b",
    description="Stalo melynos spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.table_maxb = StringProperty(
    name="max b",
    description="Stalo melynos spalvos maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_minx = StringProperty(
    name="min x",
    description="Namo matmens x minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxx = StringProperty(
    name="min x",
    description="Namo matmens x maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_miny = StringProperty(
    name="min y",
    description="Namo matmens y minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxy = StringProperty(
    name="max y",
    description="Namo matmens y maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_minz = StringProperty(
    name="min z",
    description="Namo matmens z minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxz = StringProperty(
    name="max z",
    description="Namo matmens z maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_minr = StringProperty(
    name="min r",
    description="Namo raudonos spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxr = StringProperty(
    name="max r",
    description="Namo raudonos spalvos maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_ming = StringProperty(
    name="min g",
    description="Namo zalios spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxg = StringProperty(
    name="max g",
    description="Namo zalios spalvos maksimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_minb = StringProperty(
    name="min b",
    description="Namo melynos spalvos minimumo riba",
    default="0",
    maxlen=10,
)

bpy.types.Scene.house_maxb = StringProperty(
    name="max b",
    description="Namo melynos spalvos maksimumo riba",
    default="0",
    maxlen=10,
)


def coinflip():
    return random.randint(0, 1)


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


class OBJECT_OT_proc_gen_unit_tests(bpy.types.Operator):
    """Unit testing operator for Procedural Model Generation plugin"""
    bl_idname = 'object.proc_gen_unit_tests'
    bl_label = "Unit Test Procedural Generation Plugin"
    
    def init_lists(self):
        print("INIT")
        self.legs_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\table_legs")
        self.tops_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\table_tops")
        self.walls_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\house_walls")
        self.roofs_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\house_roofs")
        self.doors_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\house_doors")
        self.chimneys_list = os.listdir("C:\\Users\\User\\Desktop\\procgentests\\house_chimneys")
        
        
    def run_all_tests(self):
        self.legs_list_init()
        self.tops_list_init()
        self.walls_list_init()
        self.roofs_list_init()
        self.doors_list_init()
        self.chimneys_list_init()
        self.remove_leg_id_negative()
        self.remove_leg_id_greater_than_amount()
        self.remove_top_id_negative()
        self.remove_top_id_greater_than_amount()
        self.remove_wall_id_negative()
        self.remove_wall_id_greater_than_amount()
        self.remove_roof_id_negative()
        self.remove_roof_id_greater_than_amount()
        self.remove_door_id_negative()
        self.remove_door_id_greater_than_amount()
        self.remove_chimney_id_negative()
        self.remove_chimney_id_greater_than_amount()
        self.remove_leg_removes_object_from_list()
        self.remove_top_removes_object_from_list()
        self.remove_wall_removes_object_from_list()
        self.remove_roof_removes_object_from_list()
        self.remove_door_removes_object_from_list()
        self.remove_chimney_removes_object_from_list()
        self.remove_legs_removes_all_objects_from_list()
        self.remove_tops_removes_all_objects_from_list()
        self.remove_walls_removes_all_objects_from_list()
        self.remove_roofs_removes_all_objects_from_list()
        self.remove_doors_removes_all_objects_from_list()
        self.remove_chimneys_removes_all_objects_from_list()
        #self.rescale_minx_negative()
        


    def legs_list_init(self):
        assert(len(self.legs_list) > 0)
    
    def tops_list_init(self):
        assert(len(self.tops_list) > 0)
        
    def walls_list_init(self):
        assert(len(self.walls_list) > 0)
        
    def roofs_list_init(self):
        assert(len(self.roofs_list) > 0)
        
    def doors_list_init(self):
        assert(len(self.doors_list) > 0)
        
    def chimneys_list_init(self):
        assert(len(self.chimneys_list) > 0)

    def remove_leg_id_negative(self):
        bpy.context.scene.remleg = "-1"
        bpy.ops.object.remove_leg()
        assert(bpy.context.scene.remleg == "0")
        
    def remove_leg_id_greater_than_amount(self):
        bpy.context.scene.remleg = "10"
        bpy.ops.object.remove_leg()
        assert(bpy.context.scene.remleg == "0")
    
    def remove_top_id_negative(self):
        bpy.context.scene.remtop = "-1"
        bpy.ops.object.remove_top()
        assert(bpy.context.scene.remtop == "0")
        
    def remove_top_id_greater_than_amount(self):
        bpy.context.scene.remtop = "10"
        bpy.ops.object.remove_top()
        assert(bpy.context.scene.remtop== "0")
        
    def remove_wall_id_negative(self):
        bpy.context.scene.remwall = "-1"
        bpy.ops.object.remove_wall()
        assert(bpy.context.scene.remwall == "0")

    def remove_wall_id_greater_than_amount(self):
        bpy.context.scene.remwall = "10"
        bpy.ops.object.remove_wall()
        assert(bpy.context.scene.remwall == "0")
        
    def remove_roof_id_negative(self):
        bpy.context.scene.remroof = "-1"
        bpy.ops.object.remove_roof()
        assert(bpy.context.scene.remroof == "0")

    def remove_roof_id_greater_than_amount(self):
        bpy.context.scene.remroof = "10"
        bpy.ops.object.remove_roof()
        assert(bpy.context.scene.remroof == "0")
        
    def remove_door_id_negative(self):
        bpy.context.scene.remdoor = "-1"
        bpy.ops.object.remove_door()
        assert(bpy.context.scene.remdoor == "0")

    def remove_door_id_greater_than_amount(self):
        bpy.context.scene.remdoor = "10"
        bpy.ops.object.remove_door()
        assert (bpy.context.scene.remdoor == "0")
        
    def remove_chimney_id_negative(self):
        bpy.context.scene.remchimney = "-1"
        bpy.ops.object.remove_chimney()
        assert(bpy.context.scene.remchimney == "0")

    def remove_chimney_id_greater_than_amount(self):
        bpy.context.scene.remchimney = "10"
        bpy.ops.object.remove_chimney()
        assert (bpy.context.scene.remchimney == "0")

    def remove_leg_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.legs_list)
        bpy.context.scene.remleg = "0"
        bpy.ops.object.remove_leg()
        assert(len(bpy.context.scene.legs_list) < temp_amount)
        
    def remove_top_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.tops_list)
        bpy.context.scene.remtop = "0"
        bpy.ops.object.remove_top()
        assert(len(bpy.context.scene.tops_list) < temp_amount)
        
    def remove_wall_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.walls_list)
        bpy.context.scene.remwall = "0"
        bpy.ops.object.remove_wall()
        assert(len(bpy.context.scene.walls_list) < temp_amount)

    def remove_roof_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.roofs_list)
        bpy.context.scene.remroof = "0"
        bpy.ops.object.remove_roof()
        assert(len(bpy.context.scene.roofs_list) < temp_amount)
        
    def remove_door_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.doors_list)
        bpy.context.scene.remdoor = "0"
        bpy.ops.object.remove_door()
        assert(len(bpy.context.scene.doors_list) < temp_amount)
        
    def remove_chimney_removes_object_from_list(self):
        temp_amount = len(bpy.context.scene.chimneys_list)
        bpy.context.scene.remchimney = "0"
        bpy.ops.object.remove_chimney()
        assert(len(bpy.context.scene.chimneys_list) < temp_amount)

    def remove_legs_removes_all_objects_from_list(self):
        bpy.ops.object.remove_legs()
        assert(len(bpy.context.scene.legs_list) == 0)
        
    def remove_tops_removes_all_objects_from_list(self):
        bpy.ops.object.remove_tops()
        assert(len(bpy.context.scene.tops_list) == 0)
        
    def remove_walls_removes_all_objects_from_list(self):
        bpy.ops.object.remove_walls()
        assert(len(bpy.context.scene.walls_list) == 0)
        
    def remove_roofs_removes_all_objects_from_list(self):
        bpy.ops.object.remove_roofs()
        assert(len(bpy.context.scene.roofs_list) == 0)
        
    def remove_doors_removes_all_objects_from_list(self):
        bpy.ops.object.remove_doors()
        assert(len(bpy.context.scene.doors_list) == 0)
        
    def remove_chimneys_removes_all_objects_from_list(self):
        bpy.ops.object.remove_chimneys()
        assert(len(bpy.context.scene.chimneys_list) == 0)
        
    
    def rescale_minx_negative(self):
        bpy.context.scene.tablecol_checkbox = False
        bpy.context.scene.tablebev_checkbox = False
        bpy.context.scene.tabledec_checkbox = False
        bpy.context.scene.table_minx = "-1"
        bpy.ops.object.generate_simple_table()
        assert(int(bpy.context.scene.table_minx) == 0)
     

    def execute(self, context):
        self.init_lists()
        self.run_all_tests()
        return {'FINISHED'}


class OBJECT_OT_add_legs(bpy.types.Operator):
    """Adds table legs objects from specific folder"""
    bl_idname = 'object.add_legs'
    bl_label = "Add Table Legs"

    def execute(self, context):
        if len(context.scene.legs_list) > 0:
            legs_collection = bpy.data.collections.new("ProcGen_TableLegs")
            bpy.context.scene.collection.children.link(legs_collection)

            for leg in context.scene.legs_list:
                bpy.ops.import_scene.obj(filepath="C:\\Users\\User\\Desktop\\procgensamples\\table_legs\\" + leg)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    legs_collection.objects.link(ob)
        else:
            print("No table legs objects found in the legs list")
        return {'FINISHED'}


class OBJECT_OT_add_tops(bpy.types.Operator):
    """Adds table tops objects from specific folder"""
    bl_idname = 'object.add_tops'
    bl_label = "Add Table Tops"

    def execute(self, context):
        if len(context.scene.tops_list) > 0:
            tops_collection = bpy.data.collections.new("ProcGen_TableTops")
            bpy.context.scene.collection.children.link(tops_collection)

            for top in context.scene.tops_list:
                bpy.ops.import_scene.obj(filepath="C:\\Users\\User\\Desktop\\procgensamples\\table_tops\\" + top)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    tops_collection.objects.link(ob)
        else:
            print("No table tops objects found in the tops list")
        return {'FINISHED'}


class OBJECT_OT_add_walls(bpy.types.Operator):
    """Adds house walls objects from specific folder"""
    bl_idname = 'object.add_walls'
    bl_label = "Add House Walls"

    def execute(self, context):
        if len(context.scene.walls_list) > 0:
            walls_collection = bpy.data.collections.new("ProcGen_HouseWalls")
            bpy.context.scene.collection.children.link(walls_collection)

            for wall in context.scene.walls_list:
                bpy.ops.import_scene.obj(filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_walls\\" + wall)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    walls_collection.objects.link(ob)
        else:
            print("No house walls objects found in the walls list")
        return {'FINISHED'}


class OBJECT_OT_add_roofs(bpy.types.Operator):
    """Adds house roofs objects from specific folder"""
    bl_idname = 'object.add_roofs'
    bl_label = "Add House Roofs"

    def execute(self, context):
        if len(context.scene.roofs_list) > 0:
            roofs_collection = bpy.data.collections.new("ProcGen_HouseRoofs")
            bpy.context.scene.collection.children.link(roofs_collection)

            for roof in context.scene.roofs_list:
                bpy.ops.import_scene.obj(filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_roofs\\" + roof)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    roofs_collection.objects.link(ob)
        else:
            print("No house roofs objects found in the roofs list")
        return {'FINISHED'}


class OBJECT_OT_add_doors(bpy.types.Operator):
    """Adds house doors objects from specific folder"""
    bl_idname = 'object.add_doors'
    bl_label = "Add House Doors"

    def execute(self, context):
        if len(context.scene.doors_list) > 0:
            doors_collection = bpy.data.collections.new("ProcGen_HouseDoors")
            bpy.context.scene.collection.children.link(doors_collection)

            for door in context.scene.doors_list:
                bpy.ops.import_scene.obj(filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_doors\\" + door)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    doors_collection.objects.link(ob)
        else:
            print("No house doors objects found in the doors list")
        return {'FINISHED'}


class OBJECT_OT_add_chimneys(bpy.types.Operator):
    """Adds house chimneys objects from specific folder"""
    bl_idname = 'object.add_chimneys'
    bl_label = "Add House Chimneys"

    def execute(self, context):
        if len(context.scene.chimneys_list) > 0:
            chimneys_collection = bpy.data.collections.new("ProcGen_HouseChimneys")
            bpy.context.scene.collection.children.link(chimneys_collection)

            for chimney in context.scene.chimnneys_list:
                bpy.ops.import_scene.obj(
                    filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_chimneys\\" + chimney)
                objs = bpy.context.selected_objects[:]
                for ob in objs:
                    for coll in ob.users_collection:
                        coll.objects.unlink(ob)
                    chimneys_collection.objects.link(ob)
        else:
            print("No house chimneys objects found in the chimneys list")
        return {'FINISHED'}


class OBJECT_OT_remove_leg(bpy.types.Operator):
    """Remove table leg object from legs list"""
    bl_idname = 'object.remove_leg'
    bl_label = "Remove Table Leg"

    def execute(self, context):
        try:
            remlegid = int(context.scene.remleg)
            if remlegid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remleg = "0"
            elif remlegid > int(context.scene.legs_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.legs_amount) + ")")
                context.scene.remleg = "0"
            else:
                print("Removed object with id: " + str(remlegid))
                context.scene.legs_list.remove(context.scene.legs_list[remlegid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remleg = "0"
        except:
            print("Unknown Error")
            context.scene.remleg = "0"
        return {'FINISHED'}


class OBJECT_OT_remove_top(bpy.types.Operator):
    """Remove table top object from tops list"""
    bl_idname = 'object.remove_top'
    bl_label = "Remove Table Top"

    def execute(self, context):
        try:
            remtopid = int(context.scene.remtop)
            if remtopid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remtop = "0"
            elif remtopid > int(context.scene.tops_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.tops_amount) + ")")
                context.scene.remtop = "0"
            else:
                print("Removed object with id: " + str(remtopid))
                context.scene.tops_list.remove(context.scene.tops_list[remtopid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remtop = "0"
        except:
            print("Unknown Error")
            context.scene.remtop = "0"
        return {'FINISHED'}


class OBJECT_OT_remove_wall(bpy.types.Operator):
    """Remove house wall object from walls list"""
    bl_idname = 'object.remove_wall'
    bl_label = "Remove House Wall"

    def execute(self, context):
        try:
            remwallid = int(context.scene.remwall)
            if remwallid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remwall = "0"
            elif remwallid > int(context.scene.walls_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.walls_amount) + ")")
                context.scene.remwall = "0"
            else:
                print("Removed object with id: " + str(remwallid))
                context.scene.walls_list.remove(context.scene.walls_list[remwallid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remwall = "0"
        except:
            print("Unknown Error")
            context.scene.remwall = "0"
        return {'FINISHED'}


class OBJECT_OT_remove_roof(bpy.types.Operator):
    """Remove house roof object from roofs list"""
    bl_idname = 'object.remove_roof'
    bl_label = "Remove House Roof"

    def execute(self, context):
        try:
            remroofid = int(context.scene.remroof)
            if remroofid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remroof = "0"
            elif remroofid > int(context.scene.roofs_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.roofs_amount) + ")")
                context.scene.remroof = "0"
            else:
                print("Removed object with id: " + str(remroofid))
                context.scene.roofs_list.remove(context.scene.roofs_list[remroofid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remroof = "0"
        except:
            print("Unknown Error")
            context.scene.remroof = "0"
        return {'FINISHED'}


class OBJECT_OT_remove_door(bpy.types.Operator):
    """Remove house door object from doors list"""
    bl_idname = 'object.remove_door'
    bl_label = "Remove House Door"

    def execute(self, context):
        try:
            remdoorid = int(context.scene.remdoor)
            if remdoorid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remdoor = "0"
            elif remdoorid > int(context.scene.doors_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.doors_amount) + ")")
                context.scene.remdoor = "0"
            else:
                print("Removed object with id: " + str(remdoorid))
                context.scene.doors_list.remove(context.scene.doors_list[remdoorid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remdoor = "0"
        except:
            print("Unknown Error")
            context.scene.remdoor = "0"
        return {'FINISHED'}


class OBJECT_OT_remove_chimney(bpy.types.Operator):
    """Remove house chimney object from chimneys list"""
    bl_idname = 'object.remove_chimney'
    bl_label = "Remove House chimney"

    def execute(self, context):
        try:
            remchimneyid = int(context.scene.remchimney)
            if remchimneyid < 0:
                print("Error: Please input valid index (>-1)")
                context.scene.remchimney = "0"
            elif remchimneyid > int(context.scene.chimneys_amount) - 1:
                print("Error: Please input valid index (<" + str(context.scene.chimneys_amount) + ")")
                context.scene.remchimney = "0"
            else:
                print("Removed object with id: " + str(remchimneyid))
                context.scene.chimneys_list.remove(context.scene.chimneys_list[remchimneyid])
        except ValueError:
            print("Error: Please input int type value")
            context.scene.remchimney = "0"
        except:
            print("Unknown Error")
            context.scene.remchimney = "0"
        return {'FINISHED'}


class OBJECT_OT_print_legs(bpy.types.Operator):
    """Print all table legs objects (id and name) in legs list"""
    bl_idname = 'object.print_legs'
    bl_label = "Print Table Legs"

    def execute(self, context):
        for leg in context.scene.legs_list:
            print(str(context.scene.legs_list.index(leg)) + ": " + leg)
        return {'FINISHED'}


class OBJECT_OT_print_tops(bpy.types.Operator):
    """Print all table top objects (id and name) in tops list"""
    bl_idname = 'object.print_tops'
    bl_label = "Print Table Tops"

    def execute(self, context):
        for top in context.scene.tops_list:
            print(str(context.scene.tops_list.index(top)) + ": " + top)
        return {'FINISHED'}


class OBJECT_OT_print_walls(bpy.types.Operator):
    """Print all house walls objects (id and name) in walls list"""
    bl_idname = 'object.print_walls'
    bl_label = "Print House Walls"

    def execute(self, context):
        for wall in context.scene.walls_list:
            print(str(context.scene.walls_list.index(wall)) + ": " + wall)
        return {'FINISHED'}


class OBJECT_OT_print_roofs(bpy.types.Operator):
    """Print all house roofs objects (id and name) in roofs list"""
    bl_idname = 'object.print_roofs'
    bl_label = "Print House Roofs"

    def execute(self, context):
        for roof in context.scene.roofs_list:
            print(str(context.scene.roofs_list.index(roof)) + ": " + roof)
        return {'FINISHED'}


class OBJECT_OT_print_doors(bpy.types.Operator):
    """Print all house doors objects (id and name) in doors list"""
    bl_idname = 'object.print_doors'
    bl_label = "Print House Doors"

    def execute(self, context):
        for door in context.scene.doors_list:
            print(str(context.scene.doors_list.index(door)) + ": " + door)
        return {'FINISHED'}


class OBJECT_OT_print_chimneys(bpy.types.Operator):
    """Print all house chimneys objects (id and name) in chimneys list"""
    bl_idname = 'object.print_chimneys'
    bl_label = "Print House Chimneys"

    def execute(self, context):
        for chimney in context.scene.chimneys_list:
            print(str(context.scene.chimneys_list.index(chimney)) + ": " + chimney)
        return {'FINISHED'}


class OBJECT_OT_remove_all_legs(bpy.types.Operator):
    """Remove ALL table legs objects from legs list"""
    bl_idname = 'object.remove_legs'
    bl_label = "Remove ALL Table Legs"

    def execute(self, context):
        context.scene.legs_list.clear()
        print("All table legs objects removed from legs list")
        return {'FINISHED'}


class OBJECT_OT_remove_all_tops(bpy.types.Operator):
    """Remove ALL table top objects from tops list"""
    bl_idname = 'object.remove_tops'
    bl_label = "Remove ALL Table Tops"

    def execute(self, context):
        context.scene.tops_list.clear()
        print("All table top objects removed from tops list")
        return {'FINISHED'}


class OBJECT_OT_remove_all_walls(bpy.types.Operator):
    """Remove ALL house walls objects from walls list"""
    bl_idname = 'object.remove_walls'
    bl_label = "Remove ALL House Walls"

    def execute(self, context):
        context.scene.walls_list.clear()
        print("All house walls objects removed from walls list")
        return {'FINISHED'}


class OBJECT_OT_remove_all_roofs(bpy.types.Operator):
    """Remove ALL house roofs objects from roofs list"""
    bl_idname = 'object.remove_roofs'
    bl_label = "Remove ALL House Roofs"

    def execute(self, context):
        context.scene.roofs_list.clear()
        print("All house roofs objects removed from roofs list")
        return {'FINISHED'}


class OBJECT_OT_remove_all_doors(bpy.types.Operator):
    """Remove ALL house doors objects from doors list"""
    bl_idname = 'object.remove_doors'
    bl_label = "Remove ALL House Doors"

    def execute(self, context):
        context.scene.doors_list.clear()
        print("All house doors objects removed from doors list")
        return {'FINISHED'}


class OBJECT_OT_remove_all_chimneys(bpy.types.Operator):
    """Remove ALL house chimneys objects from chimneys list"""
    bl_idname = 'object.remove_chimneys'
    bl_label = "Remove ALL House Chimneys"

    def execute(self, context):
        context.scene.chimneys_list.clear()
        print("All house chimneys objects removed from chimneys list")
        return {'FINISHED'}


class OBJECT_OT_generate_simple_table(bpy.types.Operator):
    """Procedurally generate table model using modular method"""
    bl_idname = 'object.generate_simple_table'
    bl_label = "Procedurally generate modular table"

    def execute(self, context):

        table_legs_index = random.randint(0, len(context.scene.legs_list) - 1)
        table_top_index = random.randint(0, len(context.scene.tops_list) - 1)

        if 'Simple Table Generation Results' not in bpy.data.collections.keys():
            simple_table_results_collection = bpy.data.collections.new("Simple Table Generation Results")
            bpy.context.scene.collection.children.link(simple_table_results_collection)

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\table_legs\\" + context.scene.legs_list[
                table_legs_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple Table Generation Results'].objects.link(ob)
            ob.location.x = 0
            ob.location.y = 0
            ob.location.z = 0.0

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\table_tops\\" + context.scene.tops_list[
                table_top_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple Table Generation Results'].objects.link(ob)
            ob.location.x = 0
            ob.location.y = 0
            ob.location.z = 6.2

        for objects in bpy.data.collections['Simple Table Generation Results'].all_objects:
            objects.select_set(True)

        objs = bpy.context.selected_objects[:]
        ctx = bpy.context.copy()
        ctx['active_object'] = objs[0]
        ctx['selected_objects'] = objs[1:]
        bpy.ops.object.join(ctx)
        simple_table_model = bpy.data.collections['Simple Table Generation Results'].all_objects[0]
        simple_table_model.name = "Table model"

        return {'FINISHED'}


class OBJECT_OT_generate_simple_house(bpy.types.Operator):
    """Procedurally generate house model using modular method"""
    bl_idname = 'object.generate_simple_house'
    bl_label = "Procedurally generate modular house"

    def execute(self, context):

        house_wall_index = random.randint(0, len(context.scene.walls_list) - 1)
        house_roof_index = random.randint(0, len(context.scene.roofs_list) - 1)
        house_door_index = random.randint(0, len(context.scene.doors_list) - 1)
        house_chimney_index = random.randint(0, len(context.scene.chimneys_list) - 1)

        if 'Simple House Generation Results' not in bpy.data.collections.keys():
            simple_house_results_collection = bpy.data.collections.new("Simple House Generation Results")
            bpy.context.scene.collection.children.link(simple_house_results_collection)

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_walls\\" + context.scene.walls_list[
                house_wall_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple House Generation Results'].objects.link(ob)
            ob.location.x = 0
            ob.location.y = 35
            ob.location.z = 0

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_roofs\\" + context.scene.roofs_list[
                house_roof_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple House Generation Results'].objects.link(ob)
            ob.location.x = 0
            ob.location.y = 35
            ob.location.z = 6

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_doors\\" + context.scene.doors_list[
                house_door_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple House Generation Results'].objects.link(ob)
            ob.location.x = 0
            ob.location.y = 32
            ob.location.z = 0

        bpy.ops.import_scene.obj(
            filepath="C:\\Users\\User\\Desktop\\procgensamples\\house_chimneys\\" + context.scene.chimneys_list[
                house_chimney_index])
        objs = bpy.context.selected_objects[:]
        for ob in objs:
            for coll in ob.users_collection:
                coll.objects.unlink(ob)
            bpy.data.collections['Simple House Generation Results'].objects.link(ob)
            ob.location.x = 2
            ob.location.y = 35
            ob.location.z = 6

        for objects in bpy.data.collections['Simple House Generation Results'].all_objects:
            objects.select_set(True)

        objs = bpy.context.selected_objects[:]
        ctx = bpy.context.copy()
        ctx['active_object'] = objs[0]
        ctx['selected_objects'] = objs[1:]
        bpy.ops.object.join(ctx)
        simple_house_model = bpy.data.collections['Simple House Generation Results'].all_objects[0]
        simple_house_model.name = "House model"

        return {'FINISHED'}


class OBJECT_OT_generate_complex_table(bpy.types.Operator):
    """Procedurally generate table model using automatic variations method"""
    bl_idname = 'object.generate_complex_table'
    bl_label = "Procedurally generate AV table"

    bpy.types.Scene.counter = 0

    def smooth_scale(self, obj, delta_x, delta_y, delta_z, iterations, delay=0.1):
        bpy.types.Scene.counter += 1
        obj.scale = (obj.scale[0] + delta_x, obj.scale[1] + delta_y, obj.scale[2] + delta_z)
        if bpy.types.Scene.counter == iterations:
            return None
        return delay

    def execute(self, context):
        if 'Complex Table Generation Results' not in bpy.data.collections.keys():
            complex_table_results_collection = bpy.data.collections.new("Complex Table Generation Results")
            bpy.context.scene.collection.children.link(complex_table_results_collection)
        else:
            complex_table_results_collection = bpy.data.collections["Complex Table Generation Results"]

        if len(bpy.data.collections["Complex Table Generation Results"].all_objects) == 0:
            bpy.ops.import_scene.obj(
                filepath="C:\\Users\\User\\Desktop\\procgensamples\\complex_table\\complex_table.obj")
            objs = bpy.context.selected_objects[:]
            for ob in objs:
                for coll in ob.users_collection:
                    coll.objects.unlink(ob)
                complex_table_results_collection.objects.link(ob)
        complex_table_model = bpy.data.collections['Complex Table Generation Results'].all_objects[0]
        complex_table_model.name = "Sample table model"
        complex_table_model.location.z = 1

        if context.scene.tabledim_checkbox:
            try:
                table_minx = int(context.scene.table_minx)
                table_maxx = int(context.scene.table_maxx)
                table_miny = int(context.scene.table_miny)
                table_maxy = int(context.scene.table_maxy)
                table_minz = int(context.scene.table_minz)
                table_maxz = int(context.scene.table_maxz)
                if table_minx <= 0 or table_maxx > 10 or table_miny <= 0 or table_maxy > 10 or table_minz <= 0 or table_maxz > 10:
                    print("Error: Please input valid dimensions (0<x<10)")
                    context.scene.table_minx = "1"
                    context.scene.table_maxx = "1"
                    context.scene.table_miny = "1"
                    context.scene.table_maxy = "1"
                    context.scene.table_minz = "1"
                    context.scene.table_maxz = "1"
                    table_minx = 1
                    table_maxx = 1
                    table_miny = 1
                    table_maxy = 1
                    table_minz = 1
                    table_maxz = 1
                if table_minx > table_maxx or table_miny > table_maxy or table_minz > table_maxz:
                    print("Error: min has to be lower than max")
                    context.scene.table_minx = "1"
                    context.scene.table_maxx = "1"
                    context.scene.table_miny = "1"
                    context.scene.table_maxy = "1"
                    context.scene.table_minz = "1"
                    context.scene.table_maxz = "1"
                    table_minx = 1
                    table_maxx = 1
                    table_miny = 1
                    table_maxy = 1
                    table_minz = 1
                    table_maxz = 1
            except ValueError:
                print("Error: Please input int type value")
                context.scene.table_minx = "1"
                context.scene.table_maxx = "1"
                context.scene.table_miny = "1"
                context.scene.table_maxy = "1"
                context.scene.table_minz = "1"
                context.scene.table_maxz = "1"
                table_minx = 1
                table_maxx = 1
                table_miny = 1
                table_maxy = 1
                table_minz = 1
                table_maxz = 1
            except:
                print("Unknown Error")
                context.scene.table_minx = "1"
                context.scene.table_maxx = "1"
                context.scene.table_miny = "1"
                context.scene.table_maxy = "1"
                context.scene.table_minz = "1"
                context.scene.table_maxz = "1"
                table_minx = 1
                table_maxx = 1
                table_miny = 1
                table_maxy = 1
                table_minz = 1
                table_maxz = 1

            # complex_table_model.scale = (1.0, 1.0, 1.0)
            current_scale = complex_table_model.scale
            iterations = 10
            rand_x = random.uniform(table_minx, table_maxx)
            rand_y = random.uniform(table_miny, table_maxy)
            rand_z = random.uniform(table_minz, table_maxz)
            rand_scale = [rand_x, rand_y, rand_z]
            delta_x = (rand_scale[0] - current_scale[0]) / iterations
            delta_y = (rand_scale[1] - current_scale[1]) / iterations
            delta_z = (rand_scale[2] - current_scale[2]) / iterations
            bpy.types.Scene.counter = 0
            bpy.app.timers.register(functools.partial(
                self.smooth_scale,
                complex_table_model,
                delta_x,
                delta_y,
                delta_z,
                iterations,
                0.03))

        complex_table_model.modifiers.clear()

        if context.scene.tablecol_checkbox:
            try:
                table_minr = int(context.scene.table_minr)
                table_maxr = int(context.scene.table_maxr)
                table_ming = int(context.scene.table_ming)
                table_maxg = int(context.scene.table_maxg)
                table_minb = int(context.scene.table_minb)
                table_maxb = int(context.scene.table_maxb)
                if table_minr < 0 or table_maxr > 1 or table_ming < 0 or table_maxg > 1 or table_minb < 0 or table_maxb > 1:
                    print("Error: Please input valid dimensions (0<x<1)")
                    context.scene.table_minr = "0"
                    context.scene.table_maxr = "0"
                    context.scene.table_ming = "0"
                    context.scene.table_maxg = "0"
                    context.scene.table_minb = "0"
                    context.scene.table_maxb = "0"
                    table_minr = 0
                    table_maxr = 0
                    table_ming = 0
                    table_maxg = 0
                    table_minb = 0
                    table_maxb = 0
                if table_minr > table_maxr or table_ming > table_maxg or table_minb > table_maxb:
                    print("Error: min has to be lower than max")
                    context.scene.table_minr = "0"
                    context.scene.table_maxr = "0"
                    context.scene.table_ming = "0"
                    context.scene.table_maxg = "0"
                    context.scene.table_minb = "0"
                    context.scene.table_maxb = "0"
                    table_minr = 0
                    table_maxr = 0
                    table_ming = 0
                    table_maxg = 0
                    table_minb = 0
                    table_maxb = 0
            except ValueError:
                print("Error: Please input int type value")
                context.scene.table_minr = "0"
                context.scene.table_maxr = "0"
                context.scene.table_ming = "0"
                context.scene.table_maxg = "0"
                context.scene.table_minb = "0"
                context.scene.table_maxb = "0"
                table_minr = 0
                table_maxr = 0
                table_ming = 0
                table_maxg = 0
                table_minb = 0
                table_maxb = 0
            except:
                print("Unknown Error")
                context.scene.table_minr = "0"
                context.scene.table_maxr = "0"
                context.scene.table_ming = "0"
                context.scene.table_maxg = "0"
                context.scene.table_minb = "0"
                context.scene.table_maxb = "0"
                table_minr = 0
                table_maxr = 0
                table_ming = 0
                table_maxg = 0
                table_minb = 0
                table_maxb = 0

            complex_table_model.select_set(True)
            bpy.ops.mesh.separate(type='LOOSE')
            mat = bpy.data.materials.new("PKHG")
            rand_r = random.uniform(table_minr, table_maxr)
            rand_g = random.uniform(table_ming, table_maxg)
            rand_b = random.uniform(table_minb, table_maxb)
            mat.diffuse_color = (rand_r, rand_g, rand_b, 1.0)

            for object in bpy.data.collections["Complex Table Generation Results"].all_objects:
                object.active_material = mat

            obj_array = []
            for object in bpy.data.collections["Complex Table Generation Results"].all_objects:
                obj_array.append(object)

            c = {"object": obj_array[0],
                 "active_object": obj_array[0],
                 "selected_objects": obj_array[0:],
                 "selected_editable_objects": obj_array[0:]}
            bpy.ops.object.join(c)

        modifier_names = ["BEVEL", "DECIMATE"]

        if context.scene.tablebev_checkbox:
            complex_table_model.modifiers.new("Bevel", "BEVEL")
            complex_table_model.modifiers.get("Bevel").affect = "EDGES"
            complex_table_model.modifiers.get("Bevel").segments = random.randint(1, 6)
            complex_table_model.modifiers.get("Bevel").width = random.uniform(0.1, 1.0)
        if context.scene.tabledec_checkbox:
            complex_table_model.modifiers.new("Decimate", "DECIMATE")
            if coinflip():
                complex_table_model.modifiers.get("Decimate").decimate_type = "COLLAPSE"
                complex_table_model.modifiers.get("Decimate").ratio = random.uniform(0.5, 1.000)
            else:
                complex_table_model.modifiers.get("Decimate").decimate_type = "UNSUBDIV"
                complex_table_model.modifiers.get("Decimate").iterations = random.randint(1, 4)

        return {'FINISHED'}
    

class OBJECT_OT_generate_complex_house(bpy.types.Operator):
    """Procedurally generate house model using automatic variations method"""
    bl_idname = 'object.generate_complex_house'
    bl_label = "Procedurally generate AV house"

    bpy.types.Scene.counter = 0

    def smooth_scale(self, obj, delta_x, delta_y, delta_z, iterations, delay=0.1):
        bpy.types.Scene.counter += 1
        obj.scale = (obj.scale[0] + delta_x, obj.scale[1] + delta_y, obj.scale[2] + delta_z)
        if bpy.types.Scene.counter == iterations:
            return None
        return delay

    def execute(self, context):
        if 'Complex House Generation Results' not in bpy.data.collections.keys():
            complex_house_results_collection = bpy.data.collections.new("Complex House Generation Results")
            bpy.context.scene.collection.children.link(complex_house_results_collection)
        else:
            complex_house_results_collection = bpy.data.collections["Complex House Generation Results"]

        if len(bpy.data.collections["Complex House Generation Results"].all_objects) == 0:
            bpy.ops.import_scene.obj(
                filepath="C:\\Users\\User\\Desktop\\procgensamples\\complex_house\\complex_house.obj")
            objs = bpy.context.selected_objects[:]
            for ob in objs:
                for coll in ob.users_collection:
                    coll.objects.unlink(ob)
                complex_house_results_collection.objects.link(ob)
        complex_house_model = bpy.data.collections['Complex House Generation Results'].all_objects[0]
        complex_house_model.name = "Sample House model"
        complex_house_model.location.z = 1

        if context.scene.housedim_checkbox:
            try:
                house_minx = int(context.scene.house_minx)
                house_maxx = int(context.scene.house_maxx)
                house_miny = int(context.scene.house_miny)
                house_maxy = int(context.scene.house_maxy)
                house_minz = int(context.scene.house_minz)
                house_maxz = int(context.scene.house_maxz)
                if house_minx <= 0 or house_maxx > 10 or house_miny <= 0 or house_maxy > 10 or house_minz <= 0 or house_maxz > 10:
                    print("Error: Please input valid dimensions (0<x<10)")
                    context.scene.house_minx = "1"
                    context.scene.house_maxx = "1"
                    context.scene.house_miny = "1"
                    context.scene.house_maxy = "1"
                    context.scene.house_minz = "1"
                    context.scene.house_maxz = "1"
                    house_minx = 1
                    house_maxx = 1
                    house_miny = 1
                    house_maxy = 1
                    house_minz = 1
                    house_maxz = 1
                if house_minx > house_maxx or house_miny > house_maxy or house_minz > house_maxz:
                    print("Error: min has to be lower than max")
                    context.scene.house_minx = "1"
                    context.scene.house_maxx = "1"
                    context.scene.house_miny = "1"
                    context.scene.house_maxy = "1"
                    context.scene.house_minz = "1"
                    context.scene.house_maxz = "1"
                    house_minx = 1
                    house_maxx = 1
                    house_miny = 1
                    house_maxy = 1
                    house_minz = 1
                    house_maxz = 1
            except ValueError:
                print("Error: Please input int type value")
                context.scene.house_minx = "1"
                context.scene.house_maxx = "1"
                context.scene.house_miny = "1"
                context.scene.house_maxy = "1"
                context.scene.house_minz = "1"
                context.scene.house_maxz = "1"
                house_minx = 1
                house_maxx = 1
                house_miny = 1
                house_maxy = 1
                house_minz = 1
                house_maxz = 1
            except:
                print("Unknown Error")
                context.scene.house_minx = "1"
                context.scene.house_maxx = "1"
                context.scene.house_miny = "1"
                context.scene.house_maxy = "1"
                context.scene.house_minz = "1"
                context.scene.house_maxz = "1"
                house_minx = 1
                house_maxx = 1
                house_miny = 1
                house_maxy = 1
                house_minz = 1
                house_maxz = 1

            # complex_house_model.scale = (1.0, 1.0, 1.0)
            current_scale = complex_house_model.scale
            iterations = 10
            rand_x = random.uniform(house_minx, house_maxx)
            rand_y = random.uniform(house_miny, house_maxy)
            rand_z = random.uniform(house_minz, house_maxz)
            rand_scale = [rand_x, rand_y, rand_z]
            delta_x = (rand_scale[0] - current_scale[0]) / iterations
            delta_y = (rand_scale[1] - current_scale[1]) / iterations
            delta_z = (rand_scale[2] - current_scale[2]) / iterations
            bpy.types.Scene.counter = 0
            bpy.app.timers.register(functools.partial(
                self.smooth_scale,
                complex_house_model,
                delta_x,
                delta_y,
                delta_z,
                iterations,
                0.03))

        complex_house_model.modifiers.clear()

        if context.scene.housecol_checkbox:
            try:
                house_minr = int(context.scene.house_minr)
                house_maxr = int(context.scene.house_maxr)
                house_ming = int(context.scene.house_ming)
                house_maxg = int(context.scene.house_maxg)
                house_minb = int(context.scene.house_minb)
                house_maxb = int(context.scene.house_maxb)
                if house_minr < 0 or house_maxr > 1 or house_ming < 0 or house_maxg > 1 or house_minb < 0 or house_maxb > 1:
                    print("Error: Please input valid dimensions (0<x<1)")
                    context.scene.house_minr = "0"
                    context.scene.house_maxr = "0"
                    context.scene.house_ming = "0"
                    context.scene.house_maxg = "0"
                    context.scene.house_minb = "0"
                    context.scene.house_maxb = "0"
                    house_minr = 0
                    house_maxr = 0
                    house_ming = 0
                    house_maxg = 0
                    house_minb = 0
                    house_maxb = 0
                if house_minr > house_maxr or house_ming > house_maxg or house_minb > house_maxb:
                    print("Error: min has to be lower than max")
                    context.scene.house_minr = "0"
                    context.scene.house_maxr = "0"
                    context.scene.house_ming = "0"
                    context.scene.house_maxg = "0"
                    context.scene.house_minb = "0"
                    context.scene.house_maxb = "0"
                    house_minr = 0
                    house_maxr = 0
                    house_ming = 0
                    house_maxg = 0
                    house_minb = 0
                    house_maxb = 0
            except ValueError:
                print("Error: Please input int type value")
                context.scene.house_minr = "0"
                context.scene.house_maxr = "0"
                context.scene.house_ming = "0"
                context.scene.house_maxg = "0"
                context.scene.house_minb = "0"
                context.scene.house_maxb = "0"
                house_minr = 0
                house_maxr = 0
                house_ming = 0
                house_maxg = 0
                house_minb = 0
                house_maxb = 0
            except:
                print("Unknown Error")
                context.scene.house_minr = "0"
                context.scene.house_maxr = "0"
                context.scene.house_ming = "0"
                context.scene.house_maxg = "0"
                context.scene.house_minb = "0"
                context.scene.house_maxb = "0"
                house_minr = 0
                house_maxr = 0
                house_ming = 0
                house_maxg = 0
                house_minb = 0
                house_maxb = 0

            complex_house_model.select_set(True)
            bpy.ops.mesh.separate(type='LOOSE')
            mat = bpy.data.materials.new("PKHG")
            rand_r = random.uniform(house_minr, house_maxr)
            rand_g = random.uniform(house_ming, house_maxg)
            rand_b = random.uniform(house_minb, house_maxb)
            mat.diffuse_color = (rand_r, rand_g, rand_b, 1.0)

            for object in bpy.data.collections["Complex House Generation Results"].all_objects:
                object.active_material = mat

            obj_array = []
            for object in bpy.data.collections["Complex House Generation Results"].all_objects:
                obj_array.append(object)

            c = {"object": obj_array[0],
                 "active_object": obj_array[0],
                 "selected_objects": obj_array[0:],
                 "selected_edihouse_objects": obj_array[0:]}
            bpy.ops.object.join(c)

        modifier_names = ["BEVEL", "DECIMATE"]

        if context.scene.housebev_checkbox:
            complex_house_model.modifiers.new("Bevel", "BEVEL")
            complex_house_model.modifiers.get("Bevel").affect = "EDGES"
            complex_house_model.modifiers.get("Bevel").segments = random.randint(1, 6)
            complex_house_model.modifiers.get("Bevel").width = random.uniform(0.1, 1.0)
        if context.scene.housedec_checkbox:
            complex_house_model.modifiers.new("Decimate", "DECIMATE")
            if coinflip():
                complex_house_model.modifiers.get("Decimate").decimate_type = "COLLAPSE"
                complex_house_model.modifiers.get("Decimate").ratio = random.uniform(0.5, 1.000)
            else:
                complex_house_model.modifiers.get("Decimate").decimate_type = "UNSUBDIV"
                complex_house_model.modifiers.get("Decimate").iterations = random.randint(1, 4)

        return {'FINISHED'}


class VIEW3D_PT_proc_generation_plugin(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VGTU"
    bl_label = "ProcGen"

    bpy.types.Scene.legs_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\table_legs")
    bpy.types.Scene.tops_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\table_tops")
    bpy.types.Scene.walls_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\house_walls")
    bpy.types.Scene.roofs_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\house_roofs")
    bpy.types.Scene.doors_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\house_doors")
    bpy.types.Scene.chimneys_list = os.listdir("C:\\Users\\User\\Desktop\\procgensamples\\house_chimneys")

    for leg in bpy.types.Scene.legs_list:
        if ".mtl" in leg:
            bpy.types.Scene.legs_list.remove(leg)

    for top in bpy.types.Scene.tops_list:
        if ".mtl" in top:
            bpy.types.Scene.tops_list.remove(top)

    for wall in bpy.types.Scene.walls_list:
        if ".mtl" in wall:
            bpy.types.Scene.walls_list.remove(wall)

    for roof in bpy.types.Scene.roofs_list:
        if ".mtl" in roof:
            bpy.types.Scene.roofs_list.remove(roof)

    for door in bpy.types.Scene.doors_list:
        if ".mtl" in door:
            bpy.types.Scene.doors_list.remove(door)

    for chimney in bpy.types.Scene.chimneys_list:
        if ".mtl" in chimney:
            bpy.types.Scene.chimneys_list.remove(chimney)

    bpy.types.Scene.legs_amount = str(len(bpy.types.Scene.legs_list))
    bpy.types.Scene.tops_amount = str(len(bpy.types.Scene.tops_list))
    bpy.types.Scene.walls_amount = str(len(bpy.types.Scene.walls_list))
    bpy.types.Scene.roofs_amount = str(len(bpy.types.Scene.roofs_list))
    bpy.types.Scene.doors_amount = str(len(bpy.types.Scene.doors_list))
    bpy.types.Scene.chimneys_amount = str(len(bpy.types.Scene.chimneys_list))

    def draw(self, context):
        split1 = self.layout.split()

        col1 = split1.column()
        col1_row1 = col1.row()
        col1_row1.label(text="Paprastas stalu generavimas")
        col1_row2 = col1.row()
        col1_row2.operator('object.add_legs', text="Prideti stalo kojas")
        col1_row2.label(text="Rasta koju: " + bpy.context.scene.legs_amount)
        col1_row3 = col1.row()
        col1_row3.operator('object.add_tops', text="Prideti stalvirsius")
        col1_row3.label(text="Rasta stalvirsiu: " + bpy.context.scene.tops_amount)
        col1_row4 = col1.row()
        col1_row4.operator('object.remove_leg', text="Istrinti kojas")
        col1_row4.prop(context.scene, "remleg")
        col1_row5 = col1.row()
        col1_row5.operator('object.remove_top', text="Istrinti stalvirsi")
        col1_row5.prop(context.scene, "remtop")
        col1_row6 = col1.row()
        col1_row6.operator('object.print_legs', text="Isvesti koju objektus")
        col1_row6.operator('object.print_tops', text="Isvesti stalvirsiu objektus")
        col1_row7 = col1.row()
        col1_row7.operator('object.remove_legs', text="Istrinti VISAS kojas")
        col1_row7.operator('object.remove_tops', text="Istrinti VISUS stalvirsius")
        col1_row8 = col1.row()
        col1_row8.operator('object.generate_simple_table', text="Sugeneruoti stala")

        col2 = split1.column()
        col2_row1 = col2.row()
        col2_row1.label(text="Paprastas namu generavimas")
        col2_row2 = col2.row()
        col2_row2.operator('object.add_walls', text="Prideti namo sienas")
        col2_row2.label(text="Rasta sienu: " + bpy.context.scene.walls_amount)
        col2_row3 = col2.row()
        col2_row3.operator('object.add_roofs', text="Prideti namo stogus")
        col2_row3.label(text="Rasta stogu: " + bpy.context.scene.roofs_amount)
        col2_row4 = col2.row()
        col2_row4.operator('object.add_doors', text="Prideti namo durys")
        col2_row4.label(text="Rasta durys: " + bpy.context.scene.doors_amount)
        col2_row5 = col2.row()
        col2_row5.operator('object.add_chimneys', text="Prideti namo zidinius")
        col2_row5.label(text="Rasta zidiniu: " + bpy.context.scene.chimneys_amount)
        col2_row6 = col2.row()
        col2_row6.operator('object.remove_wall', text="Istrinti siena")
        col2_row6.prop(context.scene, "remwall")
        col2_row7 = col2.row()
        col2_row7.operator('object.remove_roof', text="Istrinti stoga")
        col2_row7.prop(context.scene, "remroof")
        col2_row8 = col2.row()
        col2_row8.operator('object.remove_door', text="Istrinti duris")
        col2_row8.prop(context.scene, "remdoor")
        col2_row9 = col2.row()
        col2_row9.operator('object.remove_chimney', text="Istrinti zidini")
        col2_row9.prop(context.scene, "remchimney")
        col2_row10 = col2.row()
        col2_row10.operator('object.print_walls', text="Isvesti sienu objektus")
        col2_row10.operator('object.print_roofs', text="Isvesti stogu objektus")
        col2_row11 = col2.row()
        col2_row11.operator('object.print_doors', text="Isvesti duru objektus")
        col2_row11.operator('object.print_chimneys', text="Isvesti zidiniu objektus")
        col2_row12 = col2.row()
        col2_row12.operator('object.remove_walls', text="Istrinti VISAS sienas")
        col2_row12.operator('object.remove_roofs', text="Istrinti VISUS stogus")
        col2_row13 = col2.row()
        col2_row13.operator('object.remove_doors', text="Istrinti VISAS durys")
        col2_row13.operator('object.remove_chimneys', text="Istrinti VISUS zidinius")
        col2_row14 = col2.row()
        col2_row14.operator('object.generate_simple_house', text="Sugeneruoti nama")

        sep = self.layout.separator()

        split2 = self.layout.split()
        col3 = split2.column()
        col3_row1 = col3.row()
        col3_row1.label(text="Sudetingas stalu generavimas")
        col3_row2 = col3.row()
        col3_row2.prop(context.scene, "tabledim_checkbox")
        col3_row3 = col3.row()
        col3_row3.prop(context.scene, "table_minx")
        col3_row3.prop(context.scene, "table_maxx")
        col3_row4 = col3.row()
        col3_row4.prop(context.scene, "table_miny")
        col3_row4.prop(context.scene, "table_maxy")
        col3_row5 = col3.row()
        col3_row5.prop(context.scene, "table_minz")
        col3_row5.prop(context.scene, "table_maxz")
        col3_row6 = col3.row()
        col3_row6.prop(context.scene, "tablecol_checkbox")
        col3_row7 = col3.row()
        col3_row7.prop(context.scene, "table_minr")
        col3_row7.prop(context.scene, "table_maxr")
        col3_row8 = col3.row()
        col3_row8.prop(context.scene, "table_ming")
        col3_row8.prop(context.scene, "table_maxg")
        col3_row9 = col3.row()
        col3_row9.prop(context.scene, "table_minb")
        col3_row9.prop(context.scene, "table_maxb")
        col3_row10 = col3.row()
        col3_row10.prop(context.scene, "tablebev_checkbox")
        col3_row11 = col3.row()
        col3_row11.prop(context.scene, "tabledec_checkbox")
        col3_row12 = col3.row()
        col3_row12.operator('object.generate_complex_table', text="Sugeneruoti stala")

        col4 = split2.column()
        col4_row1 = col4.row()
        col4_row1.label(text="Sudetingas namu generavimas")
        col4_row2 = col4.row()
        col4_row2.prop(context.scene, "housedim_checkbox")
        col4_row3 = col4.row()
        col4_row3.prop(context.scene, "house_minx")
        col4_row3.prop(context.scene, "house_maxx")
        col4_row4 = col4.row()
        col4_row4.prop(context.scene, "house_miny")
        col4_row4.prop(context.scene, "house_maxy")
        col4_row5 = col4.row()
        col4_row5.prop(context.scene, "house_minz")
        col4_row5.prop(context.scene, "house_maxz")
        col4_row6 = col4.row()
        col4_row6.prop(context.scene, "housecol_checkbox")
        col4_row7 = col4.row()
        col4_row7.prop(context.scene, "house_minr")
        col4_row7.prop(context.scene, "house_maxr")
        col4_row8 = col4.row()
        col4_row8.prop(context.scene, "house_ming")
        col4_row8.prop(context.scene, "house_maxg")
        col4_row9 = col4.row()
        col4_row9.prop(context.scene, "house_minb")
        col4_row9.prop(context.scene, "house_maxb")
        col4_row10 = col4.row()
        col4_row10.prop(context.scene, "housebev_checkbox")
        col4_row11 = col4.row()
        col4_row11.prop(context.scene, "housedec_checkbox")
        col4_row12 = col4.row()
        col4_row12.operator('object.generate_complex_house', text="Sugeneruoti nama")


def register():
    bpy.utils.register_class(VIEW3D_PT_proc_generation_plugin)
    bpy.utils.register_class(MESH_OT_monkey_grid)
    bpy.utils.register_class(OBJECT_OT_add_legs)
    bpy.utils.register_class(OBJECT_OT_add_tops)
    bpy.utils.register_class(OBJECT_OT_add_walls)
    bpy.utils.register_class(OBJECT_OT_add_roofs)
    bpy.utils.register_class(OBJECT_OT_add_doors)
    bpy.utils.register_class(OBJECT_OT_add_chimneys)
    bpy.utils.register_class(OBJECT_OT_remove_leg)
    bpy.utils.register_class(OBJECT_OT_remove_top)
    bpy.utils.register_class(OBJECT_OT_remove_wall)
    bpy.utils.register_class(OBJECT_OT_remove_roof)
    bpy.utils.register_class(OBJECT_OT_remove_door)
    bpy.utils.register_class(OBJECT_OT_remove_chimney)
    bpy.utils.register_class(OBJECT_OT_print_legs)
    bpy.utils.register_class(OBJECT_OT_print_tops)
    bpy.utils.register_class(OBJECT_OT_print_walls)
    bpy.utils.register_class(OBJECT_OT_print_roofs)
    bpy.utils.register_class(OBJECT_OT_print_doors)
    bpy.utils.register_class(OBJECT_OT_print_chimneys)
    bpy.utils.register_class(OBJECT_OT_remove_all_legs)
    bpy.utils.register_class(OBJECT_OT_remove_all_tops)
    bpy.utils.register_class(OBJECT_OT_remove_all_walls)
    bpy.utils.register_class(OBJECT_OT_remove_all_roofs)
    bpy.utils.register_class(OBJECT_OT_remove_all_doors)
    bpy.utils.register_class(OBJECT_OT_remove_all_chimneys)
    bpy.utils.register_class(OBJECT_OT_generate_simple_table)
    bpy.utils.register_class(OBJECT_OT_generate_simple_house)
    bpy.utils.register_class(OBJECT_OT_generate_complex_table)
    bpy.utils.register_class(OBJECT_OT_generate_complex_house)
    bpy.utils.register_class(OBJECT_OT_proc_gen_unit_tests)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_proc_generation_plugin)
    bpy.utils.unregister_class(MESH_OT_monkey_grid)
    bpy.utils.unregister_class(OBJECT_OT_add_legs)
    bpy.utils.unregister_class(OBJECT_OT_add_tops)
    bpy.utils.unregister_class(OBJECT_OT_add_walls)
    bpy.utils.unregister_class(OBJECT_OT_add_roofs)
    bpy.utils.unregister_class(OBJECT_OT_add_doors)
    bpy.utils.unregister_class(OBJECT_OT_add_chimneys)
    bpy.utils.unregister_class(OBJECT_OT_remove_leg)
    bpy.utils.unregister_class(OBJECT_OT_remove_top)
    bpy.utils.unregister_class(OBJECT_OT_remove_wall)
    bpy.utils.unregister_class(OBJECT_OT_remove_roof)
    bpy.utils.unregister_class(OBJECT_OT_remove_door)
    bpy.utils.unregister_class(OBJECT_OT_remove_chimney)
    bpy.utils.unregister_class(OBJECT_OT_print_legs)
    bpy.utils.unregister_class(OBJECT_OT_print_tops)
    bpy.utils.unregister_class(OBJECT_OT_print_walls)
    bpy.utils.unregister_class(OBJECT_OT_print_roofs)
    bpy.utils.unregister_class(OBJECT_OT_print_doors)
    bpy.utils.unregister_class(OBJECT_OT_print_chimneys)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_legs)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_tops)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_walls)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_roofs)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_doors)
    bpy.utils.unregister_class(OBJECT_OT_remove_all_chimneys)
    bpy.utils.unregister_class(OBJECT_OT_generate_simple_table)
    bpy.utils.unregister_class(OBJECT_OT_generate_simple_house)
    bpy.utils.unregister_class(OBJECT_OT_generate_complex_table)
    bpy.utils.unregister_class(OBJECT_OT_generate_complex_house)
    bpy.utils.unregister_class(OBJECT_OT_proc_gen_unit_tests)

