import ruamel.yaml as yaml

def parse_yaml(path2yaml='parameters.yml'):
    """a utility function to generate variables from a .yml file in format
    :param path2yaml: an absolute or relative path to a .yml file
            this file should be in format <variable>: <value>
    :rtype: no return, but sets variables are global

     """
    yaml_file = open(path2yaml, 'r')
    yaml_content = yaml.load(yaml_file, Loader=yaml.Loader)

    print("Key: Value")
    for key, value in yaml_content.items():
        print(f"{key}: {value}")
        # globals()[key] = value
        exec('global {}'.format(key))
        exec('{} = {}'.format(key, value))

    global variab
    variab = 10
    variab = 11
