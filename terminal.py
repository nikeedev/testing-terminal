import os, getpass, time

version = "0.0.1"
build_date = "2022.1"
running = True


print(f"\n\n\nTesting Terminal v{version}, Build {build_date}, userId: {getpass.getuser()} \n\n")

while running:
    commands = input(f"{getpass.getuser()} [-> ")
    if "vim" in commands:
        try:
            os.system("vim")
        except SyntaxError:
            print("Vim isn't installed")

    if "say" in commands:
        sayword = input("What to say? ")
        print(f"\n\n\n\{sayword}")

    if "help" in commands:
        print("You can write 'say': to print what you wrote")
        print("'vim': to run Vi IMporved")