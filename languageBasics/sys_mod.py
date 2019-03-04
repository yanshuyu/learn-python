if __name__ == '__main__':
    import sys
    print('----------------------python-----------------')
    print('platfrom: {}'.format(sys.platform))
    print('version: {}'.format(sys.version))
    print('search path: {}'.format(sys.path))
    #print('loaded modules: {}'.format(sys.modules))
    print('buildin modules: {}'.format(sys.builtin_module_names))
    print('---------------------------------------------')
    print(help(sys))