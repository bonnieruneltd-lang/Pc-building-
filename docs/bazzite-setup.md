# Bazzite setup: modded Minecraft with good graphics

Everything below assumes the hardware in [`../README.md`](../README.md) (AMD RDNA4 GPU, AM5 X3D CPU)
and a clean Bazzite 44 desktop install (Fedora-atomic base, kernel 7.2.x, Mesa 26.2.x, KDE Plasma 6.5
or GNOME). Commands are copy-paste ready.

---

## 1. Pick the right image and confirm the GPU stack

| Your GPU | Image to download | Why |
|---|---|---|
| **AMD Radeon (recommended, this build)** | `bazzite` (standard desktop, KDE or GNOME) | RDNA4 runs on in-tree `amdgpu` + Mesa RADV. Best-behaved path on Linux. |
| NVIDIA | `bazzite-nvidia` | Ships the proprietary driver; expect Wayland regressions (crashes/freezes reported through driver 580+ and 610.x). |

```bash
# confirm Mesa/RADV is driving the card (not llvmpipe!)
vulkaninfo --summary | grep -E 'deviceName|driverName|apiVersion'
# expect: deviceName = AMD Radeon RX 9070 XT (RADV GFX1201), driverName = radv
glxinfo -B | grep -E 'OpenGL renderer|OpenGL version'

# optional: is anything running on the CPU renderer by mistake?
DRI_PRIME= MESA_LOADER_DRIVER_OVERRIDE= glxinfo -B | grep renderer
```

If `vulkaninfo` shows `llvmpipe`, the game will run at 5 fps and look "broken". That is a driver
selection problem, not a hardware one.

**Optional but good on Bazzite:**

```bash
# MangoHud for in-game overlay (fps, frame time, GPU watts, VRAM, CPU per-core)
ujust install-mangohud        # or: flatpak install -y flathub org.freedesktop.Platform.VulkanLayer.MangoHud

# LACT: AMD GPU tuning (power cap, fan curve, undervolt) without Windows tools
ujust install-lact

# check what ujust offers on your image
ujust --choose
```

Bazzite ships a `sched_ext` CPU scheduler (SCX, e.g. `scx_lavd`) tuned for gaming; it noticeably helps
Minecraft's 1% lows because chunk-meshing threads compete with the world thread. Leave it enabled.

---

## 2. Install Prism Launcher (do not use the vanilla launcher)

Prism is the standard on Linux: per-instance Java, per-instance JVM args, per-instance memory, and it
handles Fabric/NeoForge/Quilt installs for you.

```bash
flatpak install -y flathub org.prismlauncher.PrismLauncher
flatpak run org.prismlauncher.PrismLauncher
```

If you keep instances on a second drive, grant the sandbox access once:

```bash
flatpak override --user --filesystem=/run/media/$USER/:/run/media/$USER/ \
  org.prismlauncher.PrismLauncher
```

In Prism: **Settings → Java** → let it download a runtime (**Java 21** for 1.21.x packs; **Java 25** if
the pack/loader demands it — Minecraft 26.x modpacks may require newer). Never point Prism at a
system JRE you layered in with `rpm-ostree`; it makes updates fragile on an immutable OS.

---

## 3. Memory and JVM arguments (the part most guides get wrong)

Set these **per instance**: *Edit → Settings → Memory / Java arguments*.

| Pack class | Heap (`-Xmx`) | Notes |
|---|---|---|
| Vanilla+ / light (Sodium, QoL) | 4–6 GB | more heap is slower, not faster |
| Medium (100–200 mods, no DH) | 8–10 GB | |
| Heavy (All the Mods class, 300+ mods) | **12 GB** (16 GB max) | the pack itself wants 12–16 GB |
| Heavy + Distant Horizons | 12 GB game heap | DH needs its own VRAM, not heap |

**JVM arguments — Java 21 (most 1.21.x packs):**

```
-XX:+UseZGC -XX:+ZGenerational -XX:+AlwaysPreTouch
-XX:+ParallelRefProcEnabled -XX:+PerfDisableSharedMem
-Dfile.encoding=UTF-8
```

**JVM arguments — Java 23+ (Minecraft 26.x era runtimes):** generational ZGC is the default, so the
generational flag is obsolete/removed:

```
-XX:+UseZGC -XX:+AlwaysPreTouch
-XX:+ParallelRefProcEnabled -XX:+PerfDisableSharedMem
-Dfile.encoding=UTF-8
```

Why: a 12 GB heap under the default collector causes multi-hundred-ms pauses when mods allocate
chunks — the classic "modded Minecraft stutter". ZGC keeps pauses sub-10 ms at the cost of a little
throughput, which is exactly the trade you want for a game that renders 60–240 times a second.

Sanity rule: **never set `-Xmx` above ~60% of installed RAM.** On 32 GB that means 16 GB is the hard
ceiling; 12 GB is the practical one.

---

## 4. The mod stack that produces "good graphics"

Install as a **Fabric** instance (or NeoForge if the pack requires it), then:

