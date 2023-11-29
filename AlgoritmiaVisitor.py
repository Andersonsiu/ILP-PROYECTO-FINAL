# Generated from Algoritmia.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser

# This class defines a complete generic visitor for a parse tree produced by AlgoritmiaParser.

class AlgoritmiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmiaParser#root.
    def visitRoot(self, ctx:AlgoritmiaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#inss.
    def visitInss(self, ctx:AlgoritmiaParser.InssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#ins.
    def visitIns(self, ctx:AlgoritmiaParser.InsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#read.
    def visitRead(self, ctx:AlgoritmiaParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#write.
    def visitWrite(self, ctx:AlgoritmiaParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#condition.
    def visitCondition(self, ctx:AlgoritmiaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#while_.
    def visitWhile_(self, ctx:AlgoritmiaParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#siz.
    def visitSiz(self, ctx:AlgoritmiaParser.SizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#procDef.
    def visitProcDef(self, ctx:AlgoritmiaParser.ProcDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#proc.
    def visitProc(self, ctx:AlgoritmiaParser.ProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#assign.
    def visitAssign(self, ctx:AlgoritmiaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#looksheet.
    def visitLooksheet(self, ctx:AlgoritmiaParser.LooksheetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#paramsId.
    def visitParamsId(self, ctx:AlgoritmiaParser.ParamsIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#paramsExpr.
    def visitParamsExpr(self, ctx:AlgoritmiaParser.ParamsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#reprod.
    def visitReprod(self, ctx:AlgoritmiaParser.ReprodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#listrem.
    def visitListrem(self, ctx:AlgoritmiaParser.ListremContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#listadd.
    def visitListadd(self, ctx:AlgoritmiaParser.ListaddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#consult.
    def visitConsult(self, ctx:AlgoritmiaParser.ConsultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#lista.
    def visitLista(self, ctx:AlgoritmiaParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#List_.
    def visitList_(self, ctx:AlgoritmiaParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Mod.
    def visitMod(self, ctx:AlgoritmiaParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Var.
    def visitVar(self, ctx:AlgoritmiaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Parens.
    def visitParens(self, ctx:AlgoritmiaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Num.
    def visitNum(self, ctx:AlgoritmiaParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Lt.
    def visitLt(self, ctx:AlgoritmiaParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#String.
    def visitString(self, ctx:AlgoritmiaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Nota.
    def visitNota(self, ctx:AlgoritmiaParser.NotaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Tamanio.
    def visitTamanio(self, ctx:AlgoritmiaParser.TamanioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Eq.
    def visitEq(self, ctx:AlgoritmiaParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Gt.
    def visitGt(self, ctx:AlgoritmiaParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Div.
    def visitDiv(self, ctx:AlgoritmiaParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Consult_.
    def visitConsult_(self, ctx:AlgoritmiaParser.Consult_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Suma.
    def visitSuma(self, ctx:AlgoritmiaParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Min.
    def visitMin(self, ctx:AlgoritmiaParser.MinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Mult.
    def visitMult(self, ctx:AlgoritmiaParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Gte.
    def visitGte(self, ctx:AlgoritmiaParser.GteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Neq.
    def visitNeq(self, ctx:AlgoritmiaParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Lte.
    def visitLte(self, ctx:AlgoritmiaParser.LteContext):
        return self.visitChildren(ctx)



del AlgoritmiaParser