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
    def __init__(self, d=list(), cols=list()):
        self.data = d
        self.columns = cols
        self.df = pd.DataFrame(data=d, column=cols)

    def getEmptyDataFrameList(self):
        return self.df
    
    def appendSheetToExistingExcel(self, filePath, sheetName):
        with pd.ExcelWriter(
        filePath,
        mode="a",
        engine="openpyxl",
        if_sheet_exists="replace",
        ) as writer:
            self.df.to_excel(writer, sheet_name=sheetName)  
    

    
        