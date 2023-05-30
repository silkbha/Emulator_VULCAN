import glob
import os
from pathlib import Path

def string_slicer(my_str,sub):
   index=my_str.find(sub)
   if index !=-1 :
         return my_str[index:] 
   else :
         raise Exception('Sub string not found!')

def main():
    # setup directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = str(Path(script_dir).parents[1])
    VULCAN_dir = os.path.join(parent_dir, 'VULCAN')
    output_dir = os.path.join(parent_dir, 'Emulator_VULCAN/data/vulcan_output')
    configs_dir = os.path.join(parent_dir, 'Emulator_VULCAN/data/configs')
    std_output_dir = os.path.join(output_dir, 'std_output')

    # load config files
    config_files = glob.glob(os.path.join(configs_dir, 'vulcan_cfg*.py'))
    print(f'Found {len(config_files)} config file(s).')

    # Checks for already run:
    # Create list of completed configs
    done_files = glob.glob(os.path.join(output_dir, 'output*.vul'))
    print(f'Found {len(done_files)} previously run config(s). Removing from queue...')
        
    # Remove completed configs from config_files list
    removed = 0
    for i,file in enumerate(done_files):
        file = string_slicer(file,"/output_")
        file = file.removeprefix("/output_")
        file = file.removesuffix(".vul")
        done_files[i] = file
    for file in config_files:
        filename = string_slicer(file,"/vulcan_cfg_")
        filename = filename.removeprefix("/vulcan_cfg_")
        filename = filename.removesuffix(".py")
        if filename in done_files:
            config_files.remove(file)
            removed +=1
    print(f'   Removed {removed} config(s) from queue.')

if __name__ == "__main__":
    main()