| Purpose | Mod | Notes |
|---|---|---|
| Renderer rewrite | **Sodium** | 2–5× vanilla FPS on its own; the single most important mod |
| Shader loader | **Iris** | loads OptiFine-style shader packs, but on a modern renderer |
| Shader pack | **Complementary Reimagined** (safe default) / **Photon** (crisp, bright) / **Solas** (stylised) / **Rethinking Voxels** (near-RT, heavy) | start at "High", step down to "Balanced" on Build C |
| Distance | **Distant Horizons** | LOD terrain far beyond render distance; wants **6 GB+ VRAM**, and it is the biggest visual win for the money |
| Textures | **Patrix 64x/128x** (paid) or **Stratum** / **Faithful 64x** | 128x + DH + heavy shaders is what eats your VRAM |
| QoL/perf | Lithium, FerriteCore, ModernFix, ImmediatelyFast, Entity Culling, Krypton (multiplayer) | cheap wins, install them all |
| Optional | Nvidium | **NVIDIA only** — irrelevant on this AMD build; Sodium already covers it |

> **Version trap (Nov 2026):** there is a known crash where the *newest* Sodium build is incompatible
> with Iris on Minecraft 26.3 (IrisShaders issue #3265). Pin a known-good pair — install the Iris
> version whose changelog lists your exact Sodium build — and keep a working instance as a backup
> before updating anything. Do not update Sodium and Iris independently on a pack you care about.

---

## 5. Tune in this order (biggest win per minute spent)

1. **Render distance** — the #1 CPU cost. 16 chunks is plenty when Distant Horizons is doing the far
   view; 32 chunks is where even an X3D part starts losing frames under mods.
2. **Shader preset** — drop from "Ultra" to "High" before you touch resolution. Most packs lose <10%
   of their look and gain 30–50% of their frame rate.
3. **Distant Horizons LOD radius / quality** — set *Quality* to Medium, LOD radius to 128–256 chunks,
   and turn **off** "Distant Generation" while exploring (it competes with the world thread for CPU).
   If you see stutter when crossing chunk borders, lower LOD radius first.
4. **Resource pack resolution** — 128x→64x is nearly free visually with shaders on and saves ~2–3 GB
   of VRAM.
5. **Sodium extras** — enable *Render Regions*, *Compact Vertex Format*, and set chunk update threads
   to `cores/2` (4 for the 8-core X3D). Leave "Use Persistent Mapping" on.

Cap the frame rate **slightly below** your refresh rate (e.g. 237 fps on a 240 Hz panel, or 120 on
144 Hz) using MangoHud's `fps_limit` or the driver's frame-rate target. An uncapped Minecraft shader
load spins the GPU and the fans for zero visible benefit.

---

## 6. HDR, VRR and per-game launch options

Bazzite's desktop session handles VRR/HDR in KDE Plasma 6.x, but Minecraft (a Java window) behaves
best launched through **gamescope** when you want HDR + integer scaling + a locked refresh:

```bash
# in Prism: Edit -> Settings -> Custom commands -> check "Custom command", then:
gamescope -W 2560 -H 1440 -r 240 -f --hdr-enabled --adaptive-sync -- %command%
```

Add MangoHud by prefixing instead of `%command%`:

```bash
mangohud --dlsym gamescope -W 2560 -H 1440 -r 240 -f --hdr-enabled --adaptive-sync -- %command%
```

Tips:
- For VRR flicker in dark caves, set the panel's VRR range in KDE display settings, not in-game.
- `MESA_VK_WSI_PRESENT_MODE=mailbox` as an environment variable in Prism gives lower-latency
  presentation on RADV when you are not using gamescope.
- Test 1440p first. 4K + 128x textures + DH is where 16 GB of VRAM becomes the limit on Build A/B.

---

## 7. Troubleshooting on Bazzite

| Symptom | Cause | Fix |
|---|---|---|
| 5–15 fps, fans silent | running on `llvmpipe` / software Vulkan | verify `vulkaninfo --summary`; check you are not on the NVIDIA image with an AMD card |
| Game crashes right after the shader loads | Sodium/Iris version mismatch (26.3 issue) | pin a known-good pair, test on a fresh profile, keep the old instance |
| Stutter every few seconds, then smooth | heap too small for the pack, or default GC | 12 GB heap + ZGC args (section 3) |
| Memory climbs for hours until the game dies | known Prism-on-Bazzite leak pattern (bazzite issue #4145) | cap `-Xmx`, and restart the instance between long sessions; watch RSS with `htop` |
| UI text tiny/blurry | Wayland fractional scaling (125%/150%) | use 100% or 200%, or run under gamescope with `-w 2560 -h 1440` |
| Controller not detected in Prism Flatpak | Flatpak sandbox device access | `flatpak override --user --device=all org.prismlauncher.PrismLauncher` |
| `flatpak` cannot see modpack exports | sandbox filesystem limits | add the path with `flatpak override --user --filesystem=...` |
| Shaders compile every launch | shader cache not persisted for the Flatpak | keep the cache inside the instance folder; do not clear it |

Backup habit: right-click an instance in Prism → **Export instance** → keep the `.mrpack`/zip on a
second drive. Modpack updates break worlds; exports are your undo button.

---

## 8. Launch-day checklist

```bash
# 1. system is current (Bazzite 44 has a GUI updater; CLI equivalent:)
ujust update

# 2. GPU stack is sane
vulkaninfo --summary | grep -E 'deviceName|driverName'

# 3. launcher exists and can see the disk you keep instances on
flatpak run org.prismlauncher.PrismLauncher

# 4. per-instance: Java 21 (or 25), 12 GB heap, ZGC args, Sodium + Iris + DH, 16-chunk render distance
# 5. cap fps just under your refresh rate, then push settings up one notch at a time
```

