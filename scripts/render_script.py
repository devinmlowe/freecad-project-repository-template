#!/usr/bin/env python3
import sys
import FreeCAD
import FreeCADGui

def render_model(fcstd_path, output_path):
    """Render FreeCAD model to PNG"""
    
    # Open document
    doc = FreeCAD.openDocument(fcstd_path)
    
    # Initialize GUI for rendering
    FreeCADGui.showMainWindow()
    
    # Get all visible objects
    objects = [obj for obj in doc.Objects if hasattr(obj, 'ViewObject') and obj.ViewObject.Visibility]
    
    if not objects:
        print(f"No visible objects in {fcstd_path}")
        return
    
    # Fit all objects in view
    FreeCADGui.ActiveDocument.ActiveView.fitAll()
    
    # Set isometric view
    FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
    
    # Render and save
    FreeCADGui.ActiveDocument.ActiveView.saveImage(output_path, 1920, 1080, 'Transparent')
    
    # Close document
    FreeCAD.closeDocument(doc.Name)
    print(f"Rendered: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: render_script.py <input.FCStd> <output.png>")
        sys.exit(1)
    
    render_model(sys.argv[1], sys.argv[2])