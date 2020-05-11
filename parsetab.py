
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expleftEQEQleftLESSERLEEQGREATERGEEQleftADDSUBPOWERleftMULTIPLYDIVIDErightNOEQADD AND BOOL CHAR COLON COMMA DIVIDE DOUBLE EQEQ EQUAL FALSE FOR GEEQ GREATER INT LCURL LEEQ LESSER LPAREN MINUSMINUS MOD MULTIPLY NOEQ NOT OR PLUSPLUS POWER PRINT RCURL RPAREN SEMICOLON STRING STRUCT SUB TO TRUE TYPE VARNAMEstmnts : stmnt stmntsexp : exp COMMA expstmnts : exp : FALSE \n        | TRUE exp : stmntsstmnt : VARNAME PLUSPLUS SEMICOLON\n    | VARNAME PLUSPLUS stmnt : VARNAME MINUSMINUS SEMICOLON\n    | VARNAME MINUSMINUSstmnt : TYPE VARNAME vnames EQUAL exp\n        | TYPE VARNAME vnames EQUAL exp SEMICOLON stmnt : TYPE VARNAME vnames SEMICOLONstmnt : VARNAME EQUAL exp SEMICOLONstmnt : FOR LPAREN exp COLON exp COLON exp RPAREN LCURL stmnts RCURLstmnt : PRINT LPAREN exp RPAREN SEMICOLONexp : LPAREN exp RPARENchoice : PLUSPLUS\n\t\t| MINUSMINUSattrs : TYPE VARNAME attrs2attrs2 : COMMA attrs\n\t\t| exp : vnames : COMMA VARNAME vnamesvnames : exp : INTexp : CHARexp : STRINGexp : DOUBLEexp : BOOLexp : VARNAME exp : exp ADD exp \n\t\t| exp SUB exp \n\t\t| exp MULTIPLY exp \n\t\t| exp POWER exp \n\t\t| exp DIVIDE exp \n\t\t| exp MOD expexp : exp EQEQ exp \n\t\t| exp LEEQ exp \n\t\t| exp GEEQ exp \n\t\t| exp GREATER exp \n\t\t| exp LESSER exp\n\t\t| exp NOEQ expexp : exp OR exp \n\t\t| exp AND exp \n\t\t| exp NOT expexp : exp PLUSPLUS  \n\t\t| exp MINUSMINUSstmnt : STRUCT VARNAME LCURL stmnts RCURL SEMICOLONstmnt : VARNAME VARNAME SEMICOLON'
    
