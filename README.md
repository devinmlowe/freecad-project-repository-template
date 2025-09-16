# [Project Name]

## Project Overview
Brief description of what this project creates/designs.

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
| Main Assembly | `models/assembly.FCStd` | ⏳ In Progress |
| Part 1 | `models/part1.FCStd` | ✅ Complete |

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