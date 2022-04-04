# SQL

[toc]

## 1. SQL 개념

> SQL(StructuredQueryLanguage)는 관계형 데이터베이스 관리시스템(RDBMS)의데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.



**SQL 문법의 세가지 종류**

- **DDL - 데이터 정의 언어**
  - CREATE
  - DROP
  - ALTER
- **DML - 데이터 조작 언어**
  - INSERT
  - UPDATE
  - DELETE
  - SELECT
- DCL - 데이터 제어 언어
  - GRANT
  - REVOKE
  - COMMIT
  - ROLLBACK


## 2. sqlite
### 1. Database 생성

> 해당하는 데이터베이스 파일이 있으면 해당DB를 콘솔로 연다. 
>
> 만약 해당하는 파일이 없으면 새로 생성하고, 해당 DB를 콘솔로 연다.

```sqlite
$ sqlite3 database

ex)
$ sqlite3 tutorial.sqlite3    -- 1. 콘솔로 DB를 열고,
sqlite> .databases            -- 2.데이터베이스 목록을 확인한다.
```



**CSV 파일 불러오는 명령어**

> 주의사항)
>
> `.`으로 시작하는 모든 명령어는 SQLite에서 데이터베이스를 조금 더 편리하게 다루기 위해 제공하는 명령어이며, SQL 문법에 속하지 않는다.

```sqlite
sqlite> .mode csv
sqlite> .import 파일명.csv 테이블명

ex)
sqlite> .import users.csv users_user -- users.csv 파일을 users_user 테이블에 전부 집어 넣겠다.
```



### 2. 테이블 생성 및 삭제 

> 데이터 타입의 종류는 INTEGER, TEXT, REAL, NUMERIC, BLOB 등이 존재한다.
>
> 자세한 내용은 [SQLite3 공식문서](https://sqlite.org/datatype3.html)를 참조한다.
>
> - 데이터 베이스(.sqlite3 파일) 하나에 여러 개의 테이블 존재 가능



**테이블 생성 (CREATE)**

```sql
CREATE TABLE table (
  column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);
```



**테이블 생성 with NOT NULL 조건 예시**

```sql
CREATE TABLE table (
  id INTEGER PRIMARY KEY, -- AUTOINCREMENT Option은 지워진 데이터의 재사용 여부
  name TEXT NOT NULL,
  age INT NOT NULL,
  ...
);
```

 

**테이블 및 스키마 조회 명령어** **(!= SQL 명령어 아님)**

```sqlite
sqlite> .tables          -- 테이블 목록 조회
sqlite> .schema table    -- 특정 테이블 스키마 조회
```



**테이블 제거 (DROP)**

```sql
sqlite> DROP TABLE classmates;
sqlite> .tables -- 테이블 제거 확인
```



### 3. 데이터 추가, 읽기, 수정 및 삭제

**추가 (INSERT)**

```sql
INSERT INTO table (column1, column2, ...)
VALUES(value1, value2);
```



**조회 (SELECT)**

> 참고)
>
> SQL은 세미콜론(;)을 만나기 전까지 절대 실행되지 않습니다.
>
> 따라서 아래 LIMIT 예시와 같이 들여쓰기를 비교적 자유롭게 할 수 있습니다.

```sql
-- 모든 컬럼 가져오기 --
SELECT * FROM table;

-- 특정 컬럼 가져오기 --
SELECT column1, column2 FROM table;

-- LIMIT: 원하는 개수(num)만큼 가져오기 -- 
SELECT column1, column2
FROM table
LIMIT num;

-- OFFSET: 특정 위치에서부터 가져올 때 --
-- (맨 위부터 num만큼 떨어진 값부터 가져온다는 의미)
SELECT column1, column2
FROM table
LIMIT num OFFSET num;

-- WHERE: 조건을 통해 값 가져오기 --
SELECT column1, column2
FROM table
WHERE column=value;

-- DISTINCT: 중복없이 가져오기 -- 
SELECT DISTINCT column FROM table;
```



