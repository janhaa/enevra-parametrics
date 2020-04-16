# numArguments = 1

import ConfigParser
Config = ConfigParser.ConfigParser()

from flask import Flask, escape, request

import FreeCAD

Config.read("config.ini")


# load
FreeCAD.open("parametric_model.FCStd")

# set parameters

print(Config.get("parameters", "fluegel_breite"))

FreeCAD.ActiveDocument.Spreadsheet.set('B1', Config.get("parameters", "fluegel_breite"))

# Fluegelband_Laenge
FreeCAD.ActiveDocument.Spreadsheet.set('B2', Config.get("parameters", 'fluegel_laenge'))

# Armband_Laenge
FreeCAD.ActiveDocument.Spreadsheet.set('B3', Config.get("parameters", 'armband_laenge'))

# Hinten_Breite
FreeCAD.ActiveDocument.Spreadsheet.set('B4', Config.get("parameters", 'hinten_breite'))

# Schnuere_Winkel:
FreeCAD.ActiveDocument.Spreadsheet.set('B5', '80')

# Schnuere_HorizontalerInnenabstand:
FreeCAD.ActiveDocument.Spreadsheet.set('B6', '0,50')

# Schnuere_HoriontalerAussenabstand:
FreeCAD.ActiveDocument.Spreadsheet.set('B7', '1,50')

# Schnuere_VertikalerInnenabstand:
FreeCAD.ActiveDocument.Spreadsheet.set('B8', '3')

# Rippe_Breite:
FreeCAD.ActiveDocument.Spreadsheet.set('B9', '2')

# rebuild
FreeCAD.ActiveDocument.recompute()

# export
__objs__=[]
__objs__.append(FreeCAD.ActiveDocument.getObject("Body"))
import Mesh
Mesh.export(__objs__,u"./output.stl")
del __objs__

# close and exit
FreeCAD.closeDocument("parametric_model")
FreeCAD.setActiveDocument("")
FreeCAD.ActiveDocument=None