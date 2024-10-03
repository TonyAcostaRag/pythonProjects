from tests import TestExecutor


def integer_to_english_words(num):
    units = ['0', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
             'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['0', '0', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand ', 'Million ', 'Billion ']

    if num == 0:
        return "Zero"

    scale = 0
    whole_phrase = ''
    while num > 0:

        if num % 1000 != 0:
            chunk = num % 1000
            chunk_string = ''

            if chunk >= 100:
                chunk_string += units[chunk // 100] + ' Hundred '
                chunk %= 100

            if chunk >= 20:
                chunk_string += tens[chunk // 10] + ' '
                chunk %= 10

            if chunk > 0:
                chunk_string += units[chunk] + ' '

            whole_phrase = chunk_string + thousands[scale] + whole_phrase
        scale += 1
        num //= 1000

    return whole_phrase.strip()


if __name__ == '__main__':
    TestExecutor.execute_function([
        [123],
        [12345],
        [1234567],
        [0],
        [1000010],
        [20],
        [50868]
    ],
        [
            "One Hundred Twenty Three",
            "Twelve Thousand Three Hundred Forty Five",
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
            "Zero",
            "One Million Ten",
            "Twenty",
            "Fifty Thousand Eight Hundred Sixty Eight"
        ],
        integer_to_english_words
    )
