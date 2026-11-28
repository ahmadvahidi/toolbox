#!/usr/bin/env python3
"""blender_skills job — one real Blender artifact per run (vertical 720x1280 still).

Uses the blender-skills pack's rules in practice: a hero prop, 3-point studio light,
Cycles on CPU, no texture downloads. Blender 5.3 portable lives at /opt/data/bin.
"""
from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

BLENDER = "/opt/data/bin/blender-5.3.0-linux-x64/blender"

SCENE = r'''
import bpy, math
from mathutils import Vector

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = 64
sc.cycles.use_denoising = True
sc.render.resolution_x = 720
sc.render.resolution_y = 1280
sc.render.image_settings.file_format = "PNG"
sc.render.filepath = "{out}"

def mat(name, base, rough=0.4, metal=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    return m

ceramic = mat("Ceramic", (0.10, 0.42, 0.62), 0.22)
stone = mat("Stone", (0.30, 0.29, 0.28), 0.8)

bpy.ops.mesh.primitive_cylinder_add(radius=0.17, depth=0.09, location=(0, 0, 0.045))
ped = bpy.context.object; ped.data.materials.append(stone)
bev = ped.modifiers.new("Bevel", "BEVEL"); bev.width = 0.005; bev.segments = 3

bpy.ops.mesh.primitive_cylinder_add(radius=0.055, depth=0.16, location=(0, 0, 0.17),
                                    vertices=64, end_fill_type="NOTHING")
body = bpy.context.object; body.data.materials.append(ceramic)
sol = body.modifiers.new("Solidify", "SOLIDIFY"); sol.thickness = 0.006; sol.offset = -1
bev = body.modifiers.new("Bevel", "BEVEL"); bev.width = 0.004; bev.segments = 3
bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_circle_add(radius=0.055, fill_type="NGON", location=(0, 0, 0.092), vertices=64)
bot = bpy.context.object; bot.data.materials.append(ceramic)

bpy.ops.mesh.primitive_torus_add(major_radius=0.032, minor_radius=0.007,
                                 major_segments=48, minor_segments=16,
                                 location=(0.062, 0, 0.175), rotation=(math.radians(90), 0, 0))
h = bpy.context.object; h.data.materials.append(ceramic); bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, -0.001))
fl = bpy.context.object; fl.data.materials.append(mat("Backdrop", (0.035, 0.045, 0.06), 0.9))

def light(name, loc, energy, size, target=(0, 0, 0.18)):
    d = bpy.data.lights.new(name, "AREA"); d.energy = energy; d.size = size
    o = bpy.data.objects.new(name, d); bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

light("Key", (0.55, -0.6, 0.85), 55, 1.0)
light("Fill", (-0.7, -0.35, 0.35), 14, 1.2)
light("Rim", (-0.2, 0.65, 0.55), 45, 0.5)

w = bpy.data.worlds.new("W"); w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.015, 0.02, 0.03, 1)
sc.world = w

cd = bpy.data.cameras.new("Cam"); cd.lens = 60
cam = bpy.data.objects.new("Cam", cd); bpy.context.collection.objects.link(cam)
cam.location = (0.30, -0.52, 0.34)
tgt = Vector((0, 0, 0.155))
cam.rotation_euler = (tgt - cam.location).to_track_quat("-Z", "Y").to_euler()
sc.camera = cam
bpy.ops.render.render(write_still=True)
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
        fh.write(SCENE.format(out=str(out)))
        script = fh.name
    r = subprocess.run([BLENDER, "-b", "--factory-startup", "--python", script],
                       capture_output=True, text=True, timeout=900)
    ok = out.exists() and out.stat().st_size > 20000
    print(f"blender job: {'ok' if ok else 'FAILED'} -> {out} ({out.stat().st_size if out.exists() else 0} B)")
    if not ok:
        print(r.stdout[-800:])
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
