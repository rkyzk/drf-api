# Django Rest Framework API for your-poetry project

## General Introduction
This Django Rest Framework API serves as the backend for "Your Poetry" application -- a platform for sharing poetry.

## Contents
[Overview](## Overview)
[Main-Technologies-Used](## Main Technologies used)
[Features-in-Detail](## Main Technologies used)
[Manual-Testing](## Manual Testing)
[Credits]
[Deployment Procedures]
 
## Overview
This API involves following applications:
1. poems
2. profiles
3. comments
4. likes
5. followers

### 1. poems
- Poem model stores information of poem objects including title, content and created, published & updated dates etc.
- The owner field will be automatically assigned the value of the current user so the person who creates the object doesn't need to enter their own name.
- The owner field will be automatically assigned the value of the current user so the person who creates the object doesn't need to enter their own name.

## Main Technologies
Django Rest Framework

## Manual Testing

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|message at root | go to "https://poetry-6c31c94e3988.herokuapp.com" | Check the displayed information | message "Welcome to my drf API!" is displayed. |message "Welcome to my drf API!" is displayed.| pass||2023/4/30|

### Profiles

|1|A profile is automatically made for a new user. | go to admin panel, add user (username: 'user1' password: 
'swUf8LcR'.) | Go to "/profiles" and check if User object 'user1' is created. | 'user1' is created. |'user1' is created.| pass|[image](./images/manual-tests/DRF-profiles/1&2.png)|2023/7/29|
|2|'sunset.jpg' is set as default profile image. |--| Go to "/profiles" and check if the value of 'image' for user1 is "https://res.cloudinary.com/ds66fig3o/image/upload/v1/media/../sunset.jpg". | The correct URL is set for 'image' field. |The correct URL is set for 'image' field.| pass|[image](./images/manual-tests/DRF-profiles/1&2.png)|2023/7/29|
|3|profile edit if logged in and owner. |log in as admin| Go to "/profiles/1" (1 is admin's id) and update the data as follows: display name: admin display name; about me: Im admin; favorites: my favorites. Click 'PUT.' |The data are updated. |The data are updated.| pass|[image](./images/manual-tests/DRF-profiles/4.png)|2023/7/29|
|4|profile image can be updated. || Go to "/profiles/1" and upload 'test-profile.jpg' Click 'PUT.' |The image URL is updated and contains 'test-profile'. |The image URL is updated. The URL shows 'test-profile.jpg'. | pass|[image1 ](./images/manual-tests/DRF-profiles/4-1.png)[image](./images/manual-tests/DRF-profiles/4-2.png)|2023/7/29|
|5|Profile can't be updated by other users |Log out and log in as user1| Go to "/profiles/1" |The edit form is absent. |The edit form is absent. | pass|[image1 ](./images/manual-tests/DRF-profiles/4-1.png)[image](./images/manual-tests/DRF-profiles/5.png)|2023/7/29|

### Poems

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't create poems if not logged in. | Log out. | Check if the form is displayed. | The form is absent. |The form is absent.| pass|[image](./images/manual-tests/DRF-poems/1.png)|2023/7/29|
|2|Can create poems if logged in. | Log in as user1. | Enter title: title; content: content; category: other; publish: false; and click 'post.' | The new poem 'title' is created.|The new poem 'title' is created.| pass|[image](./images/manual-tests/DRF-poems/2.png)|2023/7/29|
|3|Can update poems |Go to "/poems/7"| Enter title: title updated; content: content updated; category: nature; publish: true; and click 'PUT.' | The poem data is updated.|The poem data is updated.| pass|[image](./images/manual-tests/DRF-poems/3.png)|2023/7/29|
|4|Other users cannot update poems. |Log in as admin and go to "/poems/7"| Check if the edit form is absent | The edit form is absent.|The edit form is absent.| pass|[image](./images/manual-tests/DRF-poems/4.png)|2023/7/29|
|5|Owners can delete their own poems. |Log in as user1 and go to "/poems/7"| Click 'Delete' and go to "/poems/7" | The poem will not be found.|A note indicates 404 error, and that the poem is 'not found.'| pass|[image](./images/manual-tests/DRF-poems/5.png)|2023/7/29|

### Comments
- log in as user1 and make a poem (title: poem 1; content: content; category: 'other'; publish: true)

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can create comments | Log in as admin | Select 'poem 1' and enter 'hello' for content.  Click 'Post.'|Comment 'hello' is created. |Comment 'hello' is created. | pass|[image](./images/manual-tests/DRF-comments/1.png)|2023/7/29|
|2|Can edit comments |--| Update as follows: content: 'hello updated'; Click 'Put.'|Comment is updated. |Comment is updated. | pass|[image](./images/manual-tests/DRF-comments/2.png)|2023/7/29|
|3|can't update comments if logged out |Log out. Go to "/comments/9"| Check if the edit form is present.|The edit form is absent. |The edit form is absent. | pass|[image](./images/manual-tests/DRF-comments/3.png)|2023/7/29|
|4|Other members can't update comments. |Log in as admin. Go to "/comments/| Check if the edit form is present.|The edit form is absent. |The edit form is absent. | pass|[image](./images/manual-tests/DRF-comments/4.png)|2023/7/29|

### Likes

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't like poems if not logged in. | Log out. Go to "/poems." |Check if the form is displayed. |The form is 
absent. |The form is absent. | pass|[image](./images/manual-tests/DRF-likes/1.png)|2023/7/29|
|2|Can like poems if logged in. | Log in as admin. Go to "/likes" |Select 'poem 1' and click 'POST' |Like object is made.|Like object with values owner: admin; poem: 8 (id of 'poem 1') is made. | pass|[image](./images/manual-tests/DRF-likes/2.png)|2023/7/29|
|3|Can't like the same poem twice |--|Select 'poem 1' and click 'POST' |Error will be raised.|Error "possible duplicated" is raised (400 Bad request) |pass|[image](./images/manual-tests/DRF-likes/3.png)|2023/7/29|
|4|Can like one's own poems | Log in as user1. Go to "/likes" |Select 'poem 1' and click 'POST' |Like object is created.|Like object with values owner: user1; poem: 8 (id of 'poem 1') is created. | pass|[image](./images/manual-tests/DRF-likes/2.png)|2023/7/29|

### Followers

Test No.| Feature tested| Preparation Steps if any | Test Steps | Expected results | Actual results | Pass/Fail |Image| Date |
|:---| :--- | :--- |:---| :--- | :--- |:---| :--- |:--- |
|1|Can't follow users if not logged in. | Log out. Go to "/followers" |Check if the form is displayed. |The form is absent. |The form is absent. | pass|[image](./images/manual-tests/DRF-followers/1.png)|2023/7/29|
|2|Can follow users if logged in. | Log in as admin. Go to "/followers" |Select 'user1' and click 'POST' |Follow object is made.|Follow object with values owner: admin; followed_name: user1 is made. | pass|[image](./images/manual-tests/DRF-followers/2.png)|2023/7/29|
|3|Can't follow the same user twice |--|Select 'user1' and click 'POST' |Error will be raised.|Error "possible duplicated" is raised (400 Bad request) |pass|[image](./images/manual-tests/DRF-followers/4.png)|2023/7/29|
|4|Can follow onself |--|Select 'admin' and click 'POST' |A new Follower object is made.|Follower object with values owner: admin and followed_name: admin is created. |pass|[image](./images/manual-tests/DRF-followers/4.png)|2023/7/29|

### Check some fields in profiles


|1|message at root | go to "https://poetry-6c31c94e3988.herokuapp.com" | Check the displayed information | message "Welcome to my drf API!" is displayed. |message "Welcome to my drf API!" is displayed.| pass|[image](./images/manual-tests/DRF-lieks/2.png)|2023/4/30|

