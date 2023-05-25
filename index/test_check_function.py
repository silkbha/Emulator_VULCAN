import glob
import os
from pathlib import Path

def slicer(my_str,sub):
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
    done_files = glob.glob(os.path.join(output_dir, '*.vul'))
    print(f'Found {len(done_files)} previously run config(s). Removing from queue...')
    
    print(done_files[0:3])
    
    # Remove completed configs from config_files list
    for i,file in enumerate(done_files):
        # TODO: remove abs path prefix!!!!
        print(file)
        file = slicer(file,"/output_")
        print(file)
        file = file.removeprefix("/output_")
        file = file.removesuffix(".vul")
        print(file)
        done_files[i] = file
    
    print(done_files[0:3])
    print(config_files[0:3])
    removed = 0

    for file in config_files:
        # TODO: remove abs path prefix!!!!
        filename = slicer(file,"/vulcan_cfg_")
        filename = filename.removeprefix("/vulcan_cfg_")
        filename = filename.removesuffix(".py")
        if filename in done_files:
            config_files.remove(file)
            removed +=1
    print(f'   Removed {removed} configs from queue.')

    print(config_files[0:3])

if __name__ == "__main__":
    main()