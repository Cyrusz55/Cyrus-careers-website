
from sqlalchemy import create_engine
engine = create_engine ("mysql+pymysql://")





from sqlalchemy import create_engine, text
import os



db_connection_str = os.environ['DB_CONNECTION_STRING']







  




  
def load_jobs_from_db():
 with engine.connect() as conn:
   result = conn.execute(text("select * from jobs"))
   jobs = []
   for row in result.all():
     jobs.append(row)
   return jobs

