from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from calc_evaluator import CalcEvaluator

def main():
    expression = input("Enter an expression: ")
    input_stream = InputStream(expression)
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)
    tree = parser.expr()

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    print("Result:", calc_evaluator.getValue())

if __name__ == "__main__":
    main()


# from antlr4 import *
# from CalcLexer import CalcLexer
# from CalcParser import CalcParser
# from calc_evaluator import CalcEvaluator

# def main():
#     expression = input("Enter an expression: ")
#     input_stream = InputStream(expression)
#     lexer = CalcLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = CalcParser(token_stream)
#     tree = parser.expr()

#     calc_evaluator = CalcEvaluator()
#     walker = ParseTreeWalker()
#     walker.walk(calc_evaluator, tree)

#     print("Syntax Tree:", tree.toStringTree(recog=parser))
#     print("Result:", calc_evaluator.getValue())

# if __name__ == "__main__":
#     main()
