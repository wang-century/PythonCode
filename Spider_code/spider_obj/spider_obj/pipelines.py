# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class SpiderObjPipeline(object):
    def open_spider(self,spider):
        myclient = pymongo.MongoClient("mongodb://192.168.37.128:27017/")
        self.mydb = myclient["books"]

    def process_item(self, item, spider):
        mycol = self.mydb[item['type']]
        # yes_or_no = False if len([i for i in mycol.find(item)]) > 0 else True
        # if yes_or_no:
        mycol.insert_one(item)
        # if spider.name == 'book3':
        #     yes_or_no = False if len([i for i in mycol.find({'name':item['name']})]) > 0 else True
        #     if yes_or_no:
        #         mycol.insert_one(item)
        #     else:
        #         content = [i for i in mycol.find({'name':item['name']})][0]
        #         item['content'] = content['content'] + '\n' + item['content']
        #         mycol.update_one(content, { "$set": { "content": item['content'] } })

        return item


