from abc import ABC, abstractmethod

from app.ingestion.pipeline_context import PipelineContext


class BaseStage(ABC):
    """
    Base class for every pipeline stage.
    """

    @abstractmethod
    def process(
        self,
        context: PipelineContext,
    ) -> None:
        """
        Process the pipeline context.
        """
        pass