# -*- coding: utf-8 -*-

from FilesScanner import *
from SequenceGenerator import *
import os
import sys
import moviepy
import ntpath

class Videocringe():
    '''Main class of video cutter combine
       Defines how and how much video will be cringed'''

    def __init__(self, path='./'):
        self.exec_numb = 5
        self.path = path
        self.clips = []
        self.sequences = []
        self.date = time.strftime("%I%M%S")

    def cut_video(self, minLength=1, maxLength=1, times=1):
        Scanner = FilesScanner(self.path)
        self.clips = Scanner.scan_video()
        print(self.clips)
        Generator = SequenceGenerator(minLength, maxLength)
        for i in self.clips:
            for j in range(0,times):
                self.sequences.append(Generator.rand_sequence(i))
        print(self.sequences)

    '''helper function for getting filename (or dirname) from path'''
    def get_filename(self):
        head, tail = ntpath.split(self.path)
        return tail or ntpath.basename(head)

    def write_video(self):
        clipOut = concatenate_videoclips(self.sequences, method='compose')
        clipOut.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30)

if __name__ == '__main__':
    editor = Videocringe(sys.argv[1])
    editor.cut_video(1,3,4)
    editor.write_video()