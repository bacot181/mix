
from pymongo import MongoClient, errors
import logging
from pymongo.errors import DuplicateKeyError

DATABASE_URI =  "mongodb+srv://novaapp53:nimas123@cluster0.dvag6lu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dbclient = MongoClient(DATABASE_URI)
db = dbclient["Auto"]
col = db["DMUTE"]

# Create unique index on dmute column
col.create_index([("dmute", 1)], unique=True)

# Function to save dmute to the database
async def save_dmute(dmute):
    data = {"dmute": dmute}
    try:
        col.insert_one(data)
        logger.info(f"dmute {dmute} successfully added to the database.")
    except DuplicateKeyError:
        logger.warning(f"dmute {dmute} already exists in the database.")
    except Exception as e:
        logger.error(f"Error while saving dmute: {e}")

# Function to get dmute from the database
def get_dmute(dmute):
    try:
        user_data = col.find_one({"dmute": dmute})
        return user_data["dmute"] if user_data else None
    except Exception as e:
        logger.error(f"Error while fetching dmute: {e}")
        return None

# Function to fetch all dmute values from the database
async def get_all_dmute():
    try:
        dmutes = col.find({}, {"_id": 0, "dmute": 1})
        dmute_list = [dmute["dmute"] for dmute in dmutes]
        return dmute_list
    except Exception as e:
        logger.error(f"Error while fetching dmute values: {e}")
        return []

# Function to remove dmute from the database
async def remove_dmute(dmute):
    try:
        col.delete_one({"dmute": dmute})
        logger.info(f"dmute {dmute} successfully removed from the database.")
    except Exception as e:
        logger.error(f"Error while removing dmute: {e}")
        