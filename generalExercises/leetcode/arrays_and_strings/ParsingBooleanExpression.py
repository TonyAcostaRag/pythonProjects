from tests import TestExecutor


def parse_bool_expr(expression: str):

    def evaluate_single_expression(single_expression):
        if len(single_expression) == 1:
            return True if single_expression == 't' else False

        if single_expression[0] == '&':
            return False if 'f' in single_expression else True
        elif single_expression[0] == '|':
            return True if 't' in single_expression else False
        elif single_expression[0] == '!':
            return True if single_expression[2:-1] == 'f' else False

    def is_single_operation(expression):
        for i in ['&', '|', '!']:
            if i in expression[2:-1]:
                return False
        return True

    def get_inner_operators(expression):

        for i in ['&', '|', '!']:
            if i in expression[2:]:
                break
        else:
            return None, expression

        expressions_list = []
        single_exp = ''
        parenthesis_count = 0
        for i in range(2, len(expression) - 1):
            if (expression[i] == ','
                    and (expression[i - 1] == ')'
                         or expression[i - 1] == 'f'
                         or expression[i - 1] == 't')):
                continue
            single_exp += expression[i]
            if expression[i] == '(':
                parenthesis_count += 1
            elif expression[i] == ')':
                parenthesis_count -= 1
            elif parenthesis_count == 0 and (expression[i] == 't' or expression[i] == 'f'):
                expressions_list.append(single_exp)
                single_exp = ''
            if parenthesis_count == 0 and len(single_exp) > 2 and '(' in single_exp:
                expressions_list.append(single_exp)
                single_exp = ''

        return expression[:2], expressions_list

    outer_operator, inner_operators = get_inner_operators(expression)

    if is_single_operation(expression):
        return evaluate_single_expression(inner_operators)

    evaluated_operations = ''
    for inner_op in inner_operators:
        if is_single_operation(inner_op):
            evaluated_operations += 't' if evaluate_single_expression(inner_op) else 'f'
        else:
            evaluated_operations += 't' if parse_bool_expr(inner_op) else 'f'

    return parse_bool_expr(outer_operator + evaluated_operations + ')')


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["&(|(f))"],
        ["|(f,f,f,t)"],
        ["!(&(f,t))"],
        ["|(&(t,f,t),t)"],
        ["|(f,&(t,t))"],
        ["!(&(!(t),!(!(&(f))),&(&(!(&(f)),&(t),|(f,f,t)),&(t),&(t,t,f))))"]
    ],
    [
        False,
        True,
        True,
        True,
        True,
        True
    ],
        parse_bool_expr
    )
