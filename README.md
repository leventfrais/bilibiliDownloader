# bilidownloader

基于b站视频流api的B站视频下载器  
参考 https://github.com/SocialSisterYi/bilibili-API-collect/tree/master 的api  
原理大致为 根据url取bvid，再申请cid与dash流信息。构造requests并伪造Referer绕过盗链检测后下载音视频流。最后使用ffmpeg合并  
支持多p cookie验证获取高质量度流 脚本自动化合并  
依赖库：re argparse os requests shutil datetime  

##### 已内置 ffmpeg   默认会生成合并音视频的脚本  

##### 如需下载1080p请将自己的b站cookie复制进myCookie.txt 以通过验证  

##### 简单的获取方法 访问b站时 F12打开开发者模式 找到网络 找Cookie即可  

## 使用方法：  

##### python 命令行 启动  

python bilidl.py -u [URL]  
bilidl.exe -u [URL]  

##### -u "[URL]" 就可以了。该指令会自动获取最高质量流，下载至downloads目录，同时会创建.bat脚本，执行即可合并音视频流生成最终.mp4文件  


## 详细参数  
##### 仅url是必须的参数，其他皆有默认值  

##### -h, --help            获取帮助  

##### -u , --url , URL     下载视频的b站url  

##### -c CODE, --code CODE  编码方式，默认为hev 大部分b站视频支持 hev 和 avc 两种编码  编码洁癖可选  

##### -m , --mode , MODE  下载模式:   

​								1 - 下载音视频及封面 (默认 可自行使用ffmpeg合并混流 高效且低占用) 

​								2 - 仅下载音频 

​								3 -  仅下载封面 

​								4 - 下载音视频及封面并合并
​                        			(慎用：需要moviepy库，且极度占用cpu与内存 - [负载太高效率太低 - 已弃用] )

##### -q , --quality , QUALITY  下载质量:  （未登录仅能下载480p，可以将自己的Cookie复制进根目录的myCookie.txt ）  

​								16 - 360p 流畅 

​								32 - 480p 清晰 

​								64 - 720p 高清 

​								74 - 720p60 高帧率 

​								80 - 1080p 高清 --- 默认  

                若无法获取则自动获取最高质量  

##### -p , --partial , PARTIAL

                分p下载 从1算起  --  默认只下载第1p

                如下载第3至第7p   则为 3-7 

                如仅下载第2p 则为 2-2
