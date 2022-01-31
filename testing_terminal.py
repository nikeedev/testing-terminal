import os, getpass, time

version = "0.0.1"
build_date = "2022.1"
running = True


print(f"\n\n\nTesting Terminal v{version}, Build {build_date}, userId: {getpass.getuser()} \n\n")

while running:
    commands = input(f"{getpass.getuser()} [-> ")
