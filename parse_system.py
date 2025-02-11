"""
This script is used to parse the system and print the classes in each file.
"""
import subprocess
import pathlib
import shutil
import ast
from diagrams import Diagram, Edge
from diagrams.custom import Custom
from  pyflowchart import Flowchart
from pyflowchart import output_html






def parse_system(root_dir: pathlib.Path, format_output: str = "dot", output_dir: pathlib.Path = pathlib.Path("dot_inputs")):
    """
    Parse all the dot files in the root_dir and print the classes in each file.
    """
    map_files_with_directory = {}
    output_dir = output_dir / root_dir.name
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in root_dir.glob("**/*.py"):
        directory_only = file.relative_to(root_dir)
        directory = directory_only.parent
        map_files_with_directory[file] = directory

    for file, directory in map_files_with_directory.items():
        new_dir = output_dir / directory
        new_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pyreverse", "-o", format_output, "-p", directory, "-d", new_dir, file], check=True)



def parse_system_with_diagrams(root_dir: pathlib.Path, format_output: str = "png", output_dir: pathlib.Path = pathlib.Path("dot_inputs")):
    """
    Parse all the dot files in the root_dir and print the classes in each file.
    """
    map_files_with_directory = {}
    output_dir = output_dir / root_dir.name
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in root_dir.glob("**/*.py"):
        directory_only = file.relative_to(root_dir)
        directory = directory_only.parent
        map_files_with_directory[file] = directory
    

    for file, directory in map_files_with_directory.items():
        new_dir = output_dir / directory
        new_dir.mkdir(parents=True, exist_ok=True)
        with Diagram(file.name, show=False, direction="TB", filename=file.name.replace(".py", "")):
            custom_nodes = {
                "agents": Custom("agent","res\\icons\\agent.png"),
                "config": Custom("config","res\\icons\\config.png"),
                "models": Custom("models","res\\icons\\models.png"),
                "notebooks": Custom("notebooks","res\\icons\\notebooks.png"),
                "scripts": Custom("scripts","res\\icons\\script.png"),
                "test": Custom("tests","res\\icons\\test.png"),
                "utils": Custom("utils","res\\icons\\utils.png"),
                "train": Custom("train","res\\icons\\train.png"),


            }
            if directory in custom_nodes:
                custom_nodes[directory] >> Edge(color="darkgreen")
        # move png file to the new_dir
        shutil.move(file.name.replace(".py", ".png"), new_dir / file.name.replace(".py", ".png"))


def parse_system_with_diagrams_and_flowchart(root_dir: pathlib.Path, output_dir: pathlib.Path = pathlib.Path("dot_inputs")):
    """
    Parse all the dot files in the root_dir and print the classes in each file.
    """
    map_files_with_directory = {}
    output_dir = output_dir / root_dir.name
    output_dir.mkdir(parents=True, exist_ok=True)
    for file in root_dir.glob("**/*.py"):
        directory_only = file.relative_to(root_dir)
        directory = directory_only.parent
        map_files_with_directory[file] = directory
    
    for file, directory in map_files_with_directory.items():
        new_dir = output_dir / directory
        new_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                print(f"Skipping empty file: {file}")
                continue

            # Check for syntax errors
            try:
                ast.parse(content)
            except SyntaxError as syntax_err:
                print(f"Skipping file {file} due to syntax error: {syntax_err}")
                continue

            flowchart = Flowchart.from_code(content, simplify=False)
            output_html((new_dir / file.name.replace(".py", ".html")).resolve(), directory.name, flowchart.flowchart())

        except AssertionError as e:
            print(f"Skipping file {file} due to parsing error: {e}")
        except Exception as e:
            print(f"Unexpected error with file {file}: {e}")
    








if __name__ == "__main__":
    # parse_system(pathlib.Path(__file__).parent.parent / "solidity_rl", format_output="png", output_dir=pathlib.Path("output"))
    # parse_system_with_diagrams(pathlib.Path(__file__).parent.parent / "solidity_rl", format_output="png", output_dir=pathlib.Path("output"))
    parse_system_with_diagrams_and_flowchart(pathlib.Path(__file__).parent.parent / "solidity_rl", output_dir=pathlib.Path("output"))
