class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        def is_int(string):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]
            return string.isdigit()

        def is_dec(string):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]

            if '.' not in string:
                return False

            before_dot, after_dot = string.split('.', 1)
            if before_dot == '' and after_dot == '':
                return False
            if before_dot != '' and not before_dot.isdigit():
                return False
            if after_dot != '' and not after_dot.isdigit():
                return False
            return True

        if 'e' in s or 'E' in s:
            parts = s.lower().split('e')
            if len(parts) != 2:
                return False
            base, exp = parts
            return (is_int(base) or is_dec(base)) and is_int(exp)
        else:
            return is_int(s) or is_dec(s)