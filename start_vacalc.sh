RF=bin/robotframework-2.5.7.jar
MAIN=org.robotframework.vacalc.VacalcRunner
java -cp $RF:bin/ -Dpython.path=src $MAIN
