import os, getpass

version = "0.0.1"
build_date = "2022.1"
running = True


print(f"Testing Terminal v{version}, Build {build_date}, userId: {getpass.getuser()}")

while running:
    commands = input(f"{getpass.getuser()} --> ")
