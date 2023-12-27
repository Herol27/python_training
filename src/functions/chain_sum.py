def chain_sum(num: int):
    res = num

    def nested_chain_sum(nested_num: int = None):
        nonlocal res
        if not nested_num:
            return res
        res += nested_num
        return nested_chain_sum

    return nested_chain_sum


if __name__ == '__main__':
    print(chain_sum(1)(2)(3)(4)())
