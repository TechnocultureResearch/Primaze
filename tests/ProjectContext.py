""" Easy fix: Adds the parent directory of this folder to system path """

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


""" Imports needed by tests """

from Core import Core