from typing import Dict
import uuid

from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
  def __init__(self, activities_repository: ActivitiesRepository) -> None:
    self.__activitiess_repository = activities_repository

  def create(self, body, trip_id: str) -> Dict:
    try:
      activity_id = str(uuid.uuid4())

      activity_infos = {
        'id': activity_id,
        'trip_id': trip_id,
        'title': body['title'],
        'occurs_at': body['occurs_at']
      }

      self.__activitiess_repository.registry_activity(activity_infos)

      return {
        'body': { 'activity_id': activity_id },
        'status_code': 201
      }
    except Exception as exception:
      return {
        'body': { 'error': 'Bad Request', 'message': str(exception) },
        'status_code': 400
      }
