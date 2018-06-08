# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
class MeizituPipeline(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'Referer':'http://www.mzitu.com/',
                        }
    def process_item(self, item, spider):
        filename = item['title'] + os.path.splitext(item['photo'])[-1]
        with open('./meizitus4/%s'%filename,'wb') as fp:
            response = requests.get(url=item['photo'],headers=self.headers)
            fp.write(response.content)
        return item
