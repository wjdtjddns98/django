from django.db import models

class CommonModel(models.Model):

    #현제 데이터 생성 시간을 기준으로 생성 -> 이후 수정x
    created_at = models.DateTimeField(auto_now_add=True)
    #현제 데이터 생성 시간을 기준으로 생성 -> 이후 수정시마다 갱신
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 이 모델은 추상 모델로, 데이터베이스에 테이블을 생성하지 않음
        # 다른 모델에서 상속받아 사용하기 위한 용도
