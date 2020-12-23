import transcrypt.__main__
import sys, os

sys.path.append (os.path.join(os.path.abspath(transcrypt.__main__.__file__), "modules"))

from org.transcrypt import utils
from org.transcrypt import compiler

try:
    compiler.Program (transpilationDirs, __symbols__, __envir__)
    return setExitCode (exitSuccess)
except utils.Error as error:
    utils.log (True, '\n{}\n', error)
    
    # Don't log anything else, even in verbose mode, since this would only be confusing
    if utils.commandArgs.dextex:
        utils.log (True, '{}\n', traceback.format_exc ())
        
    return setExitCode (exitSpecificCompileError)
except Exception as exception:
    utils.log (True, '\n{}', exception)
    
    # Have to log something else, because a general exception isn't informative enough
    utils.log (True, '{}\n', traceback.format_exc ())
    
    return setExitCode (exitGeneralCompileError)
