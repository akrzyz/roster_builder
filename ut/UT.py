#UTs
import traceback
import sys
sys.path.append('../')
import logging as LOG
import b_log

try:
    import b_classes_UT
    import b_xmlwriter_UT
    import b_xmlreader_UT  
    import b_engine_UT    
    import console_viewer_UT
except:
    traceback.print_exc()
    pass

if __name__ == '__main__' :    
    b_log.init_ut()
    LOG.info('~~!!!ALL TestModules Start!!!~~')    
    b_classes_UT.run_tests()
    b_xmlwriter_UT.run_tests()
    b_xmlreader_UT.run_tests()
    b_engine_UT.run_tests()
    console_viewer_UT.run_tests()
    LOG.info('~~!!!ALL TestModules Done!!!~~')
    print("~~!!! All Test Modules done !!!~~")
    input();
    sys.exit(0)