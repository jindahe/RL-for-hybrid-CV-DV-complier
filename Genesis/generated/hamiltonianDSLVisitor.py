# Generated from hamiltonianDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .hamiltonianDSLParser import hamiltonianDSLParser
else:
    from hamiltonianDSLParser import hamiltonianDSLParser

# This class defines a complete generic visitor for a parse tree produced by hamiltonianDSLParser.

class hamiltonianDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hamiltonianDSLParser#program.
    def visitProgram(self, ctx:hamiltonianDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#statementList.
    def visitStatementList(self, ctx:hamiltonianDSLParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#statement.
    def visitStatement(self, ctx:hamiltonianDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#constDeclaration.
    def visitConstDeclaration(self, ctx:hamiltonianDSLParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#rangeDeclaration.
    def visitRangeDeclaration(self, ctx:hamiltonianDSLParser.RangeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#expression.
    def visitExpression(self, ctx:hamiltonianDSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#addExpr.
    def visitAddExpr(self, ctx:hamiltonianDSLParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#mulExpr.
    def visitMulExpr(self, ctx:hamiltonianDSLParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#powerExpr.
    def visitPowerExpr(self, ctx:hamiltonianDSLParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#unaryExpr.
    def visitUnaryExpr(self, ctx:hamiltonianDSLParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:hamiltonianDSLParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#expressionList.
    def visitExpressionList(self, ctx:hamiltonianDSLParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#accumulationExpr.
    def visitAccumulationExpr(self, ctx:hamiltonianDSLParser.AccumulationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#rangeVars.
    def visitRangeVars(self, ctx:hamiltonianDSLParser.RangeVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#rangeVar.
    def visitRangeVar(self, ctx:hamiltonianDSLParser.RangeVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#quantumOp.
    def visitQuantumOp(self, ctx:hamiltonianDSLParser.QuantumOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hamiltonianDSLParser#bracketedIndices.
    def visitBracketedIndices(self, ctx:hamiltonianDSLParser.BracketedIndicesContext):
        return self.visitChildren(ctx)



del hamiltonianDSLParser