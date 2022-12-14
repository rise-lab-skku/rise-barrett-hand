#  puck_properties_consts.py
#
#  ~~~~~~~~~~~~
#
#  pyHand Constants File
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Authors : Chloe Eghtebas,
#            Brendan Ritter,
# 	     Pravina Samaratunga,
#            Jason Schwartz
#
#  Last change: 08.08.2013
#
#  Language: Python 2.7
#  ------------------------------------------------------------------
#
#  This version of pyHand is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as published
#  by the Free Software Foundation.
#

# PuckID
FINGER1 = 11
FINGER2 = 12
FINGER3 = 13
SPREAD = 14
ALL_FINGERS = (FINGER1, FINGER2, FINGER3, SPREAD)
GRASP = (FINGER1, FINGER2, FINGER3)
# Property = ID
ACCEL = 82
ADDR = 6
ANA0 = 18
ANA1 = 19
BAUD = 12
CMD = 29
CMD_LOAD = 0
CMD_SAVE = 1
CMD_RESET = 2
CMD_DEF = 3
CMD_GET = 4
CMD_FIND = 5
CMD_SET = 6
CMD_HOME = 7
CMD_KEEP = 8
CMD_LOOP = 9
CMD_PASS = 10
CMD_VERS = 11
CMD_ERR = 12
CMD_HI = 13
CMD_IC = 14
CMD_IO = 15
CMD_TC = 16
CMD_TO = 17
CMD_CLOSE = 18
CMD_MOVE = 19
CMD_OPEN = 20
CMD_TERM = 21
CMD_HELP = 22
CMD_PPSINIT = 23
CMD_TESTEE = 24
CT = 56
CT2 = 57
CTS = 68
CTS2 = 69
DEF = 32
DIG0 = 14
DIG1 = 15
DP = 50
DP2 = 51
DS = 60
E = 52
E2 = 53
ECMAX = 101
ECMIN = 102
EN = 94
EN2 = 95
ERROR = 4
FET0 = 16
FET1 = 17
FIND = 33
GRPA = 26
GRPB = 27
GRPC = 28
HALLH = 88
HALLH2 = 89
HALLS = 87
HOLD = 77
HSG = 71
ID = 3
IHIT = 108
IKCOR = 93
IKI = 92
IKP = 91
ILOGIC = 24
IMOTOR = 22
IOFF = 74
IOFF2 = 75
IOFST = 62
IPNM = 86
IVEL = 73
JIDX = 85
JOFST = 98
JOFST2 = 99
JP = 96
JP2 = 97
KD = 80
KI = 81
KP = 79
LCTC = 104
LCVC = 105
LFLAGS = 103
LOAD = 31
LOCK = 13
LSG = 72
M = 58
M2 = 59
MAX_ENCODER_TICKS = 195000.0
MAX_SPREAD_TICKS = 36000.0
MAX_FINGERTIP_TICKS = 78000.0
MCV = 46
MDS = 65
MECH = 66
MECH2 = 67
MODE = 8
MODE_IDLE = 0
MODE_TORQUE = 2
MODE_PID = 3
MODE_VEL = 4
MODE_TRAP = 5
MOFST = 61
MOV = 47
MPE = 76
MT = 43
MV = 45
OD = 64
OT = 54
OT2 = 55
OTEMP = 11
P = 48
P2 = 49
PIDX = 70
POLES = 90
PTEMP = 10
ROLE = 1
SAVE = 30
SG = 25
SN = 2
STAT = 5
T = 42
TACT = 106
TACT_FULL = 2
TACT_10 = 1
TACTID = 107
TACTID = 107
TEMP = 9
TENSO = 84
TENST = 83
THERM = 20
TIE = 100
TSTOP = 78
UPSECS = 63
V = 44
VALUE = 7
VBUS = 21
VERS = 0
VLOGIC = 23
X0 = 34
X1 = 35
X2 = 36
X3 = 37
X4 = 38
X5 = 39
X6 = 40
X7 = 41
FTS = 8
FTS_SG1 = 42
FTS_SG2 = 43
FTS_SG3 = 44
FTS_SG4 = 45
FTS_SG5 = 46
FTS_SG6 = 47
FTS_FX = 48
FTS_FY = 49
FTS_FZ = 50
FTS_TX = 51
FTS_TY = 52
FTS_TZ = 53
FTS_FT = 54
FTS_AX = 55
FTS_AY = 56
FTS_AZ = 57
FTS_GM = 58
FTS_OV = 59
FTS_LED = 60
FTS_T1 = 61
FTS_T2 = 62
FTS_T3 = 63
FTS_A = 64
NO_WRITE_PROPERTIES = [
    ANA0,
    ANA1,
    CT2,
    DP2,
    E2,
    EN2,
    ERROR,
    HALLH2,
    ILOGIC,
    IMOTOR,
    IOFF2,
    JOFST2,
    JP2,
    M2,
    MECH,
    MECH2,
    OT2,
    P2,
    SG,
    TEMP,
    THERM,
    VBUS,
    VLOGIC,
]
NO_READ_PROPERTIES = [
    CMD,
    CT2,
    DEF,
    DP2,
    E2,
    EN2,
    FIND,
    HALLH2,
    IOFF2,
    JOFST2,
    JP2,
    LOAD,
    LOCK,
    M,
    M2,
    MECH2,
    OT2,
    P2,
    SAVE,
]
LOCKED_PROPERTIES = [DIG0, DIG1, FET0, FET1, HALLH, HALLS, OD, PTEMP, ROLE, SN]