**삭제 (DELETE)**

```sql
DELETE FROM table
WHERE condition;

ex)
DELETE FROM classmates
WHERE name='김싸피';
```



**수정 (UPDATE)**

```sql
UPDATE table
SET column1=value1, column2=value2, ...
WHERE condition;

ex)
-- 김싸피의 이름을 김삼성으로 바꾼다고 하면... --
UPDATE classmates
SET name='김싸피', address='대한민국'
WHERE name='김삼성';
```



**예시와 함께하는 WHERE문 심화 (READ)**

```sql
-- Q.users에서 age가 30이상인 사람만 가져온다면? --

SELECT * FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상인 사람의 이름만 가져온다면? --

SELECT first_name FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 가져온다면? --
SELECT age, last_name FROM users
WHERE age >= 30 and last_name='김';
```



### 4. 심화 SQL문

> SELECT를 통해 데이터를 조회(Read)하는 다양한 방법
>
> - 실행 순서
>   1. FROM
>   2. WHERE
>   3. GROUP BY
>   4. HAVING
>   5. SELECT
>   6. ORDER BY
> - 문법 순서: `SELECT <컬럼> FROM <테이블> WHERE <조건> GROUP BY <컬럼> HAVING <그룹조건> ORDER BY <컬럼>;`
> - 실행 순서:   (5)-------------------(1)------------------(2)-----------------(3)----------------------(4)------------------------(6)



#### Expressions

- COUNT (레코드 값들의 개수 반환)

  ```sql
  SELECT COUNT(*) FROM users;
  ```

- AVG (레코드 값들의 평균값 반환)

  ```sql
  SELECT AVG(age)
  FROM users
  WHERE age >= 30;
  ```

- MAX (레코드 값들의 최대값 반환)
- MIN (레코드 값들의 최소값 반환)
- SUM (레코드 값들의 합 반환)



#### LIKE

> LIKE는 두 가지 와일드 카드(언더스코어 그리고 퍼센트 기호)와 함께 동작한다.

- `-` (반드시 이 자리에 한 개의 문자가 존재해야 한다는 뜻)

  ```sql
  -- 20대인 사람들만 가져올 때 --
  SELECT *
  FROM users
  WHERE age LIKE '2_';
  ```

- `%` (이 자리에 문자열이 있을 수도, 없을 수도 있다. 0개 이상이라는 뜻)

  ```sql
  -- 지역번호가 02인 사람만 가져올 때 --
  SELECT *
  FROM users
  WHERE phone LIKE '02-%';
  ```

- 두 개를 조합해서 사용할 수도 있다.

  ```sql
  -- 핸드폰 중간 번호가 반드시 4자리면서 511로 시작되는 사람들 --
  
  SELECT * FROM users
  WHERE phone LIKE '%-511_-%';
  ```



**정렬 (ORDER BY)**

```sql
SELECT columns FROM table
ORDER BY column1, column2 ASC | DESC;

-- ASC: 오름차순 / DESC: 내림차순 --
```

```sql
-- 나이, 성 순서로 오름차순 정렬하여 상위 10개만 뽑아보면? --
SELECT * 
FROM users
ORDER BY age, last_name ASC -- 2개 이상의 정렬 기준을 갖는 경우 ,로 분리 가능하며 ASC는 기본값이기 때문에 생략 가능합니다.
LIMIT 10;
```



**GROUP BY**

> 지정된 기준에 따라 행 세트를 그룹으로 결합한다.
>
> 데이터를 요약하는 상황에서 주로 사용한다.

```sql
SELECT column1, aggregate_function(column_2)
FROM table
GROUP BY column1, column2;
```

```sql
-- 성(last_name)씨가 몇 명인지 조회할 때 --
-- AS 구문을 통해 요약되는 컬럼의 이름을 변경할 수 있습니다.
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
```



