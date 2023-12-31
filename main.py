from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME_01 = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME_01} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_02 = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME_02} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_03 = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME_03} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME_03} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_04 = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME_04} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME_04} completed <<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_05 = "Model Evaluation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME_05} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME_05} completed <<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