_lr_action_items = {'FALSE':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'TRUE':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'LPAREN':([0,5,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[5,5,43,44,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'COMMA':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,75,76,79,81,82,84,85,86,87,91,],[-3,17,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,17,-8,-10,-3,-1,68,-3,-3,17,-32,-33,-34,-35,-36,17,-38,-39,-40,-41,-42,-43,17,17,17,-17,-50,-7,-9,17,17,17,-14,-3,-13,68,-3,17,17,-16,-12,-3,-49,17,-15,]),'ADD':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,18,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,18,-8,-10,-3,-1,-3,-3,18,-32,-33,-34,-35,-36,18,18,18,18,18,18,-43,18,18,18,-17,-50,-7,-9,18,18,18,-14,-3,-13,-3,18,18,-16,-12,-3,-49,18,-15,]),'SUB':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,19,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,19,-8,-10,-3,-1,-3,-3,19,-32,-33,-34,-35,-36,19,19,19,19,19,19,-43,19,19,19,-17,-50,-7,-9,19,19,19,-14,-3,-13,-3,19,19,-16,-12,-3,-49,19,-15,]),'MULTIPLY':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,20,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,20,-8,-10,-3,-1,-3,-3,20,20,20,-34,20,-36,20,20,20,20,20,20,-43,20,20,20,-17,-50,-7,-9,20,20,20,-14,-3,-13,-3,20,20,-16,-12,-3,-49,20,-15,]),'POWER':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,21,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,21,-8,-10,-3,-1,-3,-3,21,-32,-33,-34,-35,-36,21,21,21,21,21,21,-43,21,21,21,-17,-50,-7,-9,21,21,21,-14,-3,-13,-3,21,21,-16,-12,-3,-49,21,-15,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,22,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,22,-8,-10,-3,-1,-3,-3,22,22,22,-34,22,-36,22,22,22,22,22,22,-43,22,22,22,-17,-50,-7,-9,22,22,22,-14,-3,-13,-3,22,22,-16,-12,-3,-49,22,-15,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,23,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,23,-8,-10,-3,-1,-3,-3,23,-32,-33,-34,-35,-36,23,-38,-39,-40,-41,-42,-43,23,23,23,-17,-50,-7,-9,23,23,23,-14,-3,-13,-3,23,23,-16,-12,-3,-49,23,-15,]),'EQEQ':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,24,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,24,-8,-10,-3,-1,-3,-3,24,-32,-33,-34,-35,-36,24,-38,-39,-40,-41,-42,-43,24,24,24,-17,-50,-7,-9,24,24,24,-14,-3,-13,-3,24,24,-16,-12,-3,-49,24,-15,]),'LEEQ':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,25,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,25,-8,-10,-3,-1,-3,-3,25,-32,-33,-34,-35,-36,25,25,-39,-40,-41,-42,-43,25,25,25,-17,-50,-7,-9,25,25,25,-14,-3,-13,-3,25,25,-16,-12,-3,-49,25,-15,]),'GEEQ':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,26,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,26,-8,-10,-3,-1,-3,-3,26,-32,-33,-34,-35,-36,26,26,-39,-40,-41,-42,-43,26,26,26,-17,-50,-7,-9,26,26,26,-14,-3,-13,-3,26,26,-16,-12,-3,-49,26,-15,]),'GREATER':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,27,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,27,-8,-10,-3,-1,-3,-3,27,-32,-33,-34,-35,-36,27,27,-39,-40,-41,-42,-43,27,27,27,-17,-50,-7,-9,27,27,27,-14,-3,-13,-3,27,27,-16,-12,-3,-49,27,-15,]),'LESSER':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,28,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,28,-8,-10,-3,-1,-3,-3,28,-32,-33,-34,-35,-36,28,28,-39,-40,-41,-42,-43,28,28,28,-17,-50,-7,-9,28,28,28,-14,-3,-13,-3,28,28,-16,-12,-3,-49,28,-15,]),'NOEQ':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,29,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,29,-8,-10,-3,-1,-3,-3,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-17,-50,-7,-9,29,29,29,-14,-3,-13,-3,29,29,-16,-12,-3,-49,29,-15,]),'OR':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,30,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,30,-8,-10,-3,-1,-3,-3,30,-32,-33,-34,-35,-36,30,-38,-39,-40,-41,-42,-43,30,30,30,-17,-50,-7,-9,30,30,30,-14,-3,-13,-3,30,30,-16,-12,-3,-49,30,-15,]),'AND':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,31,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,31,-8,-10,-3,-1,-3,-3,31,-32,-33,-34,-35,-36,31,-38,-39,-40,-41,-42,-43,31,31,31,-17,-50,-7,-9,31,31,31,-14,-3,-13,-3,31,31,-16,-12,-3,-49,31,-15,]),'NOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,32,-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,32,-8,-10,-3,-1,-3,-3,32,-32,-33,-34,-35,-36,32,-38,-39,-40,-41,-42,-43,32,32,32,-17,-50,-7,-9,32,32,32,-14,-3,-13,-3,32,32,-16,-12,-3,-49,32,-15,]),'PLUSPLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,33,-4,-5,-6,-3,-26,-27,-28,-29,-30,37,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,33,-8,-10,-3,-1,37,-3,-3,33,-32,-33,-34,-35,-36,33,-38,-39,-40,-41,-42,-43,33,33,33,-17,-50,-7,-9,33,33,33,-14,-3,-13,-3,33,33,-16,-12,-3,-49,33,-15,]),'MINUSMINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,76,79,81,82,84,85,86,87,91,],[-3,34,-4,-5,-6,-3,-26,-27,-28,-29,-30,38,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,34,-8,-10,-3,-1,38,-3,-3,34,-32,-33,-34,-35,-36,34,-38,-39,-40,-41,-42,-43,34,34,34,-17,-50,-7,-9,34,34,34,-14,-3,-13,-3,34,34,-16,-12,-3,-49,34,-15,]),'$end':([0,1,2,3,4,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,72,73,74,79,82,84,86,91,],[-3,0,-4,-5,-6,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,-8,-10,-1,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,-14,-3,-13,-11,-16,-12,-49,-15,]),'INT':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'CHAR':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'STRING':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'DOUBLE':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'BOOL':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'VARNAME':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,41,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,71,72,73,74,76,79,82,84,85,86,89,91,],[11,-4,-5,-6,11,-26,-27,-28,-29,-30,36,41,42,45,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-47,-48,-8,-10,11,-1,36,11,11,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,75,41,-14,11,-13,11,-11,-16,-12,11,-49,41,-15,]),'TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,76,79,82,84,85,86,89,91,],[13,-4,-5,-6,13,-26,-27,-28,-29,-30,-31,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-47,-48,-8,-10,13,-1,13,13,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,13,-14,13,-13,13,-11,-16,-12,13,-49,13,-15,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,76,79,82,84,85,86,89,91,],[14,-4,-5,-6,14,-26,-27,-28,-29,-30,-31,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-47,-48,-8,-10,14,-1,14,14,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,14,-14,14,-13,14,-11,-16,-12,14,-49,14,-15,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,76,79,82,84,85,86,89,91,],[15,-4,-5,-6,15,-26,-27,-28,-29,-30,-31,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-47,-48,-8,-10,15,-1,15,15,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,15,-14,15,-13,15,-11,-16,-12,15,-49,15,-15,]),'STRUCT':([0,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,39,40,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,76,79,82,84,85,86,89,91,],[16,-4,-5,-6,16,-26,-27,-28,-29,-30,-31,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-47,-48,-8,-10,16,-1,16,16,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,16,-14,16,-13,16,-11,-16,-12,16,-49,16,-15,]),'RPAREN':([2,3,4,5,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,73,74,79,82,84,85,86,87,91,],[-4,-5,-6,-3,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,62,-8,-10,-1,-3,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,77,-14,-3,-13,-11,-16,-12,-3,-49,88,-15,]),'SEMICOLON':([2,3,4,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,42,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,73,74,75,77,79,80,82,83,84,86,91,],[-4,-5,-6,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,63,64,65,-3,-1,-25,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,72,74,-14,-3,-13,-25,82,84,-24,-16,86,-12,-49,-15,]),'COLON':([2,3,4,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,40,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,69,72,73,74,76,79,81,82,84,86,91,],[-4,-5,-6,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,-8,-10,-1,-3,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,76,-14,-3,-13,-3,-11,85,-16,-12,-49,-15,]),'RCURL':([2,3,4,6,7,8,9,10,11,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,37,38,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,74,78,79,82,84,86,89,90,91,],[-4,-5,-6,-26,-27,-28,-29,-30,-31,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-47,-48,-8,-10,-1,-2,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-17,-50,-7,-9,-3,-14,-3,-13,83,-11,-16,-12,-49,-3,91,-15,]),'EQUAL':([11,41,42,67,75,80,],[39,39,-25,73,-25,-24,]),'LCURL':([45,88,],[71,89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,5,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,73,76,85,],[1,35,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,69,70,79,81,87,]),'stmnts':([0,5,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,71,73,76,85,89,],[4,4,40,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,78,4,4,4,90,]),'stmnt':([0,5,12,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,39,43,44,71,73,76,85,89,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'vnames':([42,75,],[67,80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('stmnts -> stmnt stmnts','stmnts',2,'p_exp_stmnts','parser.py',25),
  ('exp -> exp COMMA exp','exp',3,'p_exp_print','parser.py',29),
  ('stmnts -> <empty>','stmnts',0,'p_exp_stempty','parser.py',33),
  ('exp -> FALSE','exp',1,'p_exp_bool','parser.py',37),
  ('exp -> TRUE','exp',1,'p_exp_bool','parser.py',38),
  ('exp -> stmnts','exp',1,'p_stmnt_start','parser.py',46),
  ('stmnt -> VARNAME PLUSPLUS SEMICOLON','stmnt',3,'p_stmnt_inn','parser.py',50),
  ('stmnt -> VARNAME PLUSPLUS','stmnt',2,'p_stmnt_inn','parser.py',51),
  ('stmnt -> VARNAME MINUSMINUS SEMICOLON','stmnt',3,'p_stmnt_dnn','parser.py',55),
  ('stmnt -> VARNAME MINUSMINUS','stmnt',2,'p_stmnt_dnn','parser.py',56),
  ('stmnt -> TYPE VARNAME vnames EQUAL exp','stmnt',5,'p_stmnt_declaration','parser.py',62),
  ('stmnt -> TYPE VARNAME vnames EQUAL exp SEMICOLON','stmnt',6,'p_stmnt_declaration','parser.py',63),
  ('stmnt -> TYPE VARNAME vnames SEMICOLON','stmnt',4,'p_stmnt_valueless','parser.py',67),
  ('stmnt -> VARNAME EQUAL exp SEMICOLON','stmnt',4,'p_stmnt_assignment','parser.py',71),
  ('stmnt -> FOR LPAREN exp COLON exp COLON exp RPAREN LCURL stmnts RCURL','stmnt',11,'p_stmnt_for','parser.py',76),
  ('stmnt -> PRINT LPAREN exp RPAREN SEMICOLON','stmnt',5,'p_stmnt_print','parser.py',81),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_closed_exp','parser.py',85),
  ('choice -> PLUSPLUS','choice',1,'p_ch_ch','parser.py',89),
  ('choice -> MINUSMINUS','choice',1,'p_ch_ch','parser.py',90),
  ('attrs -> TYPE VARNAME attrs2','attrs',3,'p_attr_attr','parser.py',94),
  ('attrs2 -> COMMA attrs','attrs2',2,'p_attr_attrs2','parser.py',98),
  ('attrs2 -> <empty>','attrs2',0,'p_attr_attrs2','parser.py',99),
  ('exp -> <empty>','exp',0,'p_exp_emp','parser.py',106),
  ('vnames -> COMMA VARNAME vnames','vnames',3,'p_vnames_emo','parser.py',110),
  ('vnames -> <empty>','vnames',0,'p_vnames_empty','parser.py',114),
  ('exp -> INT','exp',1,'p_value_int','parser.py',118),
  ('exp -> CHAR','exp',1,'p_value_char','parser.py',121),
  ('exp -> STRING','exp',1,'p_value_string','parser.py',124),
  ('exp -> DOUBLE','exp',1,'p_value_double','parser.py',127),
  ('exp -> BOOL','exp',1,'p_value_bool','parser.py',130),
  ('exp -> VARNAME','exp',1,'p_value_vname','parser.py',134),
  ('exp -> exp ADD exp','exp',3,'p_exp_binaryop','parser.py',139),
  ('exp -> exp SUB exp','exp',3,'p_exp_binaryop','parser.py',140),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_binaryop','parser.py',141),
  ('exp -> exp POWER exp','exp',3,'p_exp_binaryop','parser.py',142),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_binaryop','parser.py',143),
  ('exp -> exp MOD exp','exp',3,'p_exp_binaryop','parser.py',144),
  ('exp -> exp EQEQ exp','exp',3,'p_exp_compareop','parser.py',148),
  ('exp -> exp LEEQ exp','exp',3,'p_exp_compareop','parser.py',149),
  ('exp -> exp GEEQ exp','exp',3,'p_exp_compareop','parser.py',150),
  ('exp -> exp GREATER exp','exp',3,'p_exp_compareop','parser.py',151),
  ('exp -> exp LESSER exp','exp',3,'p_exp_compareop','parser.py',152),
  ('exp -> exp NOEQ exp','exp',3,'p_exp_compareop','parser.py',153),
  ('exp -> exp OR exp','exp',3,'p_exp_logop','parser.py',157),
  ('exp -> exp AND exp','exp',3,'p_exp_logop','parser.py',158),
  ('exp -> exp NOT exp','exp',3,'p_exp_logop','parser.py',159),
  ('exp -> exp PLUSPLUS','exp',2,'p_exp_crement','parser.py',163),
  ('exp -> exp MINUSMINUS','exp',2,'p_exp_crement','parser.py',164),
  ('stmnt -> STRUCT VARNAME LCURL stmnts RCURL SEMICOLON','stmnt',6,'p_stmnt_struct_declaration','parser.py',168),
  ('stmnt -> VARNAME VARNAME SEMICOLON','stmnt',3,'p_struct_instance','parser.py',172),
]