**ALTER**

- 테이블명 변경

  ```sql
  ALTER TABLE 기존테이블명
  RENAME TO 새로운테이블명;
  ```

- 새로운 컬럼 추가

  ```sql
  ALTER TABLE 테이블명
  ADD COLUMN 컬럼명 datatype;
  ```

  

## 3. MySQL

### 1. SELECT

1. 모든 내용 보기

   - 테이블의 모든 컬럼: `*`(asterisk)

   ```mysql
   SELECT * FROM Customers;
   -- 이와 같이 주석을 달 수 있습니다.
   ```

2. 원하는 컬럼만 골라서 보기

   - `SELECT <컬럼명> FROM <테이블명>`

   - 테이블의 컬럼이 아닌 값 선택

   ```mysql
   SELECT
     CustomerName, 1, 'Hello', NULL
   FROM Customers;
   ```

3. 원하는 조건의 행만 걸러서 보기

   - `WHERE <조건>`

4. 원하는 순서로 데이터 가져오기

   - `ORDER BY <기준컬럼> <방향>`
     - `ASC`: 오름차순, 기본값
     - `DESC`: 내림차순

   ```mysql
   SELECT * FROM OrderDetails
   ORDER BY ProductID ASC, Quantity DESC;
   ```

5. 원하는 만큼만 데이터 가져오기

   - `LIMIT <가져올 갯수>`
   - `LIMIT <건너뛸 갯수> <가져올 갯수>`

6. 원하는 별명(alias)으로 데이터 가져오기

   - `<컬럼명> AS <별명>`



### 2. 연산자

