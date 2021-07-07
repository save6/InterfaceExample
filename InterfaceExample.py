from abc import ABCMeta, abstractmethod

#Playerインターフェース
class Player(metaclass=ABCMeta):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass
  
    @abstractmethod
    def seek(self,position):
        pass

#動画再生クラス
class VideoPlayer(Player):
    def __init__(self,path):
        #何か処理があるつもりです
        print(path + 'からファイルをロードしました')

    def play(self):
        #何か処理があるつもりです
        print('動画を再生する処理を実行しました')
    
    def stop(self):
        #何か処理があるつもりです
        print('動画を停止する処理を実行しました')

    def seek(self,position):
        #何か処理があるつもりです
        print('動画の再生場所を' + str(position) + 'に変更しました')

#音楽再生クラス
class AudioPlayer(Player):
    def __init__(self,path):
        #何か処理があるつもりです
        print(path + 'からファイルをロードしました')

    def play(self):
        #何か処理があるつもりです
        print('音楽を再生する処理を実行しました')
    
    def stop(self):
        #何か処理があるつもりです
        print('音楽を停止する処理を実行しました')

    def seek(self,position):
        #何か処理があるつもりです
        print('音楽の再生場所を' + str(position) + 'に変更しました')

def sample(player):
    player.play() #再生
    player.seek(0.5) #半分まで再生場所を移動
    player.stop() #停止

if __name__=='__main__':
    print('### 動画再生のテスト ###')
    VIDEOPLAYER = VideoPlayer('my/video.mp4')
    sample(VIDEOPLAYER)

    print('### 音楽再生のテスト ###')
    AUDIOPLAYER = AudioPlayer('my/audio.mp4')
    sample(AUDIOPLAYER)
