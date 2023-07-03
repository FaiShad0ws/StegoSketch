#!/usr/bin/env python3

import sys
import getopt
from embedingData import Visible_Watermark, Invisible_Watermark

usage = ''' 
    usage: ./StegoSketch.py -i  <path-to-image>  -d  <data-to-embed> 
           ./StegoSketch.py -v  <path-to-image>  -d  <data-to-embed>
    

    Common options:
      -i, --invisible          generate an Invisible Watermark aka (Steganography)
      -v, --visible            generate a visible Watermark for copyrights
      -d, --data               specify the data to be embedded in image

    Informative options:
      -h, --help               print this help menu and exit
                              
      '''


def main(invisible = None ,visible = None, verbose = False):

      path = ""
      invisible = False
      visible = False

      # option menu
      try:
          opts, args = getopt.getopt(sys.argv[1:], 'hi:v:d:', ['help','invisible', 'visible', 'data'])

      except getopt.GetoptError as e:
          print(usage)
          print(str(e) + '\n')
          sys.exit(1)

      for opt, arg in opts: 

          if opt in ('-h', '--help'):
              print(usage)
              sys.exit(0)

          elif opt in ('-i', '--invisible'):
              path = arg
              invisible = True

          elif opt in ('-v', '--visible'):
              path = arg
              visible = True
        
          elif opt in ('-d', '--data'):
              data = arg

              if (visible):
                Visible_Watermark(path,data)

              if (invisible):
                Invisible_Watermark(path,data)

              
              

              


if __name__=="__main__":
    main()