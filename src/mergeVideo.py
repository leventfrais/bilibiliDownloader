import os


def creat_merge_bat_dir(folder_name, media_name):
    # 处理分p视频的批量合并 板正目录
    folder_name = os.path.join("downloads", folder_name)
    output_script = os.path.join(folder_name, f'{media_name}.bat')
    with open(output_script, "w") as merge_script:
        merge_script.write(f"REM 如遇到特殊字符如emoji 可能由于ffmpeg编码冲突无法混流 可以自行修改下面的音视频名称以及路径名称 进行混流\n"
                           f"REM 或是自己进行混流 (ffmpeg在项目根目录 从命令行进入) 命令为:\n"
                           f"REM ffmpeg.exe -i [视频.m4s] -i [音频.m4a] -c:v copy -c:a copy -f mp4 [混流文件].mp4\n"
                           f"cd ../\n"
                           f"cd ../\n")


def merge_media(folder_name, media_name, merged_name):
    output_dir = os.path.join("downloads", folder_name, merged_name)
    main_title = folder_name
    folder_name = os.path.join("downloads", folder_name)
    audio_input_path = os.path.join(folder_name, f'{merged_name}.m4a')
    video_input_path = os.path.join(folder_name, f'{merged_name}.m4s')
    output_script = os.path.join(folder_name, f'{main_title}.bat')

    # print(f"音频文件: {audio_input_path}")
    # print(f"视频文件: {video_input_path}")
    # print(f"输出脚本文件: {output_script}")
    # print(f"输出合并文件: {output_dir}")

    with open(output_script, "a") as merge_script:
        merge_script.write(
            f"ffmpeg.exe "
            f"-i \"{output_dir}.m4a\" "
            f"-i \"{output_dir}.m4s\" "
            f"-c:v copy "
            f"-c:a copy "
            f"-f mp4 \"{output_dir}.mp4\"\n")
    # os.system(f'"{output_dir}.bat"')


if __name__ == "__main__":
    foldername = "超爽七海娜娜米鬼叫合集"
    medianame = "超爽七海鬼叫合集"
    creat_merge_bat_dir(foldername, f"P1.{medianame}")
    merge_media(foldername, medianame, f"P1.{medianame}")
