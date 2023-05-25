import os.path 
import re 
from hiero.core import VersionScanner 

# Determine whether the file newVersionFile should be included as a new version of originalVersion 
# This filtering method only allows to add versions that have the same file pattern as the active one. 
def filterVersionSamePattern(self, binItem, newVersionFile): 
  activeVersion = binItem.activeItem() 
  if binItem.activeItem() and binItem.activeItem().mediaSource(): 
    # Obtain active item's filename 
    activeVersionFile = binItem.activeItem().mediaSource().firstpath() 

    # Substitute version index with * wildcard. 
    versionRegex = "v\\d+[a-zA-Z]*" 
    activeVersionFile = re.sub(versionRegex, "v*", activeVersionFile) 
    newVersionFile = re.sub(versionRegex, "v*", newVersionFile) 

    # Obtain pattern: 
    ext1 = re.split(r"_|\.", activeVersionFile)[-2] 
    ext2 = re.split(r"_|\.", newVersionFile)[-2] 
    return ext1 == ext2 
  return False 

VersionScanner.VersionScanner.filterVersion = filterVersionSamePattern