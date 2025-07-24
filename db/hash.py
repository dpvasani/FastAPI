from passlib.context import cryptcontext

pwd_cxt = cryptcontext(schemes = 'bcrypt', deprecated = 'auto')


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)