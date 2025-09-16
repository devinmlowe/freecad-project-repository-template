# [Project Name]

## Project Overview
Brief description of what this project creates/designs.

## Creating New Projects from Template

### Using FreeCAD Macro (Recommended)
1. **Install the macro** by copying `scripts/ProjectFromTemplate.FCMacro` to your FreeCAD macro directory:
   ```bash
   # macOS
   cp scripts/ProjectFromTemplate.FCMacro ~/Library/Application\ Support/FreeCAD/Macro/

   # Linux
   cp scripts/ProjectFromTemplate.FCMacro ~/.local/share/FreeCAD/Macro/

   # Windows
   copy scripts\ProjectFromTemplate.FCMacro %APPDATA%\FreeCAD\Macro\
   ```

2. **Run the macro** from FreeCAD (Macro → Macros → ProjectFromTemplate)

3. **Fill out the project details**:
   - **Project Name**: Your new project name (e.g., "my-robot-arm")
   - **Project Description**: Brief description of what you're designing
   - **Project Location**: Where to create the project folder
   - **Template Source**: Git URL or local path to this template

4. **The macro will automatically**:
   - Clone/copy the template files
   - Update README.md with your project name and description
   - Initialize Git repository (optional)
   - Run FreeCAD Git setup script (optional)
   - **Create an empty FreeCAD file** in `models/{project-name}.FCStd`
   - **Open the new FreeCAD file** for immediate use

### Using GitHub Template Button
1. Click "Use this template" on the GitHub repository
2. Create your new repository
3. Clone locally and run the setup script manually

### Manual Copy
1. Download/clone this template
2. Copy to your new project location
3. Run setup scripts manually

## Git Setup for FreeCAD
**First time setup on each machine:**
```bash
# Make script executable and run
chmod +x setup-git-freecad.sh
./setup-git-freecad.sh
```

This configures Git to handle `.FCStd` files efficiently using zippey and enables meaningful diffs.

## Files Structure
- `models/` - Main FreeCAD files (.FCStd)
- `exports/step/` - STEP files for CAD interoperability  
- `exports/stl/` - STL files for 3D printing
- `documentation/` - Project documentation and images
- `drawings/` - Technical drawings and plans
- `scripts/` - Custom FreeCAD macros and scripts

## Design Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

## Key Components
| Component | File | Status |
|-----------|------|--------|
| Main Design | `models/{project-name}.FCStd` | 📝 Created by template |
| Additional Parts | `models/part1.FCStd` | ⏳ Add as needed |

## Manufacturing Notes
- Material specifications
- Tolerances
- Assembly instructions

## Version History
- v1.0 - Initial design
- v1.1 - Design improvements

## How It Works
- **zippey**: Efficiently stores FreeCAD files (which are zip files) in Git
- **zip diff**: Shows meaningful diffs of file contents instead of binary changes
- Run setup script once per machine for proper Git handling

## Troubleshooting
- If diffs don't work: Check zippey path in `git config --global --list`
- If files seem corrupted: Ensure setup script ran successfully on all machines
- Large files: Consider Git LFS for files >100MB

## License
This work is licensed under [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You are free to:
- Share and adapt the material

Under these terms:
- **Attribution** - Give appropriate credit
- **NonCommercial** - Not for commercial use