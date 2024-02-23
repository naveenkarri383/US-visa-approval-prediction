import os  # to create folder and files in the current directory 
from pathlib import Path

project_name="us_visa_application"  # Root folder name 

#creating files
list_of_files=[

    f"{project_name}/__init__.py",  # constructor file to make project_name (root folder)to make a local package
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_injestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"

]

# code to import all the mentioned above files

for filepath in list_of_files:
    filepath=Path(filepath) # Coverting everything to a file path    
    filedir,filename=os.path.split(filepath)   # path class will identify the operating system and converting the path accordingly ex: / or \

    # separate the folder and file
    if filedir !="":  # File is not empty then directory will creates
        os.makedirs(filedir,exist_ok=True)  # creating the folder if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # checking file is empty or not
        with open(filepath,"w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")   # check file is present or not




