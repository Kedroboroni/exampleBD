from sqlalchemy import create_engine
from model import Base




if __name__ == "__main__":

    BB_URL = r"sqlite:///C:\WorkSpace\Python\projectGSH\ctrRecBase.db"
    engine = create_engine(BB_URL, echo=True)
    Base.metadata.create_all(engine)
