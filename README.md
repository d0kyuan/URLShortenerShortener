<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">國泰產險 Python面試考題</h3>

</p>

<!-- GETTING STARTED -->

## 基本建置

### Flask 執行環境

-   python3 package
    ```sh
    pip3 install - requirements.txt
    ```

### 資料庫

1. 建立 demo 資料庫

## 使用

-   啟動服務
    ```sh
    python3 ./manage.py
    ```
    ```
    run on http://0.0.0.0:8080
    ```

## API DOC

```
http://192.168.0.4:8080/api/spec
```

## 範例

-   新增短網址

    ```sh
    POST
    http://192.168.0.4:8080/api/url/insert?url=https%3A%2F%2Fwww.w3schools.com%2Fjsref%2Fmet_his_back.asp
    ```

-   前往短網址
`sh POST http://192.168.0.4:8080/s/NPf0279qW9 `
<!-- LICENSE -->

## License

袁瑞彤 Ray
