import os

frame_folder = './images/stable/1/'
framenames = [f for f in os.listdir(frame_folder) if not f.startswith('.')]
prev_framepath = frame_folder + framenames[0]
first_frame = 1
for framename in framenames:

    if 'ppm' in framename and first_frame != 1:
        framepath = frame_folder + framename
        ofpath = frame_folder + 'of/' + prev_framepath + '_' + framepath + '.flo'
        os.system('python script_pwc.py \'%s\' \'%s\' \'%s\'' % (prev_framepath, framepath, ofpath))
    else:
        first_frame = 0
        continue
