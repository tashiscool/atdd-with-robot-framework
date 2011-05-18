ROOTDIR=`dirname $0`/..
BINPATH=$ROOTDIR/bin
SRCPATH=$ROOTDIR/src
TESTDATA=$ROOTDIR/atest/vacalc
TESTLIBS=$ROOTDIR/atest/libraries
CP=$BINPATH/robotframework-2.5.7.jar:$TESTLIBS/swinglibrary-1.1.2.jar:$BINPATH
CLASSPATH=$CP java org.robotframework.RobotFramework -P $SRCPATH -P $TESTLIBS $* --outputdir $ROOTDIR/results --critical regression $TESTDATA
