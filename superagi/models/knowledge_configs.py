from sqlalchemy import Column, Integer, Text, String
import requests
from superagi.models.base_model import DBBaseModel
#marketplace_url = "https://app.superagi.com/api"
marketplace_url = "http://localhost:8001"


class KnowledgeConfigs(DBBaseModel):
    """
    Knowledge related configurations such as model, data_type, tokenizer, chunk_size, chunk_overlap, text_splitter, etc. are stored here.
    Attributes:
        id (int): The unique identifier of the knowledge configuration.
        knowledge_id (int): The identifier of the associated knowledge.
        key (str): The key of the configuration setting.
        value (str): The value of the configuration setting.
    """

    __tablename__ = 'knowledge_configs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    knowledge_id = Column(Integer)
    key = Column(String)
    value = Column(Text)

    def __repr__(self):
        """
        Returns a string representation of the Knowledge Configuration object.
        Returns:
            str: String representation of the Knowledge Configuration.
        """
        return f"KnowledgeConfiguration(id={self.id}, knowledge_id={self.knowledge_id}, key={self.key}, value={self.value})"
    
    @classmethod
    def fetch_knowledge_config_details_marketplace(knowledge_id: int):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            marketplace_url + f"/knowledge_configs/marketplace/details/{str(knowledge_id)}",
            headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return []