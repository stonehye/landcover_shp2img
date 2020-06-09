import arcpy
import os

cnt = 0

style = 'style.lyr'
path = 'data'
folder_list = os.listdir(path)

aprx = arcpy.mp.ArcGISProject('Project.aprx')
arcpy.env.workspace = 'Project.gdb'
aprx.defaultGeodatabase = 'Project.gdb'
aprx.defaultToolbox = 'Project.tbx'

for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)

map = aprx.listMaps()[0]

for name in folder_list:
	file = os.listdir(os.path.join(path, name))[0].split('.')[0]
	shpfile = os.path.join(path, name, file)+'.shp'
	arcpy.MakeFeatureLayer_management(shpfile, name)
	symbologyFields = [["VALUE_FIELD", "#", "L2_CODE"]]
	layer = arcpy.ApplySymbologyFromLayer_management(name, style, symbologyFields).getOutput(0)
	map.addLayer(layer)
	mv = map.defaultView
	mv.exportToPNG(name + ".png", 720, 1080)
	for lyr in map.listLayers():
		map.removeLayer(lyr)
	cnt+=1
	print("%d / %d" %(cnt, len(folder_list)))
	# aprx.save()