# Generated from hamiltonianDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .hamiltonianDSLParser import hamiltonianDSLParser
else:
    from hamiltonianDSLParser import hamiltonianDSLParser

# This class defines a complete listener for a parse tree produced by hamiltonianDSLParser.
class hamiltonianDSLListener(ParseTreeListener):

    # Enter a parse tree produced by hamiltonianDSLParser#program.
    def enterProgram(self, ctx:hamiltonianDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#program.
    def exitProgram(self, ctx:hamiltonianDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#statementList.
    def enterStatementList(self, ctx:hamiltonianDSLParser.StatementListContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#statementList.
    def exitStatementList(self, ctx:hamiltonianDSLParser.StatementListContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#statement.
    def enterStatement(self, ctx:hamiltonianDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#statement.
    def exitStatement(self, ctx:hamiltonianDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#constDeclaration.
    def enterConstDeclaration(self, ctx:hamiltonianDSLParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#constDeclaration.
    def exitConstDeclaration(self, ctx:hamiltonianDSLParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#rangeDeclaration.
    def enterRangeDeclaration(self, ctx:hamiltonianDSLParser.RangeDeclarationContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#rangeDeclaration.
    def exitRangeDeclaration(self, ctx:hamiltonianDSLParser.RangeDeclarationContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#expression.
    def enterExpression(self, ctx:hamiltonianDSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#expression.
    def exitExpression(self, ctx:hamiltonianDSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#addExpr.
    def enterAddExpr(self, ctx:hamiltonianDSLParser.AddExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#addExpr.
    def exitAddExpr(self, ctx:hamiltonianDSLParser.AddExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#mulExpr.
    def enterMulExpr(self, ctx:hamiltonianDSLParser.MulExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#mulExpr.
    def exitMulExpr(self, ctx:hamiltonianDSLParser.MulExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#powerExpr.
    def enterPowerExpr(self, ctx:hamiltonianDSLParser.PowerExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#powerExpr.
    def exitPowerExpr(self, ctx:hamiltonianDSLParser.PowerExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#unaryExpr.
    def enterUnaryExpr(self, ctx:hamiltonianDSLParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#unaryExpr.
    def exitUnaryExpr(self, ctx:hamiltonianDSLParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:hamiltonianDSLParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:hamiltonianDSLParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#expressionList.
    def enterExpressionList(self, ctx:hamiltonianDSLParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#expressionList.
    def exitExpressionList(self, ctx:hamiltonianDSLParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#accumulationExpr.
    def enterAccumulationExpr(self, ctx:hamiltonianDSLParser.AccumulationExprContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#accumulationExpr.
    def exitAccumulationExpr(self, ctx:hamiltonianDSLParser.AccumulationExprContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#rangeVars.
    def enterRangeVars(self, ctx:hamiltonianDSLParser.RangeVarsContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#rangeVars.
    def exitRangeVars(self, ctx:hamiltonianDSLParser.RangeVarsContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#rangeVar.
    def enterRangeVar(self, ctx:hamiltonianDSLParser.RangeVarContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#rangeVar.
    def exitRangeVar(self, ctx:hamiltonianDSLParser.RangeVarContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#quantumOp.
    def enterQuantumOp(self, ctx:hamiltonianDSLParser.QuantumOpContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#quantumOp.
    def exitQuantumOp(self, ctx:hamiltonianDSLParser.QuantumOpContext):
        pass


    # Enter a parse tree produced by hamiltonianDSLParser#bracketedIndices.
    def enterBracketedIndices(self, ctx:hamiltonianDSLParser.BracketedIndicesContext):
        pass

    # Exit a parse tree produced by hamiltonianDSLParser#bracketedIndices.
    def exitBracketedIndices(self, ctx:hamiltonianDSLParser.BracketedIndicesContext):
        pass



del hamiltonianDSLParser