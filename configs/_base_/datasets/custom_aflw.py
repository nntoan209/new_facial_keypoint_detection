dataset_info = dict(
    dataset_name='custom_aflw',
    paper_info=dict(
        author='Koestinger, Martin and Wohlhart, Paul and '
        'Roth, Peter M and Bischof, Horst',
        title='Annotated facial landmarks in the wild: '
        'A large-scale, real-world database for facial '
        'landmark localization',
        container='2011 IEEE international conference on computer '
        'vision workshops (ICCV workshops)',
        year='2011',
        homepage='https://www.tugraz.at/institute/icg/research/'
        'team-bischof/lrs/downloads/aflw/',
    ),
    keypoint_info={
        0:
        dict(name='kpt-0', id=0, color=[255, 255, 255], type='', swap='kpt-1'),
        1:
        dict(name='kpt-1', id=1, color=[255, 255, 255], type='', swap='kpt-0'),
        2:
        dict(name='kpt-2', id=2, color=[255, 255, 255], type='', swap=''),
        3:
        dict(name='kpt-3', id=3, color=[255, 255, 255], type='', swap=''),
        4:
        dict(name='kpt-4', id=4, color=[255, 255, 255], type='', swap=''),
    },
    skeleton_info={},
    joint_weights=[1.] * 5,
    sigmas=[])