[공식문서](https://dev.mysql.com/doc/refman/8.0/en/non-typed-operators.html)

1. 사칙연산

   - `+`, `-`, `*`, `/`: 사칙 연산
   - `%`, `MOD`: 나머지

   ```mysql
   SELECT 5 - 2.5 AS DIFFERENCE;
   SELECT 'ABC' + 3;
   -- 문자열에 사칙연산을 가하면 0으로 인식
   SELECT '1' + '002' * 3;
   -- 숫자로 구성된 문자열은 숫자로 자동인식
   SELECT
     ProductName,
     Price / 2 AS HalfPrice
   FROM Products;
   ```

2. 참/거짓 연산자

   - TRUE는 1, FALSE는 0
   - `WHERE`문에서 조건을 지정할 때 사용
   - `IS`: 양쪽이 모두 TRUE 또는 FALSE
   - `IS NOT`: 한쪽은 TRUE, 한쪽의 FALSE
   - `&&`, `AND`: 양쪽이 모두 TRUE일 때만 TRUE
   - `||`, `OR`: 한쪽이 TRUE면 TRUE
   - `=`, `!=`, `<>`(양쪽 값이 다름, `!=`와 동일), `>`, `<`, `>=`, `<=`
     - 문자열도 비교 가능, 대소문자 구분 안함
   - 테이블의 컬럼이 아닌 값으로 선택

   ```mysql
   SELECT
     ProductName, Price,
     Price > 20 AS EXPENSIVE 
   FROM Products;
   
   SELECT
     ProductName, Price,
     NOT Price > 20 AS CHEAP 
   FROM Products;
   ```

   - `BETWEEN <최소> AND <최대>`, `NOT BETWEEN <최소> AND <최대>`
   - `IN (값1, 2, 3)`, `NOT IN (값1, 2, 3)`

   ```mysql
   SELECT * FROM Customers
   WHERE City IN ('Torino', 'Paris', 'Portland', 'Madrid') 
   ```

   - `LIKE `
     - `%`: 0또는 N개의 문자를 가진 패턴
     - `_`: 1개의 문자를 가진 패턴



### 3. 숫자와 문자열 함수

[숫자 관련 함수 공식 문서](https://dev.mysql.com/doc/refman/8.0/en/numeric-functions.html)

1. 숫자 관련 함수

   - `ROUND`: 반올림
   - `CEIL`: 올림
   - `FLOOR`: 내림
   - `ABS`: 절대값
   - `GREATEST(값1, 2, 3)`: 값들 중 가장 큰 값

   ```mysql
   SELECT 
     GREATEST(1, 2, 3),
     LEAST(1, 2, 3, 4, 5);
   ```

   - `LEAST(값1, 2 ,3)`: 가장 작은 값

   ```mysql
   SELECT
     OrderDetailID, ProductID, Quantity,
     GREATEST(OrderDetailID, ProductID, Quantity),
     LEAST(OrderDetailID, ProductID, Quantity)
   FROM OrderDetails;
   ```

   - `POW(A, B)`, `POWER(A, B)`: A를 B만큼 제곱
   - `SQRT`: 제곱근
   - `TRUNCATE(N, n)`: N의 소숫점 n자리까지
     - 반올림이 아니라 그냥 해당 자리까지 표시
     - n에 음수가 들어가면 1의 자리부터 0으로 표시

2. 숫자 관련 집계 함수

   - `MAX`: 최댓값
   - `MIN`: 최솟값
   - `COUNT`: NULL 제외한 갯수
   - `SUM`: 총합
   - `AVG`: 평균

   ```mysql
   SELECT
     MAX(Quantity),
     MIN(Quantity),
     COUNT(Quantity),
     SUM(Quantity),
     AVG(Quantity)
   FROM OrderDetails
   WHERE OrderDetailID BETWEEN 20 AND 30;
   ```

3. 문자열 관련 함수

   - `UCASE`, `UPPER`: 모두 대문자로
   - `LCASE`, `LOWER`: 모두 소문자로
   - `CONCAT(값1, 2, 3)`: 괄호 안의 내용 이어붙임

   ```mysql
   SELECT CONCAT('HELLO', ' ', 'THIS IS ', 2021);
   SELECT CONCAT('O-ID: ', OrderID) FROM Orders;
   ```

   - `CONCAT_WS(S, 값1, 2, 3)`: 괄호 안의 내용 S를 기준으로 이어붙임

   ```mysql
   SELECT CONCAT_WS('-', 2021, 8, 15, 'AM');
   SELECT
     CONCAT_WS(' ', FirstName, LastName) AS FullName
   FROM Employees;
   ```

   - `SUBSTR`, `SUBSTRING`: 주어진 값에 다라 문자열 자름

   ```mysql
   SELECT
     SUBSTR('ABCDEFG', 3),		-- 처음부터 3개
     SUBSTR('ABCDEFG', 3, 2),	-- 3번째 부터 2개
     SUBSTR('ABCDEFG', -4),	-- 뒤에서부터 4개
     SUBSTR('ABCDEFG', -4, 2);	-- 뒤에서 4번째 부터 2개
   ```

   - `LEFT(S, N)`: S의 왼쪽부터 N글자
   - `RIGHT(S, N)`: S의 오른쪽부터 N글자
   - `LENGTH`: 문자열의 바이트 길이
   - `CHAR_LENTH`, `CHARACTER_LEGNTH`: 문자열의 문자 길이
   - `TRIM`: 양쪽 공백 제거
   - `LTRIM`: 왼쪽 공백 제거
   - `RTRIM`: 오른쪽 공백 제거
   - `LPAD(S, N, P)`: S가 N글자가 될 때까지 P를 왼쪽에 이어붙임
   - `RPAD(S, N, P)`: S가 N글자가 될 때까지 P를 오른쪽에 이어붙임
   - `REPLACE(S, A, B)`: S에서 A를 B로 변경
   - `INSTR(S, s)`: S중 첫 번째 s의 위치를 반환, 없으면 0 반환
   - `CAST(A, T)`: A를 T 자료형으로 변환
