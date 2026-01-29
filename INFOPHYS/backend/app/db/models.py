from sqlalchemy import Column, Integer, String, Float, JSON
from .session import Base

class Run(Base):
    __tablename__ = "runs"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)
    config = Column(JSON)
    status = Column(String)

class StepMetric(Base):
    __tablename__ = "step_metrics"
    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, index=True)
    t = Column(Integer, index=True)
    reward = Column(Float)
    info = Column(JSON)