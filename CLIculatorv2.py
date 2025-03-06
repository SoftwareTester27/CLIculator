# import typer
from colorama import Fore, Back, Style
import colorama
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.traceback import install
import webbrowser
import os
import time
install()

console = Console()

text = Text()
text.append("This is a sample text with ", style="default")
text.append("/forward/", style="default")
text.append("slashes/", style="default")

console.print(text)

# Defining variables to avoid errors
ans = 0
uc = 'x'
n1 = 0
n2 = 0

os.system("mode con: cols=134 lines=40")
os.system('title "                                                                                                                                            CLIculator                                                                                                           "')

def rgb_to_ansi256(r, g, b):
    """Convert RGB to the closest ANSI 256-color code."""
    return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)

def apply_smooth_gradient(text, start_color, end_color):
    """Applies a smooth left-to-right gradient using ANSI 256 colors."""
    gradient_text = ""
    length = len(text)

    for i, char in enumerate(text):
        factor = i / max(length - 1, 1)  # Normalize factor from 0 to 1
        r = int(start_color[0] + (end_color[0] - start_color[0]) * factor)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * factor)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * factor)

        ansi_code = rgb_to_ansi256(r, g, b)
        gradient_text += f"\033[38;5;{ansi_code}m{char}"  # Apply color per character

    gradient_text += "\033[0m"  # Reset color
    return gradient_text


# Converting temp scales
def gradient_title(title_lines, colors):
    colorama.init()
    num_lines = len(title_lines)
    num_segments = len(colors) - 1  # Number of color transitions
    segment_size = max(1, num_lines // num_segments)  # Avoid division errors

    for i, line in enumerate(title_lines):
        # Find which color segment we are in
        segment = min(i // segment_size, num_segments - 1)
        start_rgb = colors[segment]
        end_rgb = colors[segment + 1]
        
        # Interpolate colors within the segment
        factor = (i % segment_size) / max(1, segment_size - 1)
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * factor)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * factor)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * factor)

        # Apply ANSI color
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + line + Style.RESET_ALL)

# Your title as a list of lines
title_lines = [
    "                     ┌──────────────────────────────────────────────────────────────────────────────────────────┐                     ",
    "                     │                                                                                          │                     ",
    "                     │     ▄████▄   ██▓     ██▓ ▄████▄   █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███      │                     ",
    "                     │    ▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒    │                     ",
    "                     │    ▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒    │                     ",
    "                     │    ▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄      │                     ",
    "                     │    ▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒    │                     ",
    "                     │    ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░    │                     ",
    "                     │                                       [DeveloperKartik]                                  ├──┐                  ",
    "                     └──────────────────────────────────────────────────────────────────────────────────────────┘  │                  ",
    "                                                                                                                   │                  ",
    Fore.LIGHTRED_EX + "                  ┌────────────[" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit─────────────────────────[" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help──────────────────────────────[" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] Support──┘",
    Fore.LIGHTRED_EX + "                  │                  ",
    Fore.LIGHTRED_EX + "                  └─┬────────────────────────────────"
]

# [" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit │ [" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help │ [" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] 😎 Support        │                  |  _  | |_| | |  | | |___")
#     print("                     ├──────┬───┴──────────┴───────────────────────┤                  |_| |_|\___/|_|  |_|_____|")
#     print("                     │ [" + Fore.LIGHTRED_EX + "/1" + Fore.LIGHTRED_EX + "] | Basic Calculations                   │                  ")
#     print("                     ├──────┼──────────────────────────────────────┤")
#     print("                     │ [" + Fore.LIGHTRED_EX + "/2" + Fore.LIGHTRED_EX + "] | Calculate area and perimeter of      │")
#     print("                     │      | various shapes                       │")
#     print("                     ├──────┼──────────────────────────────────────┤")
#     print("                     │ [" + Fore.LIGHTRED_EX + "/3" + Fore.LIGHTRED_EX + "] | Calculate Percentage of a number     │")
#     print("                     ├──────┼──────────────────────────────────────┤")
#     print("                     │ [" + Fore.LIGHTRED_EX + "/4" + Fore.LIGHTRED_EX + "] | Check if number is Odd or Even       │")
#     print("                     ├──────┼──────────────────────────────────────┤")
#     print("                     │ [" + Fore.LIGHTRED_EX + "/5" + Fore.LIGHTRED_EX + "] | Change Temperature Units

