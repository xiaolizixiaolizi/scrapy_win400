# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from .settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline

class GirlImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs=super(GirlImagePipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item
        return  request_objs

    def file_path(self, request, response=None, info=None):
        path=super(GirlImagePipeline,self).file_path(request,response,info)
        category=request.item.get("name")
        image_stores=IMAGES_STORE
        category_path=os.path.join(image_stores,category)
        if not category_path:
            os.mkdir(category_path)

        image_name=path.replace('full/','')
        image_path=os.path.join(category_path,image_name)  #images/name/图片

        return  image_path


















class FemaleStarPipeline(object):
    def process_item(self, item, spider):
        return item
