import ConfigParser
import subprocess
import os 

working_dir_ext = ('scenario','jig')
exec_start_ext = ('test','logger','interface','trigger')

def get_cwd():
    cwd = subprocess.check_output(["pwd"])
    print("Current working dir : " + cwd)
    return cwd


def read_config():

    config = ConfigParser.ConfigParser()
    config.readfp(open(r'default.cfg'))
    Type = config.get('Default', 'WorkingDirectory')
    print(Type)

def write_cwd (filename):
    cwd = get_cwd().rstrip('\n\r')
    new_working_dir = os.path.join(cwd,"bin/")
    print("changing new working dir to :" + new_working_dir)
    config = ConfigParser.ConfigParser()
    config.optionxform = str
    config.read(filename)
    Type = config.set('Scenario', 'WorkingDirectory',new_working_dir)
    with open(filename,"wb") as configfile:
        config.write(configfile)

def write_cwd (filename):
    cwd = get_cwd().rstrip('\n\r')
    new_working_dir = os.path.join(cwd,"bin/")
    print("changing new working dir to :" + new_working_dir)
    config = ConfigParser.ConfigParser()
    config.optionxform = str
    config.read(filename)
    Type = config.set('Scenario', 'WorkingDirectory',new_working_dir)
    with open(filename,"wb") as configfile:
        config.write(configfile)


def iterate_dir():
    cwd = get_cwd().rstrip('\n\r')
    new_working_dir = os.path.join(cwd,"bin/")
    print("changing new working dir to :" + new_working_dir)

    for filename in os.listdir("."):  
        file_name , file_extension = os.path.splitext(filename)
        file_extension = file_extension.strip('.')

        config = ConfigParser.ConfigParser()
        config.optionxform = str
        if filename.endswith(working_dir_ext):
            config.read(filename)
            for section in config.sections():
                    print(section)
                    for(key, val) in config.items(section):
                        if key == 'WorkingDirectory':
                            config_path = val;
                            basename = os.path.basename(config_path)
                            config.set(section, 'WorkingDirectory',os.path.join(new_working_dir,basename))
                        elif key == 'DefaultWorkingDirectory':
                            config_path = val;
                            basename = os.path.basename(config_path)
                            config.set(section, 'DefaultWorkingDirectory',os.path.join(new_working_dir,basename))


            with open(filename,"wb") as configfile:
                config.write(configfile)
        elif filename.endswith(exec_start_ext):
            config.read(filename)
            for section in config.sections():
                     print(section)
                     for(key, val) in config.items(section):
                        if key == 'ExecStart':
                            config_path = val;
                            basename = os.path.basename(config_path)
                            config.set(section, 'ExecStart',os.path.join(new_working_dir,basename))
           
            with open(filename,"wb") as configfile:
                config.write(configfile)

def random_func():
        if filename.endswith(working_dir_ext):
            config_path = config.get(file_extension, 'WorkingDirectory')
            basename = os.path.basename(config_path)
            config.set(file_extension, 'WorkingDirectory',os.path.join(new_working_dir,basename))

        elif filename.endswith(exec_start_ext):
            config_path = config.get(file_extension, 'ExecStart')
            basename = os.path.basename(config_path)
            Type = config.set(file_extension, 'ExecStart',new_working_dir)


iterate_dir()
#write_cwd("full_sequence.scenario")



