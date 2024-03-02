import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="使用 -h 获取参数说明")
    # 输入：播放页面url与下载模式
    options = parser.add_argument_group()
    options.add_argument('-u', '--url', type=str, help='下载视频的b站url\n')
    options.add_argument('-m', '--mode', type=int, default=1,
                         help='下载模式:\n'
                              ' 1 - 下载音视频及封面 (默认 可自行使用ffmpeg合并混流 高效且低占用)   \n'
                              ' 2 - 仅下载音频   \n'
                              ' 3 - 仅下载封面   \n'
                              ' 4 - 下载音视频及封面并合并 (慎用：需要moviepy库，且极度占用cpu与内存  -  [负载太高效率太低 - 已弃用] )   \n')
    options.add_argument('-q', '--quality', type=int, default=80, help='下载视频质量:\n'
                                                                       '16 - 360p    流畅   \n'
                                                                       '32 - 480p    清晰   \n'
                                                                       '64 - 720p    高清   \n'
                                                                       '74 - 720p60  高帧率   \n'
                                                                       '80 - 1080p   高清 (默认)   \n')
    options.add_argument('-p', '--partial', type=str, default='1-1', help='分p下载 从1算起 (默认只下载第1p)\n'
                                                                          '如下载第3至第7p 则为 3-7\n'
                                                                          '如仅下载第2p   则为 2-2\n')
    options.add_argument('-c', '--code', type=str, default='hev', help='下载视频编码方式，默认为hev  '
                                                                       '大部分b站视频支持 hev 和 avc 两种编码')
    return parser


if __name__ == "__main__":
    # 调试
    args = create_parser().parse_args()
    print(args)
