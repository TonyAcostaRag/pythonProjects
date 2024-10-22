from tests import TestExecutor


def parse_bool_expr(expression: str) -> bool:

    def inner_expression_evaluator(expr: str):
        print('\nInput expr:', expr)
        boolean_operands = []
        boolean_operator = ''
        inner_evaluation = ''
        index_inner_operator = 0
        for i in range(len(expr)):
            if expr[i] == ')':
                break
            if expr[i] == '&' or expr[i] == '|' and boolean_operator != '':
                boolean_operands.clear()
                boolean_operator = ''
            if expr[i] == 'f' or expr[i] == 't':
                boolean_operands.append(expr[i])
                if boolean_operator == '':
                    boolean_operator = expr[i - 2: i - 1]
                    index_inner_operator = i - 2

        if boolean_operator == '&':
            if 'f' in boolean_operands:
                inner_evaluation = 'f'
            else:
                inner_evaluation = 't'

        elif boolean_operator == '!':
            if boolean_operands[0] == 'f':
                inner_evaluation = 't'
            else:
                inner_evaluation = 'f'

        elif boolean_operator == '|':
            if 't' in boolean_operands:
                inner_evaluation = 't'
            else:
                inner_evaluation = 'f'

        print(
            '\nboolean_operands:', boolean_operands,
            '\nboolean_operator:', boolean_operator,
            '\nindex_inner_operator:', index_inner_operator,
            '\nFirst part:', expr[:index_inner_operator],
            '\nSecond part:', inner_evaluation,
            '\nThird part:', expr.replace(',', '')[index_inner_operator + 3 + len(boolean_operands):],
            '\nWhole string:', expr[:index_inner_operator] + inner_evaluation + expr.replace(',', '')[index_inner_operator + 3 + len(boolean_operands):]
        )

        expr = expr[:index_inner_operator] + inner_evaluation + expr.replace(',', '')[index_inner_operator + 3 + len(boolean_operands):]
        return [
            True if index_inner_operator == 0 else False,
            expr
        ]

    expression = inner_expression_evaluator(expression)
    if expression[0]:
        return True if expression[1] == 't' else False

    return parse_bool_expr(expression[1])


if __name__ == '__main__':
    TestExecutor.execute_function([
        #["&(|(f))"],
        #["|(f,f,f,t)"],
        #["!(&(f,t))"],
        #["|(&(t,f,t),t)"],
        #["|(f,&(t,t))"],
        [
            "!("
                "&("
                    "!(t),"
                    "!("
                        "!(&(f))"
                    "),"
                    "&("
                        "&("
                            "!(&(f)),"
                            "&(t),"
                            "|(f,f,t)"
                        "),"
                        "&(t),"
                        "&(t,t,f)"
                    ")"
                ")"
            ")"
        ]
        # Approach: Tomar todas las funciones dentro de una funcion iterando el string, y cada una de las inner
        # funcions procesarlas recursivamente con el approach divide and conquer.
    ],
    [
        #False,
        #True,
        #True,
        #True,
        #True,
        True
    ],
        parse_bool_expr
    )
