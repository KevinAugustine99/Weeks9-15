"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Kevin Augustine
"""

from dataclasses import dataclass
from typing import Union

@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str
    

@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    
    token = tokens.pop(0)
    if token.isdigit():
        return LiteralNode(token)
    elif token.isidentifier():
        return VariableNode(token)
    else:
        left = parse(tokens)
        right = parse(tokens)
        return MathNode(left,token,right)

            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node,VariableNode):
        return str(node.name)
    else:
        left = infix(node.left)
        right = infix(node.right)
        return "(" + left + " " + str(node.op)+ " " + right +")"
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    
    if isinstance(node, LiteralNode):
        return int(node.val)
    elif isinstance(node,VariableNode):
        return int(symTbl[node.name])
    else:
        left = evaluate(node.left,symTbl)
        right = evaluate(node.right,symTbl)
        if node.op == "+":
            return left + right
        elif node.op == "-":
            return left - right
        elif node.op == "*":
            return left * right
        elif node.op == "//":
            return left // right
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    print("Derping the symbol table (variable name => integer value)...")
    symTbl = dict()
    with open(inFile) as file1:
        for line in file1:
            tbl_line = line.split()
            symTbl[str(tbl_line[0])] = int(tbl_line[1]) 
            print(tbl_line[0] + " => " + tbl_line[1])

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens = prefixExp.split(" ")
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        tr = parse(tokens)
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_exp = infix(tr)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression: "+ infix_exp)
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        eval_result = evaluate(tr, symTbl)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation: " + str(eval_result))

    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
