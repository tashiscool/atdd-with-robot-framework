RF=bin/robotframework-2.6.3.jar
MAIN=org.robotframework.vacalc.VacalcRunner
java -cp $RF:bin/ -Dpython.path=src $MAIN
