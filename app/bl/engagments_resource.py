from bson import ObjectId

from app import mongo
from app import logger
from app.bl.adventure_resource import get_adventure_by_id


def create_like(adv_id, uid):
    adventure = get_adventure_by_id(adv_id)
    if not adventure:
        logger.debug("no adventure with id " + str(adv_id))
    if 'likes' in adventure:
        result = mongo.db.adventure.update({'_id': ObjectId(adv_id)},
                                           {'$pull': {'likes': {'liker': uid}}})
        logger.debug(result)
        if result['nModified'] == 0:
            logger.debug("push new like " + str(adv_id))

            mongo.db.adventure.update({'_id': ObjectId(adv_id)},
                                      {'$push': {'likes': {'liker': uid}}})
        else:
            logger.debug("removed like " + str(adv_id))
    else:
        logger.debug('adding new like array for adv={}'.format(adv_id))
        mongo.db.adventure.update({'_id': ObjectId(adv_id)},
                                  {'$set': {'likes': [{'liker': uid}]}})