# @app.command(short_help="Basic Calculations")
def f5():
    print(end="\033c", flush=True)
    print(" ")
    gradient_title(title_lines, (128, 0, 128), (0, 255, 255))
    print("     ")
    print("     ")
    print(Fore.LIGHTRED_EX +"     ╭──────┬──────────────────────────────────────╮")
    print("     │  Id  |               Function               │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "C" + Fore.LIGHTRED_EX + "]  | Celsius to Farenhiet                 │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "F" + Fore.LIGHTRED_EX + "]  | Farenhiet to Celsius                 │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    tans = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─ID>")
    print("     │")
    ideg = int(input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─Number>"))
    if tans == 'c' or tans == 'C':
        degree = ideg * 1.8 + 32
        print(" ")
        print(Style.BRIGHT + f'     The Requested result is: {degree}°F')
        print(" ")
        input(Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif tans == 'f' or tans == 'F':
        degree = ideg - 32 / 1.8
        print(Style.BRIGHT + f"     The Requested result is: {degree}°C")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press enter to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

# checking if a number is odd or even

def f4():
    print(end="\033c", flush=True)
    print(" ")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])    
    print("     ")
    print(Fore.LIGHTRED_EX +"     ╭─────────────────────────────────────────────╮")
    print("     │                 Odd or Even                 │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├─────────────────────────────────────────────╯")
    print("     │")
    ooe = int(input(Style.BRIGHT +"     ╰─Number to calculate> "))

    if ooe % 2 == 0:
        print(Style.BRIGHT + "     Number is even")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif ooe % 2 == 1:
        print(Style.BRIGHT + "     Number is odd")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

# Defining all basic cals like DivMulAddSub.

def f1():
    # print('\n' * os.get_terminal_size().lines)
    print(end="\033c", flush=True)
    ans = 0
    uc = 0
    print("")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])                                                                                                                      
    print("     ")
    print("     ")
    print(Fore.LIGHTRED_EX +"     ╭─────────────────────────────────────────────╮")
    print("     │             Basic Calculations              │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "+" + Fore.LIGHTRED_EX + "]  | Addition                             │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "-" + Fore.LIGHTRED_EX + "]  | Subtraction                          │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "*" + Fore.LIGHTRED_EX + "]  | Multiplication                       │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "/" + Fore.LIGHTRED_EX + "]  | Division                             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uc = 0
    uc = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─ID>")

    if uc == "+" or uc == "-" or uc == "*" or uc == "/" or uc == "<":
        if uc == '+':
            print("     Selected: Addition")
        elif uc == '-':
            print("     Selected: Subtraction")
        elif uc == '*':
            print("     Selected: Multiplication")
        elif uc == '/':
            print("     Selected: Division")
        elif uc == '<':
            print(end="\033c", flush=True)
            maincode()
    else:
        print(" ")
        print(Fore.RED + Style.BRIGHT + "     Invalid Choice")
        print(" ")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to rerun")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()

    print("     │")

    n1 = int(input(Style.BRIGHT + "     ╰─First Number>"))
    print("     │")
    n2 = int(input("     ╰─Second Number>"))
    print(" ")

    if uc == '+':
        ans = n1 + n2
    elif uc == '-':
        ans = n1 - n2
    elif uc == '*':
        ans = n1 * n2
    elif uc == '/':
        ans = n1 / n2

    print(Style.BRIGHT + "     The requested answer is: " + Fore.CYAN + str(ans))
    print(" ")
    input(Style.BRIGHT + Fore.MAGENTA + "       Press Enter ←╯ to rerun")
    # Calling Maincode
    print(end="\033c", flush=True)
    maincode()

