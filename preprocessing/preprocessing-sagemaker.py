"""
haimtran
sagemaker to preprocess data
"""

import os
from time import strftime
import sagemaker
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput


# sagemaker session
session = sagemaker.Session()
BUCKET_NAME = session.default_bucket()
# s3 data path
raw_s3 = f"s3://{BUCKET_NAME}/data/raw/house_pricing.csv"
# training output path
output_path = f"s3://{BUCKET_NAME}/data/sm_processed"
# sagemaker sklearn processor
sklearn_processor = SKLearnProcessor(
    "0.20.0", os.environ['ROLE'], "ml.m4.xlarge", 1
)
# job name
job_name = f"processing-{strftime('%Y-%m-%d-%H-%M-%S')}"
# sagemaker process data
sklearn_processor.run(
    code="preprocessing.py",
    job_name=job_name,
    inputs=[
        ProcessingInput(
            # source from s3
            source=raw_s3,
            # dest in container
            destination="/opt/ml/processing/input",
            s3_data_distribution_type="ShardedByS3Key",
        )
    ],
    outputs=[
        ProcessingOutput(
            output_name="train",
            # s3 destination
            destination=f"{output_path}/train",
            # local training source
            source="/opt/ml/processing/output/train",
        ),
        ProcessingOutput(
            #
            output_name="test",
            # s3 destination
            destination=f"{output_path}/test",
            # local source
            source="/opt/ml/processing/output/test",
        ),
        ProcessingOutput(
            #
            output_name="validation",
            # s3 destination
            destination=f"{output_path}/validation",
            # local source
            source="/opt/ml/processing/output/validation",
        ),
    ],
)
