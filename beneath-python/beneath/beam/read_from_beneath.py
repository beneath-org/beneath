"""
  This module implements reading data from Beneath into a Beam pipeline
"""

import apache_beam as beam

class ReadFromBeneath(beam.PTransform):
  def __init__(self, stream):
    self.stream = stream

  def expand(self, pvalue):
    stream = self.stream
    query = "select * from `{}`".format(stream.bigquery_name())
    return (
        pvalue
        | beam.io.Read(beam.io.BigQuerySource(query=query, use_standard_sql=True))
    )
