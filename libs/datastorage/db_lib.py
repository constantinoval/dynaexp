from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from libs.datastorage.tables import *
import os

def open_session(engine: str)->Session:
    engine = create_engine(engine, echo=False)
    Base.metadata.create_all(engine)
    return Session(engine)

def create_test_database():
    if os.path.exists("test.db"):
        os.remove("test.db")
    engine = create_engine("sqlite:///test.db", echo=False)
    Base.metadata.create_all(engine)
    session = Session(engine)
    ep1 = ElasticProperties(name='Сталь', E=185000, c=4850)
    ep2 = ElasticProperties(name='Дюраль', E=74000, c=5150)
    str1 = Striker(D=20, L=300, material=ep1)
    session.add_all([ep1, ep2, str1])
    session.commit()
    session.close()


if __name__ == "__main__":
    create_test_database()
    session = open_session('sqlite:///test.db')
    for m in session.query(ElasticProperties).all():
        print(m)
    for striker in session.query(Striker).all():
        print(striker)
    session.close()
    #     im1 = DBImage(r'D:\Projects\Dynaexp\data\Img000000.jpg')
    #     session.add(im1)
    #     im2 = DBImage(r'D:\Projects\Dynaexp\data\Img000000.jpg')
    #     session.add(im2)
    #     vid1 = DBVideo(frames=[im1, im2], frame_rate=70000)
    #     session.add(vid1)
    #     # steel = ElasticProperties(name="Сталь", E=200000, rho=7800, c=4850)
    #     # session.add(steel)
    #     # circle = Section(section_type=SectionTypes.circle, par1=10)
    #     # session.add(circle)
    #     # tube = Section(section_type=SectionTypes.tube, par1=20, par2=15)
    #     # session.add(tube)
    #     # str1 = Striker(material=steel, section=circle, length=300)
    #     # session.add(str1)
    #     # bar1 = MeasureBar(material=steel, length=1000, section=circle, dispersion_data={"a": [1, 2, 3], "b": [3, 1, 5]})
    #     # session.add(bar1)
    #     # bar2 = MeasureBar(material=steel, length=3000, section=tube)
    #     # session.add(bar2)
    #     # tension = ExperimentType(code='t', description="Прямое растяжение образца")
    #     # session.add(tension)
    #     # compression = ExperimentType(code='c', description="Сжатие образца")
    #     # session.add(compression)
    #     # mat1 = Material(name="Огнеупор", code=800, description="Поставка СПБ от Смирнова")
    #     # session.add(mat1)
    #     # j1 = Jacket(R=15, R0=10, length=10, material=steel)
    #     # session.add(j1)
    #     # ch1 = OscChannel(tarir=1, bar=bar1)
    #     # session.add(ch1)
    #     # ch2 = OscChannel(tarir=1, jacket=j1)
    #     # session.add(ch2)
    #     # ch3 = OscChannel(tarir=1)
    #     # session.add(ch3)
    #     # ch4 = OscChannel(tarir=1, bar=bar2)
    #     # session.add(ch4)
    #     # shpb_setup = Setup(channels=[ch1, ch4, ch2, ch3])
    #     # shpb_setup.set_creation_time()
    #     # session.add(shpb_setup)
    #     session.commit()
    #
    # with Session(engine) as session:
    #     # materials = session.query(ElasticProperties).all()
    #     # for mat in materials:
    #     #     print(mat)
    #     # sections = session.query(Section).all()
    #     # for sec in sections:
    #     #     print(sec)
    #     # strikers = session.query(Striker).all()
    #     # for st in strikers:
    #     #     print(st)
    #     # bars = session.query(MeasureBar).all()
    #     # for b in bars:
    #     #     print(b)
    #     # for exp_type in session.query(ExperimentType).all():
    #     #     print(exp_type)
    #     # for mat in session.query(Material).all():
    #     #     print(mat)
    #     # for dat in session.query(Gauge).all():
    #     #     print(dat)
    #     # for j in session.query(Jacket).all():
    #     #     print(j)
    #     # for ch in session.query(OscChannel).all():
    #     #     print(ch)
    #     # for s in session.query(Setup).all():
    #     #     print(s)
    #     vid1 = session.query(DBVideo).one()
    #     print(vid1.frames)
    #     print(vid1.frame_rate)