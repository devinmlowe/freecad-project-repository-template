#!/usr/bin/env python3
import os
import glob
from datetime import datetime

def generate_gallery():
    """Generate HTML gallery of rendered models"""
    
    renders = glob.glob("renders/*.png")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>FreeCAD Model Gallery</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .gallery {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .model {{ border: 1px solid #ddd; padding: 15px; border-radius: 8px; }}
        .model img {{ width: 100%; height: auto; border-radius: 4px; }}
        .model h3 {{ margin: 10px 0 5px 0; }}
        .metadata {{ color: #666; font-size: 0.9em; }}
        header {{ text-align: center; margin-bottom: 40px; }}
    </style>
</head>
<body>
    <header>
        <h1>FreeCAD Model Gallery</h1>
        <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </header>
    
    <div class="gallery">"""
    
    for render_path in sorted(renders):
        model_name = os.path.basename(render_path).replace('.png', '')
        
        html += f"""
        <div class="model">
            <img src="{os.path.basename(render_path)}" alt="{model_name}">
            <h3>{model_name}</h3>
            <div class="metadata">
                Last updated: {datetime.fromtimestamp(os.path.getmtime(render_path)).strftime('%Y-%m-%d')}
            </div>
        </div>"""
    
    html += """
    </div>
</body>
</html>"""
    
    with open("renders/index.html", "w") as f:
        f.write(html)
    
    print("Gallery generated: renders/index.html")

if __name__ == "__main__":
    os.makedirs("renders", exist_ok=True)
    generate_gallery()