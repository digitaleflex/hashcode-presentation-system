# HashCode Reboot — Brand Assets

This directory contains the production brand assets used by the **HashCode Presentation System**.

## Production asset

- `hashcode-reboot-logo.webp` — approved raster logo used by Slidev layouts and presentation surfaces.

## Asset policy

The generated SVG logo files are **not approved for production use** because their gradient rendering does not match the supplied HashCode Reboot visual.

Do not reference the generated SVG files in new slides or components.

Until an official vector version is supplied, the presentation system must use:

```
/brand/hashcode-reboot-logo.webp
```

## Usage rules

Use the approved logo for covers, headers, section slides and major brand moments.

Keep adequate clear space around the logo and do not recreate its gradient or geometry in CSS/SVG.
