from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             # transport://userid:password@hostname:port/virtual_host
             broker='amqp://testcr:testcr1234@localhost/testcr',
             # Celery의 백엔드는 테스크 결과를 저장하는 경로
             # rpc는 결과를 AMQP 메시지로 보내는 것을 의미합니다.
             backend='rpc://',
             # include 인수는 Celery Worker를 시작할 때 가져올 모듈의 리스트를 지정합니다.
             include=['test_celery.tasks'])