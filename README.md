# MOVA_BACKEND
## [스파르타코딩클럽 내일배움캠프 AI 3기] A4팀 최종 프로젝트
![image](https://user-images.githubusercontent.com/112370211/207631093-78907a55-d513-4d50-9513-ed0e79c8104b.png)


## 프로젝트 소개
저희 Mova(모바)는 각 플랫폼 별 웹툰 모아보기, 웹툰 커뮤니티, 팬아트 제작 등 웹툰에 대한 애정을 느낄 수 있게 만드는 웹 페이지입니다.


## 개발기간
2022.11.30 - 12.28

## front-end github-address
[MOVA_Frontend](https://github.com/marinred/MOVA_Frontend)

## 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" align='left'/>
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white" align='left'/>
<img src="https://img.shields.io/badge/django rest framework-092E20?style=for-the-badge&logo=&logoColor=white" align='left'/>
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white" align='left'>
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" align='left'>
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" align='left'>
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white" align="left">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white" align='left'>
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" align="left">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white" align="left">
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" align="left">
<img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" align="left">
<img src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white" align="left">
<img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" align="left">
<img src="https://img.shields.io/badge/Docker-2496ed?style=for-the-badge&logo=docker&logoColor=white" align="left">
<br>
<br>
<br>
<br>

## 저작권

만화저작권 보호협의회 만화저작권 침해 단속 가이드라인  
http://www.comicright.or.kr/?page=43

1. 상식적인 범위 내에서의 인용 및 리뷰용 이미지 명장면 등 컷 단위 이미지(속칭 짤방) 
   <br>(총 3페이지 이하만 허용, 연속된 페이지 인용은 불가)
   
2. 명장면 등, 컷 단위 이미지(짤방) 허용   
    제한사항 (리뷰가 사용된 전체 페이지 누적해서 총 20컷 이하만 허용, 연속된 컷은 5컷 이하만 허용)
    
3. 패러디: 원작의 악의적인 심각한 훼손 및 이유 없는 작가의 비방물은 패러디로 인정하지 않는다.


## 아키텍쳐

![스크린샷 2022-12-27 오후 2 36 00](https://user-images.githubusercontent.com/113073174/209745765-8d45aa1b-d4d9-4e6a-a49f-5ee9885e50dc.png)



## 역할 파트
**front-end** :
- 회원가입, 로그인,  회원탈퇴, 비밀번호 찾기, 회원정보 수정: 정진엽님
- 메인 페이지, 웹툰상세페이지, 소셜 로그인:  주세민님, 염보미님
- 게시글(공지사항, 토론, 팬 게시판):  임동근님
- 팬아트 게시판: 이태규님
- 배포: 염보미님

**back-end** :
- 회원가입, 로그인,  회원탈퇴, 비밀번호 찾기, 회원정보 수정: 정진엽님
- 웹툰 크롤링, 웹툰 리뷰, 좋아요, 북마크, 소셜 로그인:  주세민님, 염보미님
- 게시글(공지사항, 토론, 팬 게시판):  임동근님
- 팬아트 게시판: 이태규님

## 주요 기능
1. 회원 가입 / 로그인
    - 회원 가입
    - 로그인
    - 소셜 로그인
2. 프로필페이지
    - 프로필
    - 좋아요 클릭된 웹툰 GET
3. 프로필수정페이지
    - 프로필 수정
    - 회원탈퇴
    - 비밀번호 변경
4. 메인페이지
    - 네이버 오늘의 웹툰 view
    - 카카오 오늘의 웹툰 view
    - 내가 북마크한 웹툰 view
    - 전체 웹툰 중 제목, 장르, 작가로 원하는 웹툰 검색하는 기능
5. 웹툰상세페이지
    - 각 웹툰의 상세정보 표시
    - 좋아요/북마크
    - 웹툰 보러가기
    - 댓글 보기/작성/수정/삭제
6. 공지사항
    - 공지사항 list get 
    - 공지사항 title 검색
    - 버튼을 이용하여 카테고리(공지사항, 이벤트) 구분
    - 공지사항 카테고리별 작성
7. 공지사항상세페이지
    - 공지사항 상세보기
    - 공지사항 관리자 권한을 가진 이용자만 수정, 삭제 가능
    - 공지사항 수정
    - 공지사항 삭제
    - 공지사항/이벤트 카테고리별 작성
8. 토론방/팬게시판페이지
    - 토론방/팬게시판 list get 
    - 토론방/팬게시판 title 검색
    - 버튼을 이용하여 카테고리(토론방, 팬게시판) 구분
9. 토론방/게시판 상세페이지
    - 게시판 카테고리 설정
    - 게시글 작성 내 웹툰 검색
    - 게시글 작성
    - 게시글 작성자만 수정/삭제 가능  
10. 팬아트페이지
    - 웹툰별 팬아트 게시글 리스트 출력
    - 좋아요 순위로 팬아트 게시글 리스트 출력
11. 팬아트상세페이지
    - 팬아트 게시글
    - 좋아요기능, 댓글달기, 댓글 삭제기능
12. 팬아트 작성페이지
    - 게시글 작성
    - 채색하기 기능
    - 스케치 따기 기능
    
## 와이어프레임
[https://www.figma.com/file/PQ2QMjtryocR803csfCQdL/Untitled?node-id=0%3A1&t=lqWiwBzbHidYZDRz-0](https://www.figma.com/file/PQ2QMjtryocR803csfCQdL/Untitled?node-id=0%3A1&t=lqWiwBzbHidYZDRz-0)

![와이어프레임](https://user-images.githubusercontent.com/113073174/209744413-8d19478c-f366-4915-8981-51a438cc0cdf.png)


## DB 설계
![ERD](https://user-images.githubusercontent.com/112370211/207582899-17ae8309-d344-48f9-aff1-990e82e3416d.jpg)

## API 설계
- Postman 활용하여 만든 api 명세서
https://documenter.getpostman.com/view/24027867/2s8Z6x2Z38



## 딥러닝 모델
[Colorization_Tool_on_Web](https://github.com/yangco-le/Colorization_Tool_on_Web)

## 프로젝트 시연영상
![image](https://user-images.githubusercontent.com/113073174/207761398-d2db14a7-cdb4-4051-b8b0-61065ee06c98.png)
[프로젝트 시연영상](https://www.youtube.com/watch?v=00SJS3V2pdw&t=3s)


## 트러블 슈팅

[Wiki로 이동](https://github.com/marinred/MOVA_BACKEND/wiki/%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85-%EB%B0%8F-%ED%94%BC%EB%93%9C%EB%B0%B1)
