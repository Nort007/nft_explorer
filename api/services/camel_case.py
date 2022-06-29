from humps import camelize


def to_camel_case(datas: str | dict) -> dict | str:
    return camelize(datas)
