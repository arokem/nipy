
def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('group', parent_package, top_path)
    config.add_subpackage('tests')
    config.add_extension('onesample',
                         sources=['onesample.pyx'],
                         libraries=['cstat'])
    config.add_extension('twosample',
                         sources=['twosample.pyx'],
                         libraries=['cstat'])
    config.add_extension('glm_twolevel',
                         sources=['glm_twolevel.pyx'],
                         libraries=['cstat'])
    return config


if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
