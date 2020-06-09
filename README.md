# landcover_shp2img
## 실행환경

* Windows

  

## 요구사항

* python3.x
* [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/get-started/install-and-sign-in-to-arcgis-pro.htm)
* [arcpy](https://pro.arcgis.com/en/pro-app/arcpy/get-started/installing-python-for-arcgis-pro.htm)



## 셰이프파일 제공

* [환경공간정보서비스](https://egis.me.go.kr/main.do)

  

## 실행방법

1.  프로젝트 생성

2.  main.py에서 aprx, gdb, tbx 파일 경로 재설정

3.  main.py에서 데이터 경로 설정 (path 변수 수정)

4.  main.py에서 symbologyFields 설정

    * 대분류: symbologyFields = [["VALUE_FIELD", "#", "L1_CODE"]]

    * 중분류: symbologyFields = [["VALUE_FIELD", "#", "L2_CODE"]]
    * 세분류: symbologyFields = [["VALUE_FIELD", "#", "L3_CODE"]]
5.  main.py 실행


