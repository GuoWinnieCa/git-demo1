# GIT-DEMO

### 版本號檢視
- git --version

### 建立全域端使用者
- git config --global user.name winnie
- git config --global user.email yanweiguo64@gmail.com

### 檢視 git 設定
- git config --list

### vscode
- ctrl +shift +P(開啟設定)
		- 選擇Default
			- Terminal cmd
### 控管專案		
- git init

### 檔案加入控管
- git add <filename>
	-Untrack => Added => modified => deleted

### 檢視控管狀態
- git status

### 檢視物件內容(t:型態, p:內容)
- git cat-file -p shal(2+4) 內容
- git cat-file -t shal(2+4) 型態

### Added => Modified 
- git status
- git add <filename>(確認修改)
		
### 返悔修改
- git restore <filename>

### 檢視暫存區目前控管的內容
- git ls-files
- git ls-files -s

### 紀錄到倉庫
- git commit -m "message"
- git commit -am "message"
			- add . + commit

### 檢視目前 commit
- git log
- git log --oneline

- git commit -m 'XXXXXXX'
	
### 開啟vim編輯器	
- git commit
- i (insert)
- ESC 切換 
	- :wq (儲存後離開)
	- :q!	(離開)

### 合併上一個commit
- git commit --amend

### 指令刪除
- git rm -f filename (強制刪除)

- git restore --staged filename(恢復)
- git restore .

### 將檔案從暫存區 或 倉庫區 移出 至 untrack
- git rm --cached filename

### 檢視分支
- git branch
### 新增分之
- git branch 分支名稱
### - git checkout 分支名稱

- git branch

- git log
- git log --0neline

### 合併分支
- git checkout master (轉至master分支, 合併test 分支)
- git merge 某分支(test)

### 刪除分支 (一定是在別的分支刪除某分支,不可以自己刪除自己)
- git branch -D test

### 新增 + 切換
- git checkout -b 分枝名稱

###
- git commit -am "修改3.txt"     am =add . + commit

### 合併分支 git merge 某一分支名稱
### 合併衝突 不同分支改動同一檔案, 選擇合併方式
### 返悔合併 git merge--abort

- git checkout master

### 切換commit
- git checkout commit-shal
- 回到過去的修改
	- 新增分支, commit
	- 切回 master 進行合併
### 回到最新位置
- git checkout master

### 重置指令 
- git reset commit-shal  (soft)
- git reset --hard commit-shal	(hard)
- git reset ORIG_HEAD (恢復)
- git reset --hard HEAD(重置到最新commit)
- git reset --hard HEAD~1(重置到最新commit的前一個)

### 檢視所有歷程
- git reflog
	- 可以觀察commit-shal, 進行reset(重置指令)


### github




###…or create a new repository on the command line
- echo "# git-demo1" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/GuoWinnieCa/git-demo1.git
- git push -u origin main	

###…or push an existing repository from the command line
- git remote add origin https://github.com/GuoWinnieCa/git-demo1.git
- git branch -M main
- git push -u origin main

### 綁定 github 雲端的倉庫
- git remote add origin https://github.com/GuoWinnieCa/git-demo1.git
- git remote -v 
	- 檢視綁定的雲端倉庫url

### 本地同步雲端	
- git push
	- git push --set-upstream origin master
	- git push -u origin master

### 複製專案
- git clone https://github.com/GuoWinnieCa/git-demo1


### 老師的: git clone https://github.com/17app001/git-demo1.git
### 老師的: https://github.com/17app001/gym_demo


### 新增/修正/刪除分支
- git add .
- git commit -m "message"

### 本地端同步到雲端
- git push 推送

<<<<<<< HEAD
=======
### 雲端同步到本地端
- git pull 拉取

- 

- 

>>>>>>> 694ed1af4d72ae33ac8964ecfa00f0a9a8b473a4



