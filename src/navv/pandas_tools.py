#!/usr/bin/env python3

# Copyright 2023 Battelle Energy Alliance, LLC

# python std library imports
import argparse
import os
import pkg_resources
import pickle
import pandas as pd
import sys

# package imports
from navv import utilities
from navv import spreadsheet_tools
from navv import _version

DATA_PATH = pkg_resources.resource_filename("navv", "data/")


class Pandas_Tools:
    def __init__(self, columnNames):
        self.columns = columnNames

    def getEmptyDataFrameList(self):
        return pd.DataFrame(self.columns)
    

    
        