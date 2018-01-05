# Import modules
import sys
import os
import PyCod.xanim as XAnim
import PyCod.xmodel as XModel

if len(sys.argv) <= 1:
    print("Error: No input file specified. example.py <xmodel.xmodel_export>")
else:
    fileImport = sys.argv[1]
    ext = os.path.splitext(fileImport)[-1].upper()
    fileExport = os.path.splitext(fileImport)[0]

    loadFn = None
    assetObj = None
    writeFn = None

    if ext == ".XMODEL_EXPORT":
        assetObj = XModel("example")
        loadFn = assetObj.LoadFile_Raw
        writeFn = assetObj.WriteFile_Bin
        fileExport = fileExport + ".XMODEL_BIN"
    elif ext == ".XMODEL_BIN":
        assetObj = XModel("example")
        loadFn = assetObj.LoadFile_Bin
        writeFn = assetObj.WriteFile_Raw
        fileExport = fileExport + ".XMODEL_EXPORT"
    elif ext == ".XANIM_EXPORT":
        assetObj = XAnim()
        loadFn = assetObj.LoadFile_Raw
        writeFn = assetObj.WriteFile_Bin
        fileExport = fileExport + ".XANIM_BIN"
    elif ext == ".XANIM_BIN":
        assetObj = XAnim()
        loadFn = assetObj.LoadFile_Bin
        writeFn = assetObj.WriteFile_Raw
        fileExport = fileExport + ".XANIM_EXPORT"

    loadFn(fileImport)
    writeFn(fileExport)

    print("The file has been saved: " + fileExport)