# Code For calculating area and perimeter
def f2():
    import math
    print(end="\033c", flush=True)
    print("")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])                                                                                                                        
    print("     ")
    print("     ")
    print(Fore.LIGHTRED_EX +"     ╭─────────────────────────────────────────────╮")
    print("     │               Area Calculator               │")
    print("     ├─────────────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "<" + Fore.LIGHTRED_EX + "]  Go Back                                │")
    print("     ├──────┬──────────────────────────────────────┤")
    print("     │  Id  |               Function               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "1" + Fore.LIGHTRED_EX + "]  | Sqaure                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "2" + Fore.LIGHTRED_EX + "]  | Rectangle                            │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "3" + Fore.LIGHTRED_EX + "]  | Circle                               │")
    print("     ├──────┼──────────────────────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "4" + Fore.LIGHTRED_EX + "]  | Triangle                             │")
    print("     ├──────┴──────────────────────────────────────╯")
    print("     │")
    uf = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─ID> ")
    # console = Console()
    # console.print(table)
    # print(" ")
    # defining crv to prevent errors
    crv = int(0)

    if uf == '1':
        sside = int(input(Style.BRIGHT + "     Enter Side: "))
        # Calculates using the "side x 4 and side x side" method.
        peri = sside * 4
        area = sside * sside
        # Prints the result
        print(Style.BRIGHT + f"     The Requested Results are: Area = {area} units Perimeter = {peri} units")
        input(Style.BRIGHT + Fore.MAGENTA + "     Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '2':
        rl = int(input(Style.BRIGHT + "     Enter Rect Length:"))
        rb = int(input(Style.BRIGHT + "     Enter Rect Breadth:"))
        # Calculates using the "l + b * 2 and l x b" method.
        area = rl * rb
        peri = 2 * (rl + rb)
        # Prints the result
        print(Style.BRIGHT + f"      The Requested Results are: Area = {area} units Perimeter = {peri} units")
        input(Fore.MAGENTA + Style.BRIGHT + "        Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '3':
        crv = int(input("      Enter radius to calculate: "))
        rans = math.pi * crv * crv
        # Prints the result
        print(Style.BRIGHT + "     The Requested result is: " + Fore.CYAN + str(rans) + " units")
        input(Fore.MAGENTA + Style.BRIGHT + "     Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '4':
        tsa = int(input(Style.BRIGHT + "     First side: "))
        tsb = int(input(Style.BRIGHT + "     Second side: "))
        tsc = int(input(Style.BRIGHT + "     Third side: "))
        # Calculates using the formulas but implemented in python using math.sqrt()
        ts = tsa + tsb + tsc / 2
        aot = math.sqrt(ts*(ts-tsa)*(ts-tsb)*(ts-tsc))

        # Prints the result
        
        print(Style.BRIGHT + "      The Requested result is: " + Fore.CYAN + Back.BLACK +  str(int(aot)))
        print(Style.RESET_ALL)
        input(Fore.MAGENTA + Style.BRIGHT + "       Press Enter ←╯ to go back")
        # Calling Maincode
        print(end="\033c", flush=True)
        maincode()
    elif uf == '<':
        print(end="\033c", flush=True)
        maincode()

# Code for calcing percent
def f3():
    print(end="\033c", flush=True)
    print(" ")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])                                                                                                                        
    print("     ")
    print("     ")
    print(Fore.LIGHTRED_EX +"     ╭─────────────────────────────────────────────╮")
    print("     │            Percentage Calculator            │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit │ [" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help │ [" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] 😎 Support        │")
    print("     ├──────────┴──────────┴───────────────────────╯")
    print("     │")

    ntcp = input(Fore.LIGHTRED_EX + Style.BRIGHT + "     ╰─> ___ is what percent of ")
    if ntcp == "x":
        quit()

    print(end="\033c", flush=True)

    print(" ")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])                                                                                                                       
    print(Fore.LIGHTRED_EX +"     ")
    print("     ")
    print("     ╭──────────────────────────────────────────────╮")
    print("     │            Percentage Calculator            │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit │ [" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help │ [" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] 😎 Support        │")
    print("     ├──────────┴──────────┴───────────────────────╯")
    print("     │")

    ul = f"     ╰─> {ntcp} is what percent of "
    nfrom = input(ul)

    print(end="\033c", flush=True)

    print(" ")
    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])                                                                                                                       
    print("     ")
    print("     ")
    print("     ╭─────────────────────────────────────────────╮")
    print("     │            Percentage Calculator            │")
    print("     ├──────────┬──────────┬───────────────────────┤")
    print("     │ [" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit │ [" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help │ [" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] 😎 Support        │")
    print("     ├──────────┴──────────┴───────────────────────╯")
    print("     │")
    print(f"     ├─> {ntcp} is what percent of {nfrom}")
    print(" ")

    result = int(ntcp) / int(nfrom) * 100

    print(Style.BRIGHT + f"     {ntcp} is {result} percent of {nfrom}")
    input(Fore.MAGENTA + Style.BRIGHT + "     Press Enter ←╯ to go back")

    # Calling Maincode
    print(end="\033c", flush=True)
    maincode()

# Main Code
def maincode():
    print(" ")
    # console.print("                                             ╔╦╗┌─┐┬  ┬┌─┐┬  ┌─┐┌─┐┌─┐┬─┐╦╔═┌─┐┬─┐┌┬┐┬┬┌─┌─┐", style="bold rgb(177,252,200)")
    # console.print("                                              ║║├┤ └┐┌┘├┤ │  │ │├─┘├┤ ├┬┘╠╩╗├─┤├┬┘ │ │├┴┐└─┐", style="bold rgb(165,252,191)")
    # console.print("                                             ═╩╝└─┘ └┘ └─┘┴─┘└─┘┴  └─┘┴└─╩ ╩┴ ┴┴└─ ┴ ┴┴ ┴└─┘", style="bold rgb(148,233,174)")
    # console.print("      ________  ___       ___  ________  ___  ___  ___       ________  _________  ________  ________  ___      ___  _______      ", style="bold #FF0000")
    # console.print("     |\   ____\|\  \     |\  \|\   ____\|\  \|\  \|\  \     |\   __  \|\___   __\|\   __  \|\   __  \|\  \    /  /|/  ___  \     ", style="bold #FE6900")
    # console.print("     \ \  \___|\ \  \    \ \  \ \  \___|\ \  \ \  \ \  \    \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \  /  / /__/|_/  /|    ", style="bold #FEE400")
    # console.print("      \ \  \    \ \  \    \ \  \ \  \    \ \  \ \  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \ \   _  _\ \  \/  / /|__|//  / /    ", style="bold #2BFE00")
    # console.print("       \ \  \____\ \  \____\ \  \ \  \____\ \  \ \  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \ \  \ \  \ \    / /     /  /_/__   ", style="bold #00BAFE")
    # console.print("        \ \_______\ \_______\ \__\ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\ \ _\ \__/ /     |\________\ ", style="bold #004DFE")
    # console.print("         \|_______|\|_______|\|__|\|_______|\|_______|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|\|__|/       \|_______| ", style="bold #4900FE")                                                                                                                       

    gradient_title(title_lines, [(255, 102, 0), (255, 51, 51), (255, 0, 102)])
    # for line in title_lines:
    #     print(apply_smooth_gradient(line, (255, 102, 0), (255, 0, 102)))
    # gradient_title(title_lines, (138, 43, 226), (0, 206, 209), (255, 0, 255))
    print(Fore.LIGHTRED_EX + """
                    │
                    ├─[1] Basic Calculations
                    │
                    ├─[2] Calculate area and perimeter of various shapes
                    │
                    ├─[3] Calculate Percentage of a number
                    │
                    ├─[4] Check if number is Odd or Even
                    │
                    ├─[5] Change Temperature Units
                    │""")
    # print(Fore.LIGHTRED_EX + "                     ┌──────┬──────────────────────────────────────╮                   _   _  ___  __  __ _____ ")
    # print("                     │  Id  |               Function               │                  | | | |/ _ \|  \/  | ____|")
    # print("                     ├──────┴───┬──────────┬───────────────────────┤                  | |_| | | | | |\/| |  _| ")
    # print("                     │ [" + Fore.LIGHTRED_EX + "x" + Fore.LIGHTRED_EX + "] Exit │ [" + Fore.LIGHTRED_EX + "?" + Fore.LIGHTRED_EX + "] Help │ [" + Fore.LIGHTRED_EX + "S" + Fore.LIGHTRED_EX + "] 😎 Support        │                  |  _  | |_| | |  | | |___")
    # print("                     ├──────┬───┴──────────┴───────────────────────┤                  |_| |_|\___/|_|  |_|_____|")
    # print("                     │ [" + Fore.LIGHTRED_EX + "/1" + Fore.LIGHTRED_EX + "] | Basic Calculations                   │                  ")
    # print("                     ├──────┼──────────────────────────────────────┤")
    # print("                     │ [" + Fore.LIGHTRED_EX + "/2" + Fore.LIGHTRED_EX + "] | Calculate area and perimeter of      │")
    # print("                     │      | various shapes                       │")
    # print("                     ├──────┼──────────────────────────────────────┤")
    # print("                     │ [" + Fore.LIGHTRED_EX + "/3" + Fore.LIGHTRED_EX + "] | Calculate Percentage of a number     │")
    # print("                     ├──────┼──────────────────────────────────────┤")
    # print("                     │ [" + Fore.LIGHTRED_EX + "/4" + Fore.LIGHTRED_EX + "] | Check if number is Odd or Even       │")
    # print("                     ├──────┼──────────────────────────────────────┤")
    # print("                     │ [" + Fore.LIGHTRED_EX + "/5" + Fore.LIGHTRED_EX + "] | Change Temperature Units             │")
    # print("                     ├──────┴──────────────────────────────────────╯")
    # print("                     │")
    uc = 0
    uc = input(Fore.LIGHTRED_EX + Style.BRIGHT + "                    └─>")
    # print(" ")
    # table = Table(title="     Function Table:", style="cyan")
    # table.add_column("Id", style="red", justify="center")
    # table.add_column("Function", style="green")
    # table.add_row("/1", "Basic Calculations")
    # table.add_row("/2", "Calculate area and perimeter of various shapeaas")
    # table.add_row("/3", "Calculate Percentage of a number")
    # table.add_row("/4", "Check if number is Odd or Even")
    # table.add_row("/5", "Change Temperature Units")
    # table.add_row("r", "Re-runs the program")
    # table.add_row("x", "Exit the program")
    # table.add_row("?", "For list of commands")
    # console = Console()
    # console.print(table)

    if uc == '/1':
        f1()
    elif uc == '/2':
        f2()
    elif uc == '/3':
        f3()
    elif uc == '/4':
        f4()
    elif uc == '/5':
        f5()
    elif uc == 'THEBESTWEBSITEEVER':
        print(end="\033c", flush=True)
        # Calling Maincode
        # maincode()
        webbrowser.open('https://softwaretester27.github.io/learnscratch3/Index.html')
        maincode()
    elif uc == '?':
        print(end="\033c", flush=True)
        os.system("mode con: cols=134 lines=40")
        print(" ")
        print("     To use the program enter the id from the ")
        print("     table given below corresponding to the ")
        print("     function you want to perform.")
        # Calling Maincode
        maincode()
        print(" ")
    elif uc == 'x':
        print(end="\033c", flush=True)
        quit()
    elif uc == 'S':
        print(end="\033c", flush=True)
        # Calling Maincode
        # maincode()
        webbrowser.open('https://github.com/SoftwareTester27')
        maincode()
    else:
        secondstoend = 5
        for number in range(5):
            print(end="\033c", flush=True)
            print(f"     Invalid fact '{uc}'. Please Re-run to retry or enter '?' in the first input asked.")
            print(f"     Restarting in {secondstoend} seconds...")
            time.sleep(1)
            secondstoend = secondstoend-1
        
        # Clearing the screen before calling maincode
        print(end="\033c", flush=True)
        # Calling Maincode
        maincode()
# Start the program
print(end="\033c", flush=True)
maincode()