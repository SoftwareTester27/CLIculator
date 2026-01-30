# CLIculator

Say goodbye to the drab default calculator haunting your command line—CLIculator explodes onto your terminal with a rainbow of colors, intuitive vibes, and zero-fuss math magic that makes calculations feel like a party, not a chore!

![CLIculator Demo](https://github.com/user-attachments/assets/957e5a8a-4827-4276-8061-981d0bcd5565)

## 🌈 Why CLIculator Rocks

Tired of that ugly, black-and-white cmd calculator that looks like it was designed in the stone age? CLIculator upgrades your terminal from boring to brilliant with:

- **Vibrant Visual Flair**: Rainbow gradients, syntax-highlighted ops (like + in fiery red for that addition thrill!), and rich panels that make math pop—no more squinting at plain text.
- **Intuitive, Menu-Driven UX**: Jump into basics, shapes, percentages, or temp conversions with simple key presses. Handles BODMAS expressions effortlessly, no complex commands needed.
- **Zero-Fuss Portability**: Pure Python script runs anywhere Python 3+ lives—Windows, Mac, Linux. Download, run, calculate. No heavy setups, just instant fun.

Teaser: Imagine your terminal lighting up like a disco—[check this GIF for the glow-up](https://github.com/user-attachments/assets/a8f5d986-0a04-4c83-807b-380872decc33)!

## 🚀 Getting Started

Fire up the party in under a minute—no PhD in terminals required. (Python 3.6+ needed for the color magic.)

1. **Grab the Script**: Download `CLIculatorv2.py` from the repo (ignore the old v1.1—v2's got the upgrades!).
2. **Install Dependencies** (one-time zap): Open your terminal and run:
   ```
   pip install colorama rich
   ```
   (These handle the eye-candy; the script assumes they're there.)
3. **Launch the Fun**: In the folder with the file, type:
   ```
   python CLIculatorv2.py
   ```
   Boom—gradient title waves in, menu awaits!

No installs? Just drag-and-drop to a Python-enabled spot and run. Pro tip: If colors look wonky, ensure your terminal supports ANSI (most do).

## 🎯 Usage Examples

CLIculator's all about that playful flow: Pick from the home menu (1-5 for features), enter values, get colorful results. Errors? Friendly nudges, no crashes. Here's the vibe in action (simulated with ANSI escapes—your terminal will shine brighter!):

### Basic Calculations (Option 1)
Enter expressions like `2+3*4`—it auto-handles order with BODMAS.

```
[Gradient Title Appears...]

                    ├─►2+3*4  (In electric blue prompt)

                    └─Result is► 14  (In glowing green)
```

Press Enter to recalculate or `<` to bounce back.

### Area/Perimeter (Option 2)
Pick shape (1-4), input sides—results in bold cyan.

Example: Square (ID 1), side 5:
```
     Enter Side: 5

     The Requested Results are: Area = 25 units Perimeter = 20 units  (Bright white on black)
```

### Percentage Calc (Option 3)
"What percent is X of Y?"—super simple.

Example: 25 of 100:
```
     ╰─► 25 is what percent of 100

     25 is 25.0 percent of 100  (Style.BRIGHT highlight)
```

### Odd/Even Check (Option 4)
Quick parity party.

Example: Input 7:
```
     ╰─Number to calculate► 7

     Number is odd  (Bold magenta)
```

### Temp Conversion (Option 5)
C to F or vice versa.

Example: C, input 0:
```
     ╰─ID►C
     ╰─Number►0

     The Requested result is: 32.0°F  (Vibrant cyan)
```

Easter eggs? Type `?` for help, `S` for support (opens GitHub), or secret codes for web surprises. Exit with `x` anytime.

## ✨ What's Under the Hood (Briefly)

CLIculator's a lightweight Python script blending `colorama` for ANSI colors, `rich` for fancy console output, and built-ins like `re` for expression parsing and `math` for shapes/temps. Evolved from v1.1 to v2 for snappier gradients and expression smarts—runs cross-platform without bloat. Tinker away; it's all in one file!

## 📄 License & Shoutouts

This project is licensed under the Other License—feel free to use, modify, and share as long as you keep the credits intact.

Made with ❤️ by [SoftwareTester27](https://github.com/SoftwareTester27)—fork it, star it, or suggest wilder colors! Let's make terminals fun for everyone. 🚀
