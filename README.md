# Blender Sculpting Layers
Blender Addon for None-Destructive Sculpting Workflow

This Addon is Still in Development Please Report Bugs to Help Improve This Addon

## Preview

---

 ![Alt text](https://github.com/FadiMHussein/blender-sculpting-layers/raw/main/preview.gif "Sculpting Layer Addon Preview")

### Installation

---

- Download the release  
- Install the addon
- Under Preferences -> Addons 
  - Enable Addon ( Sculpting Layer )
- Addon will be available in Sculpting Mode
- Enjoy...........

### Usage

---

A Wiki is being worked on .....

### Tested Versions

---
- Blender 2.83 (LTS) / MultiRes Will Not Work Due to Modifier Behaviour ( Does not have "sculpt" mode preview )
- Blender 2.92


## Roadmap

---

> - [x] Working
> - [ ] Still in Development
  
- [x] Single Resolution 
  - [x] Adding Layers
  - [x] Removing Layers
  - [x] Applying Layers
  - [x] Recording on Layers
  - [x] Hiding/Showing Layers
  - [x] Changing Layers Weight
    
- [ ] Multiple Resolution
  - [x] Adding Modifier
  - [x] Increasing/Decreasing Resolution
  - [x] Changing Resolution from Panel
  - [x] Applying/Removing Configurations
  - [ ] Adding Layers
  - [ ] Removing Layers
  - [ ] Applying Layers
  - [ ] Recording on Layers
  - [ ] Hiding/Showing Layers
  - [ ] Changing Layers Weight

### Not Tested

---

- Interactions with Shape Keys
- Heavy Sculpting Performance
- Interactions with Modifiers ( Should be minimal )

### Known Issues

---

> - [x] Fixed
> - [ ] Not Fixed
> - [ ] _Does Not Affect Actual Workflow_

- [ ] _Apply a Layer does not Apply the Relative Shape Key ( You need to Apply the Last Shape Key or 
  Apply All to Actually Apply Keys to the Original Mesh Data )_

### Future Development

---

- Work with actual Mesh Data instead of using Shape Keys for Single Resolution
- Work with Displacement Data for Multi Resolution ( Now uses proxy Object with Shape Keys )